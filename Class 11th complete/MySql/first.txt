/* Show list of existing databases  */
SHOW databases;

/* Show tables in an existing database */
SHOW tables;

select id,name,phno, ifNull(student_Name,"ghfgactor_idactor_idfirst_name") as "USER NAME" from contact c where c.name Like "%r"; 
select * from contact;

/* creating table with primary ey as auto increment */
CREATE TABLE mytable
(
id int NOT NULL auto_increment,
username varchar(100) NOT NULL,
email varchar(100) NOT NULL,
PRIMARY KEY (id)
);

/* use of back-tick 
CREATE TABLE `table`
(
`first name` VARCHAR(30)
);  */

/* getting data from recent created table */
select * from mytable;

/* inserting data to mytable  */
INSERT INTO mytable ( username, email )
VALUES ( "myuser", "myuser@example.com" );

/* Updating a row into a MySQL table */
UPDATE mytable SET username="Shashank" WHERE id=8;

/* Deleting a row into a MySQL table */
DELETE FROM mytable WHERE id=8;

/* Selecting rows based on conditions in MySQL */
SELECT * FROM mytable WHERE username = "myuser";

/*
|-----------|--------------------|----------------------------------------|
| Data Type | Before MySQL 5.6.4 | as of MySQL 5.6.4 |
|-----------|--------------------|----------------------------------------|
| YEAR | 1 byte | 1 byte |
| DATE | 3 bytes | 3 bytes |
| TIME | 3 bytes | 3 bytes + fractional seconds storage |
| DATETIME | 8 bytes | 5 bytes + fractional seconds storage |
| TIMESTAMP | 4 bytes | 4 bytes + fractional seconds storage |
|-----------|--------------------|----------------------------------------| 
*/

/*case and if */
/*SELECT st.name,
st.percentage,
CASE WHEN st.percentage >= 35 THEN 'Pass' ELSE 'Fail' END AS `Remark`
FROM student AS st ;*/

/* SELECT st.name,
st.percentage,
IF(st.percentage >= 35, 'Pass', 'Fail') AS `Remark`
FROM student AS st ;*/


/* SELECT title FROM books WHERE author_id = (SELECT id FROM authors WHERE last_name = 'Bar' AND
first_name = 'Foo'); */

/* SELECT * FROM stack WHERE username IN (SELECT username FROM signups WHERE email IS NULL); */

/* Deleteting Operations */
create table people
( id int primary key,
name varchar(100) not null,
gender char(1) not null
);
insert people (id,name,gender) values
(1,'Kathy','f'),(2,'John','m'),(3,'Paul','m'),(4,'Kim','f');
create table pets
( id int auto_increment primary key,
ownerId int not null,
name varchar(100) not null,
color varchar(100) not null
);
insert pets(ownerId,name,color) values
(1,'Rover','beige'),(2,'Bubbles','purple'),(3,'Spot','black and white'),
(1,'Rover2','white');

select * from pets;

/*we want to remove Paul's pets, the statement*/
DELETE p2
FROM pets p2
WHERE p2.ownerId in (
SELECT p1.id
FROM people p1
WHERE p1.name = 'Paul');

/*Basic delete */
/* DELETE FROM `myTable` WHERE `someColumn` = 'something' */