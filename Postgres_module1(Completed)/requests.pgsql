-- CREATE TABLE m_city (id serial, title varchar(50));
-- CREATE TABLE m_user (id serial, gender BOOLEAN, name varchar(50), email varchar(50), city_id INTEGER);

-- INSERT INTO m_city (title) VALUES ('Kharkiv'),('Kyiv'),('Zhitomyr'),('Kharkiv');

-- INSERT INTO m_user (name,email,gender,city_id) 
-- VALUES('Aaron','Aaron@gmail.com',FALSE,1),
-- ('Nifont','Nifont@gmail.com',FALSE,1),
-- ('Favst','Favst@gmail.com',FALSE,2),
-- ('Liodor','Liodor@gmail.com',FALSE,3),
-- ('Terentiy','Terentiy@gmail.com',FALSE,1),
-- ('Denis','Denis@gmail.com',FALSE,1),
-- ('Ovdokim','Ovdokim@gmail.com',FALSE,2),
-- ('Elisey','Elisey@gmail.com',FALSE,3),
-- ('Gennadiy','Gennadiy@gmail.com',FALSE,1),
-- ('Harisiy','Harisiy@gmail.com',FALSE,1),

-- ('Kira','Kira@gmail.com',TRUE,2),
-- ('Olimpiada','Olimpiada@gmail.com',TRUE,3),
-- ('Vladlena','Vladlena@gmail.com',TRUE,1),
-- ('Inessa','Inessa@gmail.com',TRUE,1),
-- ('Praskovya','Praskovya@gmail.com',TRUE,2),
-- ('Lidiya','Lidiya@gmail.com',TRUE,3),
-- ('Zoya','Zoya@gmail.com',TRUE,1),
-- ('Iraida','Iraida@gmail.com',TRUE,1),
-- ('Kristina','Kristina@gmail.com',TRUE,1),
-- ('Beatrisa','Beatrisa@gmail.com',TRUE,4);


SELECT 'This is '|| name || ', ' || CASE WHEN gender THEN 'she ' ELSE 'he ' END || 'has email '||email AS info FROM m_user;

SELECT count(city_id), m_city.title from m_user INNER JOIN m_city ON m_city.id=m_user.city_id GROUP BY city_id, m_city.title HAVING count(city_id)>10;
