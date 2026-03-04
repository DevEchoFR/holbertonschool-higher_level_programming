-- Creates the table unique_id with a default value of 1 and a UNIQUE constraint on id
CREATE TABLE IF NOT EXISTS unique_id (
    id   INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
