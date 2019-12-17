
SELECT * FROM student RIGHT JOIN team ON student.team_id=team.id;
SELECT * FROM student LEFT JOIN team ON student.team_id=team.id;
SELECT * FROM student RIGHT JOIN team ON student.team_id=team.id WHERE student.team_id IS NULL or team.id IS NULL;

SELECT * FROM student FULL JOIN team ON student.team_id=team.id WHERE student.team_id IS NOT NULL AND team.id IS NOT NULL;

SELECT team.name as team, subject.name as subject, teacher.first_name || ' ' || teacher.last_name as teacher FROM course 
FULL JOIN team ON course.team_id=team.id 
FULL JOIN subject_teacher ON course.subject_teacher_id=subject_teacher.id 
FULL JOIN subject ON subject.id=subject_teacher.subject_id 
FULL JOIN teacher ON teacher.id=subject_teacher.teacher_id ORDER BY team.name;

SELECT * FROM student FULL JOIN team ON student.team_id=team.id WHERE student.team_id IS NOT NULL AND team.id IS NOT NULL LIMIT 5 OFFSET 5;

SELECT * FROM student FULL JOIN team ON student.team_id=team.id WHERE student.team_id IS NOT NULL AND team.id IS NOT NULL AND left(first_name, 1) ='D' LIMIT 2;

SELECT * FROM student FULL JOIN team ON student.team_id=team.id WHERE student.team_id IS NOT NULL AND team.id IS NOT NULL AND left(first_name, 1) ='D' LIMIT 2 OFFSET 1;
