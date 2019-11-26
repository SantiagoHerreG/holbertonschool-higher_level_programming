-- Creates a new table
-- Creates several records inside the table
CREATE TABLE IF NOT EXISTS second_table (id INT,
name VARCHAR(256),
score INT);
-- Adds a record
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES ('1', "John", '10');
-- Adds a record
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES ('2', "Alex", '3');
-- Adds a record
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES ('3', "Bob", '14');
-- Adds a record
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES ('4', "George", '8');
