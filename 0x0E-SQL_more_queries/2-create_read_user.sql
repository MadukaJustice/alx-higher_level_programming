-- creates the database hbtn_0d_2
-- creates the user user_0d_2 with only SELECT priviledge
-- the user_0d_2 password should be set to user_0d_2_pwd
-- if the database or user already exists, the script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
