-- SQL to create credit mix table
CREATE DATABASE IF NOT EXISTS mix_db;
USE mix_db;
CREATE TABLE IF NOT EXISTS credit_mix (
    user_id INT PRIMARY KEY,
    types_used INT,
    total_types INT
);