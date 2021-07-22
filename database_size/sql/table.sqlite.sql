/*
Mock placeholder, so Sqlite3 tests can access the table without throwing a missing table error.
*/
CREATE VIEW database_size_table
AS
SELECT  'id' AS id,
        'schemaname' AS schema_name,
        'tablename' AS table_name,
        'tableowner' AS table_owner,
        123 AS size_in_bytes;
