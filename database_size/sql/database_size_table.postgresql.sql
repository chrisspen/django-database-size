/*
2013.5.12 CKS
Lists all table sizes.
*/
DROP VIEW IF EXISTS database_size_table CASCADE;
CREATE OR REPLACE VIEW database_size_table
AS
SELECT  CONCAT(CAST(schemaname AS VARCHAR), '-', CAST(tablename AS VARCHAR)) AS id,
        schemaname as schema_name,
        tablename as table_name,
        tableowner as table_owner,
        pg_total_relation_size(schemaname || '.' || tablename) as size_in_bytes
FROM    pg_tables;