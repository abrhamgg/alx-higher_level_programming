-- create user with password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON *.* TO 'user_0d_2';
CREATE DATABASE IF NOT EXIST 'hbtn_0d_2';
