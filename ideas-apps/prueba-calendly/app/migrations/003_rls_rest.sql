-- Tablas solo de servidor: RLS activo y SIN politicas = ningun rol cliente puede leer ni escribir.
-- El servidor las usa con la conexion privilegiada (service role / usuario dueño).
alter table email_outbox enable row level security;
alter table reminders enable row level security;
alter table webhook_events enable row level security;
-- Equipos: acceso solo al dueño del equipo (los miembros se anadiran con el flujo de invitaciones).
alter table teams enable row level security;
alter table team_members enable row level security;
alter table event_type_hosts enable row level security;
create policy own_teams on teams
  using (owner_id in (select id from users where auth_id = auth.uid()));
create policy own_team_members on team_members
  using (team_id in (select t.id from teams t join users u on u.id = t.owner_id where u.auth_id = auth.uid()));
create policy own_event_type_hosts on event_type_hosts
  using (event_type_id in (select e.id from event_types e join users u on u.id = e.owner_id where u.auth_id = auth.uid()));
