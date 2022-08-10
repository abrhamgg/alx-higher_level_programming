-- creates the database hbtn_0d_usa and the table states
CREATE DATABASE `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLEM IF NOT EXISTS `states` (
	`id` INT AUTO_INCREMENT NOT NULL PRIMARY_KEY,
	`name` VARCHAR(256)
	);
