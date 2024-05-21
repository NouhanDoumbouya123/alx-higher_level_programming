-- Select the hbtn_0c_0 database
USE hbtn_0c_0;

-- Converts hbtn_0c_0 database to utf8
-- Table: first_table to utf8
-- Field: name to utf8

ALTER DATABASE CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
