drop user 'admin'@'%';
drop user 'student'@'%';
drop user 'teacher'@'%';
-- 创建并授权管理员用户
CREATE USER 'admin'@'%' IDENTIFIED WITH mysql_native_password BY '***';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' WITH GRANT OPTION;
CREATE DATABASE IF NOT EXISTS `python`;
GRANT ALL PRIVILEGES ON `python`.* TO 'admin'@'%';

-- 创建并授权学生用户
CREATE USER 'student'@'%' IDENTIFIED WITH mysql_native_password BY '***';
GRANT SELECT ON *.* TO 'student'@'%';
CREATE DATABASE IF NOT EXISTS `python`;
GRANT SELECT ON `python`.* TO 'student'@'%';

-- 创建并授权教师用户
CREATE USER 'teacher'@'%' IDENTIFIED WITH mysql_native_password BY '***';
GRANT SELECT, INSERT, UPDATE, DELETE, FILE, EXECUTE ON *.* TO 'teacher'@'%';
CREATE DATABASE IF NOT EXISTS `python`;
GRANT SELECT, INSERT, UPDATE, DELETE, EXECUTE ON `python`.* TO 'teacher'@'%';