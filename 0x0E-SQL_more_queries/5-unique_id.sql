-- creates the table unique_id (should not fail if table exists)
-- unique_id description: id INT can't NULL, name VARCHAR(256)

CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
