-- SQL to create users table
CREATE DATABASE IF NOT EXISTS users_db;
USE users_db;
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);