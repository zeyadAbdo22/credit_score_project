-- SQL to create debt table
CREATE DATABASE IF NOT EXISTS debt_db;
USE debt_db;
CREATE TABLE IF NOT EXISTS debt (
    user_id INT PRIMARY KEY,
    used FLOAT,
    credit_limit FLOAT
);

