USE source_db;

-- ==========================================
-- Employees
-- ==========================================

CREATE TABLE employees (

    employee_id INT PRIMARY KEY,

    first_name VARCHAR(50),
    last_name VARCHAR(50),

    gender CHAR(1),

    birth_date DATE,
    hire_date DATE,

    department_id INT,

    city_id INT,

    job_title VARCHAR(100),

    salary DECIMAL(10,2),

    bonus DECIMAL(10,2),

    performance_score DECIMAL(3,2),

    employment_status VARCHAR(20)
);

-- ==========================================
-- Departments
-- ==========================================

CREATE TABLE departments (

    department_id INT PRIMARY KEY,

    department_name VARCHAR(50)
);

INSERT INTO departments VALUES
(1,'Engineering'),
(2,'HR'),
(3,'Finance'),
(4,'Marketing'),
(5,'IT'),
(6,'Sales'),
(7,'Operations'),
(8,'Legal'),
(9,'Customer Support'),
(10,'Research');

-- ==========================================
-- Cities
-- ==========================================

CREATE TABLE cities (

    city_id INT PRIMARY KEY,

    city_name VARCHAR(50)
);

INSERT INTO cities VALUES
(1,'Cairo'),
(2,'Giza'),
(3,'Alexandria'),
(4,'Mansoura'),
(5,'Tanta'),
(6,'Zagazig'),
(7,'Aswan'),
(8,'Luxor'),
(9,'Suez'),
(10,'Port Said'),
(11,'Ismailia'),
(12,'Minya'),
(13,'Assiut'),
(14,'Damietta'),
(15,'Fayoum');

select * from cities

select * from employees
limit 5

USE source_db;

SELECT COUNT(*) AS total_employees
FROM employees;
