create table email_outbox (
  id uuid primary key default gen_random_uuid(),
  kind text not null check (kind in ('booking_confirmation_guest','booking_confirmation_host','booking_cancelled')),
  booking_id uuid references bookings(id) on delete cascade,
  to_email text not null,
  subject text not null,
  body text not null,
  status text not null default 'pending' check (status in ('pending','sent','dead')),
  attempts integer not null default 0,
  next_try_at timestamptz not null default now(),
  last_error text,
  created_at timestamptz not null default now(),
  sent_at timestamptz,
  unique (booking_id, kind)                   -- idempotencia: un solo email de cada tipo por reserva
);
create index on email_outbox (next_try_at) where status = 'pending';
