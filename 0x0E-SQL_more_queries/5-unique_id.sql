-- Creates table unique_id
-- unique_id has field id with default value 1 and unique
CREATE TABLE IF NOT EXISTS unique_id (
	id	 INT		  NOT NULL DEFAULT 1 UNIQUE,
	name VARCHAR(256) NOT NULL
);