# Exercise 02 - Create a Table

CREATE TABLE employees (    # When creating a table, separate each column header with a comma (,)
    employee_id INT,
    first_name VARCHAR(30),     # Up to 30 characters for the names
    last_name VARCHAR(30),
    hourly_pay DECIMAL(5, 2),   # I don't except people to make more than $999.99 for hourly
    hire_date DATE
);

RENAME TABLE employees
          TO workers;

ALTER TABLE workers
        ADD phone_number VARCHAR(15);

ALTER TABLE workers
    RENAME COLUMN phone_number
               TO email;

ALTER TABLE workers
    MODIFY COLUMN email VARCHAR(75);

ALTER TABLE workers
    MODIFY email VARCHAR(75)
     AFTER last_name;    # If you need to move a column to the front, just use the keyword FIRST

ALTER TABLE workers
    MODIFY phone_number VARCHAR(15)
     AFTER last_name;

ALTER TABLE workers
    DROP COLUMN hire_date;

SELECT * FROM workers;