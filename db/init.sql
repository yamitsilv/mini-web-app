CREATE DATABASE IF NOT EXISTS `mini-web-app`;
USE mini-web-app;

CREATE TABLE IF NOT EXISTS `employees` (
  id INT PRIMARY KEY auto_increment,
  `first_name` text,
  `last_name` text,
  `personal_id` INT DEFAULT NULL,
  `department` text
);

--create dummy values
INSERT INTO `employees` (`first_name`, `last_name`, `personal_id`, `department`) VALUES
	('Israel', 'Israeli', 12345, 'Finance'),
	('Refael', 'Refaeli', 55555, 'Sales'),
	('Luci', 'Loo', 77777, 'Sales'),
	('Anna', 'Banana', 88888, 'Finance');
