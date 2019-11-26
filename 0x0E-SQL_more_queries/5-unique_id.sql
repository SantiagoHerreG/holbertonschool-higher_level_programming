-- creates the table unique_id
-- should not fail
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT '1' UNIQUE,
name VARCHAR(256));
