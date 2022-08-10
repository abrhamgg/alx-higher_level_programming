-- creates the database hbtn_0d_usa and the tables
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
	PRIMARY_KEY(`id`),
	`id` INT AUTO_INCREMENT NOT NULL,
	`state_id` INT NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	FOREIGN_KEY(`state_id`)
	REFERENCES `hbtn_od_usa`.`states`(`id`)
	);
