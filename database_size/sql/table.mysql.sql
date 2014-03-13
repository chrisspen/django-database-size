/*
2013.11.21 CKS
Lists all table sizes.
*/
DROP VIEW IF EXISTS database_size_table CASCADE;
CREATE OR REPLACE VIEW database_size_table
AS
SELECT  CONCAT(table_schema, '-', table_name) AS id,
        table_schema AS schema_name,
        table_name AS table_name,
        null AS table_owner, -- TODO: not available in MySQL?!
        (data_length + index_length) AS size_in_bytes
FROM    information_schema.TABLES
UNION ALL
SELECT  CONCAT(table_schema, '-byschema') AS id,
        table_schema AS schema_name,
        'ALL' AS table_name,
        'ALL' AS table_owner, -- TODO: not available in MySQL?!
        SUM(data_length + index_length) AS size_in_bytes
FROM    information_schema.TABLES
GROUP BY table_schema
UNION ALL
SELECT  'all-all' AS id,
        'ALL' AS schema_name,
        'ALL' AS table_name,
        'ALL' AS table_owner, -- TODO: not available in MySQL?!
        SUM(data_length + index_length) AS size_in_bytes
FROM    information_schema.TABLES;