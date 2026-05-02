create table public.profiles (
  id uuid default gen_random_uuid() primary key,
  name text,
  email text,
  password text,
  phone text,
  profession text,
  lat text,
  longt text,
  active text,
  passive text,
  jno text,
  jyes text,
  photo_url text,
  organisation text,
  description text,
  updated_at timestamp with time zone default timezone('utc'::text, now())
);
