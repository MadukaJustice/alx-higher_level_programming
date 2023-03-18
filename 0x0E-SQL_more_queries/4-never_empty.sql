-- creates the table id_not_null (should not fail if table exists)
-- force_name description: id INT can't NULL, name VARCHAR(256)

CREATE TABLE IF NOT EXISTS id_not_null (
       id INT DEFAULT 1,
       name VARCHAR(256)
);
