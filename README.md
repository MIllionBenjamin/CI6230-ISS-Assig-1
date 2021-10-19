# CI6230-ISS-Assig-1
 WANG MINGYE G2103776A, CI6230-Information System Security   Assignment 1 Solutions for Data Breaches

```sql
CREATE DATABASE user_test;

use user_test;

CREATE TABLE user (
    username VARCHAR(20) NOT NULL, 
    email_address VARCHAR(30) NOT NULL,
    home_address varchar(50) NOT NULL,
    PRIMARY KEY (username)
);

insert into user
(username, email_address, home_address)
values
('Alice', 'alice@ntu.edu.sg', 'Hall 1 201'),
('Bob', 'bob@ntu.edu.sg', 'Graduate Hall 2 301'),
('Chris', 'chris@ntu.edu.sg', 'Tan Lark Sye Walk 44');

CREATE USER 'read_only'@'localhost' IDENTIFIED BY 'readonly1';
GRANT SELECT ON *.* TO 'read_only'@'localhost';
```