SET GLOBAL general_log = 'ON';

SET GLOBAL log_output = 'TABLE';

SELECT
event_time,
user_host,
argument
FROM mysql.general_log
WHERE command_type='Query'
AND (
argument LIKE 'DROP%'
OR argument LIKE 'DELETE%'
OR argument LIKE 'TRUNCATE%'
OR argument LIKE 'ALTER%'
)
ORDER BY event_time DESC;


SHOW VARIABLES LIKE 'general_log';
DELETE FROM employees
where employee_id = '2';

CREATE TABLE test_monitor (
    id INT
);
DROP TABLE test_monitor;

SELECT
event_time,
user_host,
argument
FROM mysql.general_log
WHERE command_type='Query'
AND (
argument LIKE 'DROP%'
OR argument LIKE 'DELETE%'
OR argument LIKE 'TRUNCATE%'
OR argument LIKE 'ALTER%'
)
ORDER BY event_time DESC;