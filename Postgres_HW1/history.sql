postgres
=#
create database teams;
CREATE DATABASE
postgres
=# \c teams
You are now connected to database "teams" as user "postgres".
teams=# \d
Did not find any relations.
teams=#
create table team
(
	id serial,
	name text not null
);
CREATE TABLE
teams=# \d
             List of relations
 Schema |    Name     |   Type   |  Owner   
--------+-------------+----------+----------
 public | team        | table    | postgres
 public | team_id_seq | sequence | postgres
(2 rows)

teams=#
alter table team add column comments text default '';
ALTER TABLE
teams=#
select *
from team
teams
-# ;
 id | name | comments
----+------+----------
(0 rows)

teams=#
alter table team drop column comments;
ALTER TABLE
teams=#
select *
from team;
id | name
----+------
(0 rows)

teams=#
insert into team
	(name)
VALUES
	('Asphalt8'),
	('Asphalt Nitro');
INSERT 0 2
teams=#
select *
from team;
id |     name      
----+---------------
  1 | Asphalt8
  2 | Asphalt Nitro
(2 rows)

teams=#
create table producer
(
	id serial,
	first_name text not null default 'Dommy',
	last_name text not null default 'Imbecile'
);
CREATE TABLE
teams=# \d producer
                              Table "public.producer"
   Column   |  Type   | Collation | Nullable |               Default                
------------+---------+-----------+----------+--------------------------------------
 id         | integer |           | not null | nextval
('producer_id_seq'::regclass)
 first_name | text    |           | not null | 'Dommy'::text
 last_name  | text    |           | not null | 'Imbecile'::text

teams=#
alter table producer add column team_id integer default '-1';
ALTER TABLE
teams=# \d producer
                              Table "public.producer"
   Column   |  Type   | Collation | Nullable |               Default                
------------+---------+-----------+----------+--------------------------------------
 id         | integer |           | not null | nextval
('producer_id_seq'::regclass)
 first_name | text    |           | not null | 'Dommy'::text
 last_name  | text    |           | not null | 'Imbecile'::text
 team_id    | integer |           |          | '-1'::integer

teams=#
create table employe
(
	id serial,
	first_name text default 'Harry',
	last_name text default 'Potter',
	producer_id integer default '-1'
);
CREATE TABLE
teams=# \d employe
                               Table "public.employe"
   Column    |  Type   | Collation | Nullable |               Default               
-------------+---------+-----------+----------+-------------------------------------
 id          | integer |           | not null | nextval
('employe_id_seq'::regclass)
 first_name  | text    |           |          | 'Harry'::text
 last_name   | text    |           |          | 'Potter'::text
 producer_id | integer |           |          | '-1'::integer

teams=#
insert into producer
	(first_name)
VALUES
	('Ivan');
INSERT 0 1
teams=#
update producer SET last_name = 'Novikov' where id = 1;
UPDATE 1
teams=#
insert into employe
	(first_name)
VALUES
	('Dmitriy'),
	('Anatoliy');
INSERT 0 2
teams=#
update employe SET last_name = 'Shmatko' where first_name='Dmitriy';
UPDATE 1
teams=#
update employe SET last_name = 'Laktionov' where first_name='Anatoliy';
UPDATE 1
teams=#
truncate team 
teams-# ;
TRUNCATE TABLE
teams
=#
insert into team
	(
	id name
	teams
=#
insert into team
	(name)
VALUES
	('python'),
	('python_Ex1'),
	('python_ex2');
INSERT 0 3
teams=#
select *
from team;
id |    name    
----+------------
  3 | python
  4 | python_Ex1
  5 | python_ex2
(3 rows)

teams=#
alter table employe add column team_id integer default '-1';
ALTER TABLE
teams=#
update employe SET team_id = '5'
;
UPDATE 2
teams=#
create table teacher
(
	id serial,
	nick_name text default 'Boring_man'
);
CREATE TABLE
teams=#
alter table employe add column teacher_id integer default '-1';
ALTER TABLE
teams=#
select *
from employe;
id | first_name | last_name | producer_id | team_id | teacher_id 
----+------------+-----------+-------------+---------+------------
  1 | Dmitriy    | Shmatko   |          -1 |       5 |         -1
  2 | Anatoliy   | Laktionov |          -1 |       5 |         -1
(2 rows)

teams=#
insert into teacher
	(nick_name )
VALUES
	('Bandydan'),
	('Skytree2018');
INSERT 0 2
teams=#
create table subject
(
	id serial,
	name text not null
);
CREATE TABLE
teams=#
insert into subject
	(name)
VALUES
	('Python - introduction'),
	('Postgresql');
INSERT 0 2
teams=#
alter table teacher add column subject_id integer default '-1';
ALTER TABLE
teams=#
update teacher SET subject_id = 1 where id='1';
UPDATE 1
teams=#
update teacher SET subject_id = 2 where id='2';
UPDATE 1
teams=#
alter table employe drop column teacher_id ;
ALTER TABLE
teams=#
alter table employe drop column producer_id ;
ALTER TABLE
teams=#
drop table producer
;
DROP TABLE
teams
=#
insert into employe
	(first_name ,last_name, team_id)
VALUES
	('Ivan', 'Novikov', '5');
INSERT 0 1
teams=#
create table course
(
	id serial,
	team_id integer default '-1',
	subject_id integer default '-1',
	teacher_id integer default '-1'
);
CREATE TABLE
teams=#
insert into course
	(team_id , subject_id, teacher_id)
VALUES
	('5', '1', '1'),
	('5', '2', '2');
INSERT 0 2

teams=#
select *
from employe;
id | first_name | last_name | team_id 
----+------------+-----------+---------
  1 | Dmitriy    | Shmatko   |       5
  2 | Anatoliy   | Laktionov |       5
  3 | Ivan       | Novikov   |       5
(3 rows)

teams=#
select *
from team;
id |    name    
----+------------
  3 | python
  4 | python_Ex1
  5 | python_ex2
(3 rows)

teams=#
select *
from teacher;
id |  nick_name  | subject_id 
----+-------------+------------
  1 | Bandydan    |          1
  2 | Skytree2018 |          2
(2 rows)

teams=#
select *
from subject;
id |         name          
----+-----------------------
  1 | Python - introduction
  2 | Postgresql
(2 rows)

teams=#
select *
from course;
id | team_id | subject_id | teacher_id 
----+---------+------------+------------
  1 |       5 |          1 |          1
  2 |       5 |          2 |          2
(2 rows)

teams=#
