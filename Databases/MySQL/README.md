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

# `CREATE` a Database
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

# `INSERT` rows into a `TABLE`

# `SELECT` data `FROM` a `TABLE`

# `UPDATE` and `DELETE` data