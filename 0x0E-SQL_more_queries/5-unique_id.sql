-- creates the table unique_id on Mysql server
CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT UNIQUE DEFAULT 1,
	`name` VARCHAR(256)
	);
