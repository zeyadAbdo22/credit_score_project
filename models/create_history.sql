-- SQL to create history table
CREATE DATABASE IF NOT EXISTS history_db;
USE history_db;
CREATE TABLE IF NOT EXISTS history (
    user_id INT PRIMARY KEY,
    account_age INT
); 
