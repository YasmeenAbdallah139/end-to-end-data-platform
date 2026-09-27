--1. Create the users
CREATE USER 'db_admin'@'%' IDENTIFIED BY 'admin123';

CREATE USER 'readonly_user'@'%' IDENTIFIED BY 'readonly123';
--2. Grant privileges
GRANT ALL PRIVILEGES
ON source_db.*
TO 'db_admin'@'%';

GRANT SELECT
ON source_db.*
TO 'readonly_user'@'%';

FLUSH PRIVILEGES;
--3. Verify the grants
SHOW GRANTS FOR 'db_admin'@'%';

SHOW GRANTS FOR 'readonly_user'@'%';