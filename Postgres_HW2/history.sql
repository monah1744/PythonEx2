ma /home/monah1744 # su postgres
sh-4.4$ psql
psql (11.4)
Type "help" for help.

postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 less_02   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 teams     | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(5 rows)

postgres=# \c teams
You are now connected to database "teams" as user "postgres".
teams=# \d
                   List of relations
 Schema |          Name          |   Type   |  Owner   
--------+------------------------+----------+----------
 public | course                 | table    | postgres
 public | course_id_seq          | sequence | postgres
 public | student                | table    | postgres
 public | student_id_seq         | sequence | postgres
 public | subject                | table    | postgres
 public | subject_id_seq         | sequence | postgres
 public | subject_teacher        | table    | postgres
 public | subject_teacher_id_seq | sequence | postgres
 public | teacher                | table    | postgres
 public | teacher_id_seq         | sequence | postgres
 public | team                   | table    | postgres
 public | team_id_seq            | sequence | postgres
(12 rows)

teams=# select * from teacher;
 id | first_name | last_name 
----+------------+-----------
(0 rows)

teams=# insert INTO teacher 
(               DEFAULT VALUES  OVERRIDING      SELECT          TABLE           VALUES          
teams=# insert INTO teacher (
first_name  id          last_name   
teams=# insert INTO teacher (first_name , lsat

teams=# insert INTO teacher (first_name , las 

teams=# insert INTO teacher (first_name , last_nam

teams=# insert INTO teacher (first_name , last_nam

teams=# insert INTO teacher (first_name) VALUES ("Yevgeniy"),("Danyl");
ERROR:  column "Yevgeniy" does not exist
LINE 1: insert INTO teacher (first_name) VALUES ("Yevgeniy"),("Danyl...
                                                 ^
teams=# insert INTO teacher (first_name) VALUES ('Yevgeniy'),('Danyl');    
INSERT 0 2
teams=# select * from teacher;                                         
 id | first_name | last_name 
----+------------+-----------
  1 | Yevgeniy   |  
  2 | Danyl      |  
(2 rows)

teams=# select * from student;
 id | first_name | last_name | team_id 
----+------------+-----------+---------
(0 rows)

teams=# insert into student (fisrt  

teams=# insert into student (first_name, last_name) VALUES ('Ivan','Novikov'),('Dmitriy','Shmatko'),('Anatoliy','Laktionov'),('Dmytro','Hoi'),('Dmitriy','Miller'),('Roman','Lavro'),('Marina','Laktionova'),('Mike','Ivanov'),('Pavel','Lazarev'),('Sveta','Podtiaroba'),('Mykhailo','Havrilenko'); 
INSERT 0 11
teams=# select * from student;
 id | first_name | last_name  | team_id 
----+------------+------------+---------
  1 | Ivan       | Novikov    |      -1
  2 | Dmitriy    | Shmatko    |      -1
  3 | Anatoliy   | Laktionov  |      -1
  4 | Dmytro     | Hoi        |      -1
  5 | Dmitriy    | Miller     |      -1
  6 | Roman      | Lavro      |      -1
  7 | Marina     | Laktionova |      -1
  8 | Mike       | Ivanov     |      -1
  9 | Pavel      | Lazarev    |      -1
 10 | Sveta      | Podtiaroba |      -1
 11 | Mykhailo   | Havrilenko |      -1
(11 rows)

teams=# update 
course               pg_temp_1.           public.              subject_teacher
information_schema.  pg_toast.            student              teacher
pg_catalog.          pg_toast_temp_1.     subject              team
teams=# select * from team;                  
 id |    name    
----+------------
  3 | python
  4 | python_Ex1
  5 | python_ex2
(3 rows)

teams=# update team SET name = 'python_Ex2' where id='5';
UPDATE 1
teams=# select * from team;                              
 id |    name    
----+------------
  3 | python
  4 | python_Ex1
  5 | python_Ex2
(3 rows)

teams=# select id from team where name='python_Ex2';
 id 
----
  5
(1 row)

teams=# update student SET team_id = select id from team where name='python_Ex2';
ERROR:  syntax error at or near "select"
LINE 1: update student SET team_id = select id from team where name=...
                                     ^
teams=# update student SET team_id = (select id from team where name='python_Ex2');
UPDATE 11
teams=# select * from team;
 id |    name    
----+------------
  3 | python
  4 | python_Ex1
  5 | python_Ex2
(3 rows)

teams=# select * from student;
 id | first_name | last_name  | team_id 
----+------------+------------+---------
  1 | Ivan       | Novikov    |       5
  2 | Dmitriy    | Shmatko    |       5
  3 | Anatoliy   | Laktionov  |       5
  4 | Dmytro     | Hoi        |       5
  5 | Dmitriy    | Miller     |       5
  6 | Roman      | Lavro      |       5
  7 | Marina     | Laktionova |       5
  8 | Mike       | Ivanov     |       5
  9 | Pavel      | Lazarev    |       5
 10 | Sveta      | Podtiaroba |       5
 11 | Mykhailo   | Havrilenko |       5
(11 rows)

teams=# \d
                   List of relations
 Schema |          Name          |   Type   |  Owner   
--------+------------------------+----------+----------
 public | course                 | table    | postgres
 public | course_id_seq          | sequence | postgres
 public | student                | table    | postgres
 public | student_id_seq         | sequence | postgres
 public | subject                | table    | postgres
 public | subject_id_seq         | sequence | postgres
 public | subject_teacher        | table    | postgres
 public | subject_teacher_id_seq | sequence | postgres
 public | teacher                | table    | postgres
 public | teacher_id_seq         | sequence | postgres
 public | team                   | table    | postgres
 public | team_id_seq            | sequence | postgres
(12 rows)

teams=# create table team_subject (id serial, team_id integer not null, subject_id integer not null);
CREATE TABLE
teams=# \d
                   List of relations
 Schema |          Name          |   Type   |  Owner   
--------+------------------------+----------+----------
 public | course                 | table    | postgres
 public | course_id_seq          | sequence | postgres
 public | student                | table    | postgres
 public | student_id_seq         | sequence | postgres
 public | subject                | table    | postgres
 public | subject_id_seq         | sequence | postgres
 public | subject_teacher        | table    | postgres
 public | subject_teacher_id_seq | sequence | postgres
 public | teacher                | table    | postgres
 public | teacher_id_seq         | sequence | postgres
 public | team                   | table    | postgres
 public | team_id_seq            | sequence | postgres
 public | team_subject           | table    | postgres
 public | team_subject_id_seq    | sequence | postgres
(14 rows)

teams=# select * from subject;
 id |         name          
----+-----------------------
  1 | Python - introduction
  2 | Postgresql
(2 rows)

teams=# select * from subject_teacher;
 id | subject_id | teacher_id 
----+------------+------------
(0 rows)

teams=# update subject_teacher SET 
id          subject_id  teacher_id  
teams=# update subject_teacher SET subject_id = 1, tea  

teams=# update subject_teacher SET subject_id = 1, teacher_id = 2;
UPDATE 0
teams=# select * from subject_teacher;                            
 id | subject_id | teacher_id 
----+------------+------------
(0 rows)

teams=# insert;                                                      
insert
teams=# insert into subject_teacher (;
id          subject_id  teacher_id  
teams=# insert into subject_teacher (subject_id, teacher_id) VALUES('1','2'),('2','1');
INSERT 0 2
teams=# select * from subject_teacher;
 id | subject_id | teacher_id 
----+------------+------------
  1 |          1 |          2
  2 |          2 |          1
(2 rows)

teams=# insert into tea
teacher       team          team_subject  
teams=# insert into team_subject 
(               DEFAULT VALUES  OVERRIDING      SELECT          TABLE           VALUES
teams=# insert into team_subject (
id          subject_id  team_id     
teams=# insert into team_subject (subject_id , team_id)VALUES ('1','5'),('2','5');
INSERT 0 2
teams=# select * from course;
 id | team_id | subject_teacher_id 
----+---------+--------------------
  1 |       5 |                 -1
  2 |       5 |                 -1
(2 rows)

teams=# select * from subject_teacher;
 id | subject_id | teacher_id 
----+------------+------------
  1 |          1 |          2
  2 |          2 |          1
(2 rows)

teams=# update course SET subject_teacher_id =1 whe

teams=# update course SET subject_teacher_id =1 whe

teams=# update course SET subject_teacher_id =1 where id=1;
UPDATE 1
teams=# select * from course;
 id | team_id | subject_teacher_id 
----+---------+--------------------
  2 |       5 |                 -1
  1 |       5 |                  1
(2 rows)

teams=# update course SET subject_teacher_id =2 where id=2;
UPDATE 1
teams=# select * from course;
 id | team_id | subject_teacher_id 
----+---------+--------------------
  1 |       5 |                  1
  2 |       5 |                  2
(2 rows)

teams=# select * from subject_teacher;
 id | subject_id | teacher_id 
----+------------+------------
  1 |          1 |          2
  2 |          2 |          1
(2 rows)

teams=# 
