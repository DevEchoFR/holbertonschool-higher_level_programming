# SQL — Structured Query Language

SQL (Structured Query Language) is the standard language used to interact with **Relational Database Management Systems (RDBMS)** such as MySQL, PostgreSQL, SQLite, and others.

This project is built using **MySQL 8.0** on **Ubuntu 20.04 LTS**.

---

## Core SQL Categories

### DDL — Data Definition Language
> Defines and manages the structure of the database.

- `CREATE` — create a database or table
- `DROP` — delete a database or table
- `ALTER` — modify an existing table structure
- `SHOW` / `DESCRIBE` — inspect structure

### DML — Data Manipulation Language
> Manages the data inside tables.

- `INSERT` — add new records
- `UPDATE` — modify existing records
- `DELETE` — remove records
- `SELECT` — retrieve data

---

## Relational Database Basics

**Database** — a structured collection of data organized into tables.

**Table** — a set of rows and columns (like a spreadsheet).

**Row (record)** — a single entry in a table.

**Column (field)** — an attribute of the data (e.g., `id`, `name`, `score`).

**Primary Key (PK)** — a unique identifier for each row.

```sql
CREATE TABLE example (
    id   INT,
    name VARCHAR(256),
    score INT
);
```

---

## Essential SQL Commands

### Database level

```sql
-- List all databases
SHOW DATABASES;

-- Create a database (safe)
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

-- Delete a database (safe)
DROP DATABASE IF EXISTS hbtn_0c_0;
```

### Table level

```sql
-- List all tables in the current database
SHOW TABLES;

-- Create a table (safe)
CREATE TABLE IF NOT EXISTS first_table (
    id   INT,
    name VARCHAR(256)
);

-- Show full table definition
SHOW CREATE TABLE first_table;
```

### Read (Select)

```sql
-- Select all columns
SELECT * FROM first_table;

-- Select specific columns
SELECT score, name FROM second_table;
```

### Insert / Update / Delete

```sql
-- Insert a row
INSERT INTO first_table (id, name) VALUES (89, 'Best School');

-- Update a row by name
UPDATE second_table SET score = 10 WHERE name = 'Bob';

-- Delete rows by condition
DELETE FROM second_table WHERE score <= 5;
```

---

## Filtering, Sorting, and Limiting Data

### WHERE (filter rows)

```sql
-- Records with score >= 10
SELECT score, name FROM second_table WHERE score >= 10;

-- Exclude rows with no name
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '';
```

### ORDER BY (sorting)

```sql
-- Descending order (highest first)
SELECT score, name FROM second_table ORDER BY score DESC;
```

### COUNT (number of rows)

```sql
-- Count records matching a condition
SELECT COUNT(*) FROM first_table WHERE id = 89;
```

---

## Aggregate Functions (summary)

> Applied across multiple rows to produce a single result.

- `COUNT()` — total number of rows
- `AVG()` — average value
- `SUM()` — sum of values
- `MAX()` — highest value
- `MIN()` — lowest value

```sql
-- Average score
SELECT AVG(score) AS average FROM second_table;

-- Group by score and count occurrences
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
```

---

## NULL — Important concept

> A `NULL` value means the field has **no value** — it is not zero, not an empty string.

```sql
-- Filter out NULL names
WHERE name IS NOT NULL

-- Filter out NULL or empty names
WHERE name IS NOT NULL AND name != ''
```

---

## Data Types (used in this project)

| Type | Description |
|------|-------------|
| `INT` | Integer number |
| `VARCHAR(n)` | Variable-length string up to n characters |

---

## Requirements

- All SQL keywords in **UPPERCASE** (`SELECT`, `WHERE`, `CREATE`, etc.)
- Each file starts with a **comment** describing the task
- Each file ends with a **new line**
- Database name is always passed as an argument — no hardcoded `USE` statements (unless required)
- `SELECT` / `SHOW` / `DESCRIBE` / `EXPLAIN` forbidden where specified

---

## Usage

```bash
# Without a specific database
cat script.sql | mysql -hlocalhost -uroot -p

# With a specific database passed as argument
cat script.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

---

## Tasks

| # | File | What it does |
|---|------|--------------|
| 0 | [0-list_databases.sql](0-list_databases.sql) | List all databases |
| 1 | [1-create_database_if_missing.sql](1-create_database_if_missing.sql) | Create `hbtn_0c_0` safely |
| 2 | [2-remove_database.sql](2-remove_database.sql) | Drop `hbtn_0c_0` safely |
| 3 | [3-list_tables.sql](3-list_tables.sql) | List all tables of a database |
| 4 | [4-first_table.sql](4-first_table.sql) | Create `first_table (id, name)` |
| 5 | [5-full_table.sql](5-full_table.sql) | Show full definition of `first_table` |
| 6 | [6-list_values.sql](6-list_values.sql) | Select all rows from `first_table` |
| 7 | [7-insert_value.sql](7-insert_value.sql) | Insert row `(89, 'Best School')` |
| 8 | [8-count_89.sql](8-count_89.sql) | Count rows where `id = 89` |
| 9 | [9-full_creation.sql](9-full_creation.sql) | Create `second_table` and insert 4 rows |
| 10 | [10-top_score.sql](10-top_score.sql) | List all records ordered by score DESC |
| 11 | [11-best_score.sql](11-best_score.sql) | List records with `score >= 10` |
| 12 | [12-no_cheating.sql](12-no_cheating.sql) | Update Bob's score to 10 by name |
| 13 | [13-change_class.sql](13-change_class.sql) | Delete records with `score <= 5` |
| 14 | [14-average.sql](14-average.sql) | Compute average score |
| 15 | [15-groups.sql](15-groups.sql) | Count records per score, sorted by count |
| 16 | [16-no_link.sql](16-no_link.sql) | List records with non-empty name, sorted by score |

---

## One-line definitions (terminal)

| Term | Definition |
|------|------------|
| `DATABASE` | Organized collection of structured data |
| `TABLE` | A set of rows and columns storing related data |
| `PRIMARY KEY` | Unique identifier for each record in a table |
| `NULL` | Absence of a value — not zero, not empty string |
| `DDL` | SQL commands that define structure (CREATE, DROP, ALTER) |
| `DML` | SQL commands that manage data (INSERT, UPDATE, DELETE, SELECT) |
| `AGGREGATE` | A function that summarizes multiple rows into one value |

---

## Author

**DevEchoFR** — [GitHub](https://github.com/DevEchoFR)

