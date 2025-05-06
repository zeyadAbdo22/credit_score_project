-- SQL to create payments table
CREATE DATABASE IF NOT EXISTS payments_db;
USE payments_db;
CREATE TABLE IF NOT EXISTS payments (
    user_id INT PRIMARY KEY,
    on_time INT,
    total INT
);
