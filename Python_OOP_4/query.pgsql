CREATE TABLE IF NOT EXISTS programmer (id_programmer serial,
first_name varchar(48),
last_name varchar(48),
email varchar(48),
hired_at date,
phone varchar(20),
salary_per_day INTEGER,
main_skill varchar(48)
);
SELECT * FROM programmer;

CREATE TABLE IF NOT EXISTS recruiter (id_recruiter serial,
first_name varchar(48),
last_name varchar(48),
email varchar(48),
hired_at date,
phone varchar(20),
salary_per_day INTEGER
);
SELECT * FROM recruiter;

CREATE TABLE IF NOT EXISTS candidate (id_candidate serial,
first_name varchar(48),
last_name varchar(48),
email varchar(48),
hired_at date,
phone varchar(20),
main_skill varchar(48)
);
SELECT * FROM candidate;

CREATE TABLE IF NOT EXISTS vacancy (id_candidate serial,
title varchar(48),
salary INTEGER,
main_skill varchar(48),
technologies text,
id_recruiter INTEGER,
hired_candidate BOOLEAN,
status BOOLEAN
);
SELECT * FROM vacancy;

CREATE TABLE IF NOT EXISTS interview (id_interview serial,
id_vacancy INTEGER,
id_programmer INTEGER,
id_recruiter INTEGER,
id_candidate INTEGER,
datetime timestamp,
feedback text,
result BOOLEAN
);
SELECT * FROM interview;

