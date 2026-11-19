create table public.studio_usage(user_id uuid references auth.users on delete cascade, day date, used integer not null check(used>=0), primary key(user_id,day));
create table public.studio_posts(id uuid primary key default gen_random_uuid(), user_id uuid not null references auth.users on delete cascade, category text not null check(category in ('Dev Q&A','Showcase','Drops','Club Hub')), title text not null check(char_length(title) between 5 and 120), body text not null check(char_length(body) between 10 and 3000), author text not null check(char_length(author) between 1 and 40), created_at timestamptz not null default now(), hidden boolean not null default false);
create table public.studio_reports(id uuid primary key default gen_random_uuid(), post_id uuid not null references public.studio_posts on delete cascade, reporter uuid not null references auth.users on delete cascade, reason text not null check(reason in ('Spam','Quấy rối','Thông tin cá nhân','Khác')), created_at timestamptz not null default now(), unique(post_id,reporter));
create index studio_posts_newest on public.studio_posts(created_at desc) where not hidden;
create index studio_posts_user_date on public.studio_posts(user_id,created_at);
create index studio_reports_reporter_date on public.studio_reports(reporter,created_at);
alter table public.studio_usage enable row level security;
alter table public.studio_posts enable row level security;
alter table public.studio_reports enable row level security;
revoke all on public.studio_usage, public.studio_posts, public.studio_reports from anon,authenticated;
grant select,insert,update,delete on public.studio_usage,public.studio_posts,public.studio_reports to service_role;
create function public.studio_reserve(p_user uuid,p_day date,p_limit int) returns int language plpgsql set search_path='' as $$ declare n int; begin
  insert into public.studio_usage as q values(p_user,p_day,1) on conflict (user_id,day) do update set used=q.used+1 where p_limit is null or q.used<p_limit returning used into n;
  return coalesce(n,-1);
end $$;
create function public.studio_refund(p_user uuid,p_day date) returns void language sql set search_path='' as $$ update public.studio_usage set used=greatest(0,used-1) where user_id=p_user and day=p_day; $$;
create function public.studio_add_post(p_user uuid,p_title text,p_body text,p_category text,p_author text) returns void language plpgsql set search_path='' as $$ begin
  perform pg_advisory_xact_lock(hashtextextended(p_user::text,1));
  if (select count(*) from public.studio_posts where user_id=p_user and created_at>now()-interval '1 day')>=10 then raise exception 'post limit';end if;
  insert into public.studio_posts(user_id,title,body,category,author) values(p_user,p_title,p_body,p_category,p_author);
end $$;
create function public.studio_add_report(p_user uuid,p_post uuid,p_reason text) returns void language plpgsql set search_path='' as $$ begin
  perform pg_advisory_xact_lock(hashtextextended(p_user::text,2));
  if (select count(*) from public.studio_reports where reporter=p_user and created_at>now()-interval '1 day')>=20 then raise exception 'report limit';end if;
  insert into public.studio_reports(reporter,post_id,reason) values(p_user,p_post,p_reason);
end $$;
revoke execute on function public.studio_reserve(uuid,date,int),public.studio_refund(uuid,date),public.studio_add_post(uuid,text,text,text,text),public.studio_add_report(uuid,uuid,text) from public,anon,authenticated;
grant execute on function public.studio_reserve(uuid,date,int),public.studio_refund(uuid,date),public.studio_add_post(uuid,text,text,text,text),public.studio_add_report(uuid,uuid,text) to service_role;
create table public.studio_replies(id uuid primary key default gen_random_uuid(), post_id uuid not null references public.studio_posts on delete cascade, user_id uuid not null references auth.users on delete cascade, author text not null check(char_length(author) between 1 and 40), body text not null check(char_length(body) between 5 and 2000), created_at timestamptz not null default now());
create index studio_replies_post_date on public.studio_replies(post_id,created_at);
create index studio_replies_user_date on public.studio_replies(user_id,created_at);
alter table public.studio_replies enable row level security;
revoke all on public.studio_replies from anon,authenticated;
grant select,insert,update,delete on public.studio_replies to service_role;
create function public.studio_add_reply(p_user uuid,p_post uuid,p_body text,p_author text) returns void language plpgsql set search_path='' as $$ begin
  perform pg_advisory_xact_lock(hashtextextended(p_user::text,3));
  if not exists(select 1 from public.studio_posts where id=p_post and not hidden) or (select count(*) from public.studio_replies where user_id=p_user and created_at>now()-interval '1 day')>=30 then raise exception 'not available';end if;
  insert into public.studio_replies(user_id,post_id,body,author) values(p_user,p_post,p_body,p_author);
end $$;
revoke execute on function public.studio_add_reply(uuid,uuid,text,text) from public,anon,authenticated;
grant execute on function public.studio_add_reply(uuid,uuid,text,text) to service_role;
