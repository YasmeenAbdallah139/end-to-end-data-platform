-- Unoptimized Query
SELECT *
FROM employees
WHERE first_name = 'Ahmed';


EXPLAIN
SELECT *
FROM employees
WHERE first_name = 'Ahmed';


CREATE INDEX idx_first_name
ON employees(first_name);

EXPLAIN ANALYZE
SELECT *
FROM employees
WHERE first_name = 'Ahmed';

