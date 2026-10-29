# Structured Query Language
Structured Query Language (SQL) is used to create, retrieve, update and delete data from a database.

There are two types of databases: Relational and non-relational.
A relational database resembles an Excel spreadsheet, with there being rows and columns. Tables within a relational database can form relations with one another via keys.
A non-relational database is when data is organized in any format but a table, such as a JSON file, key-value pairs (dictionaries), graph data structures, etc.

To utilize data in a relational database, we would use SQL, and for a non-relational database we use NoSQL.

To write SQL statements, we utilize a Database Management System (DBMS) which is a workspace to write SQL statements and edit the database.
Different types of DBMS include: MySQL, PostgreSQL, Oracle, Microsoft SQL Server, JetBrains DataGrip, etc.

## Setting Up a MySQL Server in JetBrains DataGrip
To create a MySQL data source in JetBrains DataGrip follow the steps below:

1. Go to the `Database Explorer` Window and click the `New` button, scroll down the popup menu and hover over `Data Source`, and then click `MySQL`
2. Enter your connection details such as:
   - Source name
   - Connection type
   - Host and Port
   - Authentication (if any)
   - Database name
   - URL (updates automatically)
3. Make any further changes in the other tabs
4. Click the `Apply` button to accept changes

## Setting up a Query Console in JetBrains Desktop
To utilize SQL commands in JetBrains DataGrip follow the steps below:

1. Go to the `Database Explorer` Window and click the `New` button
2. Scroll down the popup menu and click `Query Console`

The `Query Console` allows end users to write and execute SQL statements directly, while a `Query File` is an `.sql` file that you can create, store, and manage within a project.

# `CREATE` a `DATABASE`
A database is essentially a folder that acts a container for the files, or tables.

Every command made in the console must end with a semicolon `;`.

To create, use, and delete a database, go to the query window and use the following commands:
```SQL
CREATE DATABASE myDB; # Create the database via a CREATE statement w/the DATABASE keyword followed by the name of the database
USE myDB;             # Set the database as default via a USE statement w/the database name
DROP DATABASE myDB;   # Delete the database via a DROP statement w/the DATABASE keyword followed by the database name
```

To ensure that a database cannot be edited, use an `ALTER` statement and set `READ ONLY` to `1`:</br>
```SQL
ALTER DATABASE myDB READ ONLY = 1;  # Data within the database cannot be modified
ALTER DATABASE myDB READ ONLY = 0;  # Data within the database can be modified
```

# `CREATE` a `TABLE`
A table in a relational database consists of rows and columns. In this section, we'll be creating the table.

To create a table, go to the query window and use the following commands:
```SQL
CREATE TABLE employees (    # When creating a table, separate each column header with a comma (,)
    employee_id INT,
    first_name VARCHAR(30),     # Up to 30 characters for the names
    last_name VARCHAR(30),
    hourly_pay DECIMAL(5, 2),   # I don't except people to make more than $999.99 for hourly
    hire_date DATE
);
```
Once you execute the code and refresh the `Database Explorer` window, you should see a `tables/` folder appear within your database along with the `employees` table and the column header row.

To rename a table, utilize the `RENAME` statement:
```SQL
RENAME TABLE employees
          TO workers;
```

To alter a table, utilize the `ALTER` statement:
```SQL
ALTER TABLE workers
ADD phone_number VARCHAR(15);

ALTER TABLE workers
RENAME COLUMN phone_number TO email;

ALTER TABLE workers
MODIFY COLUMN email VARCHAR(75);

ALTER TABLE workers
MODIFY email VARCHAR(75)
AFTER last_name;    # If you need to move a column to the front, just use the keyword FIRST
```

To select data from a table to view it in the console utilize a `SELECT` statement:
```SQL
SELECT *         # The asterisk is a wild-card character meaning all
FROM workers;    # The data within the table will show on the console
```

To delete a table, utilize the `DROP` statement:
```SQL
DROP TABLE workers;
```

# `INSERT` rows into a `TABLE`
```SQL
```

# `SELECT` data `FROM` a `TABLE`
```SQL
```

# `UPDATE` and `DELETE` data
```SQL
```