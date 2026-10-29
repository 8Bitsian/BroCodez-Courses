# Exercise 01 - Create a Database

CREATE DATABASE myDB; # Create the database via a CREATE statement w/the DATABASE keyword followed by the name of the database
USE myDB;             # Set the database as default via a USE statement w/the database name
DROP DATABASE myDB;   # Delete the database via a DROP statement w/the DATABASE keyword followed by the database name

ALTER DATABASE myDB READ ONLY = 1;  # Data within the database cannot be modified
ALTER DATABASE myDB READ ONLY = 0;  # Data within the database can be modified