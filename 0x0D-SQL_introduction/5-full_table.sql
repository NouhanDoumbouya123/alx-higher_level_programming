-- Script to print the full description of the table first_table from the database hbtn_0c_0

-- Redirect the output of the SHOW CREATE TABLE statement to a temporary table
CREATE TEMPORARY TABLE IF NOT EXISTS tmp_description AS
    SHOW CREATE TABLE hbtn_0c_0.first_table;

-- Retrieve the full description of the table from the temporary table
SELECT CONCAT_WS('\n', Create_Table, Create_View) AS 'Table Description'
FROM tmp_description;
