-- Get the table creation query from the information_schema
SELECT 
    CONCAT('Table   ', TABLE_NAME) AS 'Table',
    CONCAT('CREATE TABLE ', TABLE_NAME, ' (') AS 'Create Table',
    GROUP_CONCAT(
        CONCAT(COLUMN_NAME, ' ', COLUMN_TYPE,
               IF(IS_NULLABLE = 'NO', ' NOT NULL', ''),
               IF(COLUMN_DEFAULT IS NOT NULL, CONCAT(' DEFAULT ', QUOTE(COLUMN_DEFAULT)), ''),
               IF(EXTRA != '', CONCAT(' ', EXTRA), '')), ',\n  ')
    AS 'Table Description'
FROM
    information_schema.columns
WHERE
    table_schema = 'hbtn_0c_0' AND table_name = 'first_table'
GROUP BY
    TABLE_NAME;
