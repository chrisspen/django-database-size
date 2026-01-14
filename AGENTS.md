# AGENTS.md

## Project Overview

**django-database-size** is a Django admin extension that adds a monitoring page to display the size of all database tables. It provides read-only access to table size information directly in the Django admin interface.

**Access URL:** `/admin/database_size/`

## Key Features

- Read-only admin interface showing table sizes organized by schema
- Support for multiple databases via admin filter
- Human-readable size formatting (bytes, KB, MB, GB, TB, PB)
- Database-specific SQL views for PostgreSQL, MySQL, and SQLite

## Project Structure

```
django-database-size/
├── database_size/               # Main application package
│   ├── __init__.py             # Version definition
│   ├── admin.py                # Django admin integration (TableAdmin, SelectDatabaseListFilter)
│   ├── apps.py                 # AppConfig (DjangoDatabaseSizeConfig)
│   ├── models.py               # Table model (unmanaged, uses database views)
│   ├── utils.py                # Utility for humanizing byte sizes
│   ├── sql/                    # Database-specific SQL view definitions
│   │   ├── table.postgresql.sql
│   │   ├── table.mysql.sql
│   │   ├── table.sqlite3.sql
│   │   └── table.sqlite.sql
│   └── tests/                  # Test suite
│       ├── settings.py         # Django test settings (SQLite in-memory)
│       ├── urls.py             # Test URL configuration
│       ├── tests.py            # Test cases
│       └── manage.py           # Test management script
├── setup.py                    # Package configuration
├── tox.ini                     # Tox testing configuration
├── .travis.yml                 # Travis CI configuration
├── requirements.txt            # Runtime dependencies (empty - Django only)
├── requirements-min-django.txt # Minimum Django version
├── requirements-test.txt       # Test dependencies
├── MANIFEST.in                 # Package manifest
└── publish.sh                  # Build and publish script
```

## Architecture

### Model Layer (`models.py`)
- **Table**: Unmanaged Django model that maps to a database view (`database_size_table`)
- The model does not create migrations; it reads from SQL views defined in `sql/` directory
- Fields: `id`, `schema_name`, `table_name`, `table_owner`, `size_in_bytes`

### Admin Layer (`admin.py`)
- **TableAdmin**: ModelAdmin with read-only display of table sizes
- **SelectDatabaseListFilter**: Custom filter allowing selection between configured databases
- Disables add/delete/change operations (purely informational)

### Database Views (`sql/`)
Each supported database has a SQL view that calculates table sizes:
- **PostgreSQL**: Uses `pg_tables` and `pg_total_relation_size()`
- **MySQL**: Queries `information_schema.TABLES` with `data_length + index_length`
- **SQLite**: Placeholder/mock for testing (returns dummy data)

### Utilities (`utils.py`)
- **humanize_bytes()**: Converts byte counts to human-readable format (KB, MB, GB, etc.)

## Development

### Running Tests
```bash
# Via tox (recommended)
tox

# Direct Django test runner
django-admin.py test --traceback --settings=database_size.tests.settings database_size.tests.tests.Tests

# Specific test
TESTNAME=test_example tox
```

### Test Environment
- Uses SQLite in-memory database
- Test settings located in `database_size/tests/settings.py`
- Tests verify admin page loads correctly and model returns expected data

### Code Style
```bash
./pep8.sh  # Run PEP 8 validation
```

### Publishing
```bash
./publish.sh  # Build and upload to PyPI
```

## Dependencies

- **Runtime**: Django only (no additional packages)
- **Testing**: tox, pylint, twine

## Important Notes for AI Agents

1. **Unmanaged Model**: The `Table` model has `managed = False`. Do not create migrations for it.

2. **SQL Views**: Table size data comes from database-specific SQL views. When adding new database support, create a corresponding `table.<backend>.sql` file.

3. **Multi-Database Support**: The admin supports multiple databases via Django's `connections`. The `SelectDatabaseListFilter` routes queries to the selected database.

4. **Read-Only Design**: This is intentionally read-only. The admin class explicitly disables all modification operations.

5. **Version Management**: Version is defined in `database_size/__init__.py` as `VERSION` tuple and `__version__` string.

6. **Test Isolation**: Tests use their own settings file with an in-memory SQLite database to avoid affecting production data.

## Coding Conventions

- Follow PEP 8 style guidelines
- Maintain compatibility with supported Python and Django versions
- Keep the package minimal - no unnecessary dependencies
- All SQL files should be idempotent (use `CREATE OR REPLACE VIEW`)
