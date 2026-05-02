create table public.complaints (
  email text,
  complaints text,
  photo_url text,
  updated_at timestamp  with time zone default timezone('utc'::text, now()) 
);
