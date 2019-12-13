-- INSERT INTO teacher (first_name, last_name) VALUES ('Danil','Ivanov');
-- UPDATE teacher SET first_name='Vladislav',last_name='Ponomaryov' WHERE id=3;
-- DELETE FROM teacher WHERE id=4;
SELECT team.name, subject.name, teacher.first_name, teacher.last_name FROM course INNER JOIN team ON course.team_id=team.id INNER JOIN subject_teacher ON course.subject_teacher_id=subject_teacher.id INNER JOIN subject ON subject.id=subject_teacher.subject_id INNER JOIN teacher ON teacher.id=subject_teacher.teacher_id;

SELECT * FROM student ORDER BY first_name;

SELECT count(*), first_name FROM student WHERE first_name like 'D%' GROUP BY first_name ORDER BY first_name ;

SELECT count(*), first_name FROM student WHERE first_name like 'D%' GROUP BY first_name HAVING count(*)>1 ORDER BY first_name ;

SELECT count(*),name FROM student INNER JOIN team ON student.team_id=team.id WHERE team_id='5' GROUP BY name;

-- SELECT * FROM teacher;
--  UPDATE teacher SET first_name='Daniil',last_name='Marynich' WHERE id='2';

SELECT first_name,last_name,name FROM student INNER JOIN team ON student.team_id=team.id WHERE team_id='5' ORDER BY first_name,last_name LIMIT 5 OFFSET 3;



SELECT * FROM student FETCH NEXT ROW ONLY ;

SELECT * FROM student ORDER BY first_name FETCH NEXT 5 ROW ONLY ;

SELECT * FROM student ORDER BY first_name OFFSET 3 ROWS FETCH NEXT 5 ROW ONLY ;

-- CREATE TABLE student_snap AS TABLE student WITH NO DATA;
-- INSERT INTO student_snap SELECT * FROM student;
SELECT * FROM student_snap;
TRUNCATE TABLE student_snap;
SELECT * FROM student_snap;
INSERT INTO student_snap SELECT * FROM student;
SELECT * FROM student_snap;
