-- Schema del clon de scheduling. Postgres 14+. Tiempos en timestamptz (UTC).
create extension if not exists pgcrypto;
create extension if not exists btree_gist;

create table users (
  id uuid primary key default gen_random_uuid(),
  auth_id uuid unique,                       -- id en Supabase Auth
  email text not null unique,
  name text not null,
  slug text not null unique,                 -- /{slug}/{event-slug}
  timezone text not null default 'UTC',
  plan text not null default 'free' check (plan in ('free','standard','teams')),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table calendar_accounts (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references users(id) on delete cascade,
  provider text not null check (provider in ('google','outlook')),
  external_account text not null,
  refresh_token_enc text not null,           -- cifrado en la app, nunca en claro
  is_main boolean not null default false,
  check_conflicts boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (user_id, provider, external_account)
);
create index on calendar_accounts (user_id);
create unique index one_main_calendar on calendar_accounts (user_id) where is_main;

create table availability_rules (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references users(id) on delete cascade,
  weekday smallint not null check (weekday between 0 and 6),
  start_local time not null,                 -- hora local en users.timezone
  end_local time not null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  check (end_local > start_local)
);
create index on availability_rules (user_id, weekday);

create table teams (
  id uuid primary key default gen_random_uuid(),
  owner_id uuid not null references users(id) on delete cascade,
  name text not null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index on teams (owner_id);

create table team_members (
  team_id uuid not null references teams(id) on delete cascade,
  user_id uuid not null references users(id) on delete cascade,
  role text not null default 'member' check (role in ('owner','member')),
  created_at timestamptz not null default now(),
  primary key (team_id, user_id)
);
create index on team_members (user_id);

create table event_types (
  id uuid primary key default gen_random_uuid(),
  owner_id uuid not null references users(id) on delete cascade,
  team_id uuid references teams(id) on delete cascade,
  slug text not null,
  name text not null,
  duration_min integer not null check (duration_min between 5 and 720),
  location_kind text not null default 'video'
    check (location_kind in ('video','phone','in_person','custom')),
  location_detail text,
  kind text not null default 'one_on_one'
    check (kind in ('one_on_one','round_robin','group')),
  buffer_before_min integer not null default 0 check (buffer_before_min >= 0),
  buffer_after_min integer not null default 0 check (buffer_after_min >= 0),
  daily_limit integer check (daily_limit > 0),
  min_notice_min integer not null default 240,
  max_days_ahead integer not null default 60,
  active boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (owner_id, slug)
);
create index on event_types (owner_id);
create index on event_types (team_id);

create table event_type_hosts (               -- quien puede recibir (round robin)
  event_type_id uuid not null references event_types(id) on delete cascade,
  user_id uuid not null references users(id) on delete cascade,
  priority integer not null default 0,
  primary key (event_type_id, user_id)
);
create index on event_type_hosts (user_id);

create table bookings (
  id uuid primary key default gen_random_uuid(),
  event_type_id uuid not null references event_types(id) on delete restrict,
  host_id uuid not null references users(id) on delete restrict,
  start_at timestamptz not null,
  end_at timestamptz not null,
  guest_name text not null,
  guest_email text not null,
  guest_timezone text not null,
  status text not null default 'confirmed'
    check (status in ('confirmed','cancelled','rescheduled')),
  answers jsonb not null default '{}',
  manage_token text not null unique default encode(gen_random_bytes(24),'hex'),
  external_event_id text,                    -- id del evento en el calendario
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  constraint no_zero_length check (end_at > start_at),
  -- Dos invitados no pueden reservar el mismo hueco del mismo anfitrion.
  constraint no_double_booking exclude using gist
    (host_id with =, tstzrange(start_at, end_at) with &&)
    where (status = 'confirmed')
);
create index on bookings (host_id, start_at);
create index on bookings (event_type_id);
create index on bookings (guest_email);

create table reminders (
  id uuid primary key default gen_random_uuid(),
  booking_id uuid not null references bookings(id) on delete cascade,
  send_at timestamptz not null,
  kind text not null check (kind in ('24h','1h')),
  sent_at timestamptz,
  unique (booking_id, kind)                  -- idempotencia: no enviar dos veces
);
create index on reminders (send_at) where sent_at is null;

create table webhook_events (                -- dedupe de webhooks entrantes
  provider text not null,
  external_id text not null,
  received_at timestamptz not null default now(),
  primary key (provider, external_id)
);

-- Acceso: RLS en Supabase para todo lo que lee el anfitrion autenticado.
alter table users enable row level security;
alter table calendar_accounts enable row level security;
alter table availability_rules enable row level security;
alter table event_types enable row level security;
alter table bookings enable row level security;
create policy own_user on users using (auth_id = auth.uid());
create policy own_calendars on calendar_accounts
  using (user_id in (select id from users where auth_id = auth.uid()));
create policy own_rules on availability_rules
  using (user_id in (select id from users where auth_id = auth.uid()));
create policy own_event_types on event_types
  using (owner_id in (select id from users where auth_id = auth.uid()));
create policy host_bookings on bookings
  using (host_id in (select id from users where auth_id = auth.uid()));
-- El invitado no tiene cuenta: crea/lee su reserva solo por rutas de servidor
-- con service role y manage_token. Nunca acceso directo de anon a bookings.
