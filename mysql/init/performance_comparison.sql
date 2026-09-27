CREATE INDEX idx_hire_date
ON employees(hire_date);
EXPLAIN
SELECT COUNT(*)
FROM employees
WHERE hire_date >= '2023-01-01'
  AND hire_date < '2024-01-01';

EXPLAIN ANALYZE
SELECT COUNT(*)
FROM employees
WHERE hire_date >= '2023-01-01'
  AND hire_date < '2024-01-01';