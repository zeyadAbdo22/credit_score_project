-- Insert sample data for all tables

-- Users data
USE users_db;
INSERT INTO users (user_id, name, email) VALUES
(1, 'Ahmed Mohamed', 'ahmed.m@example.com'),
(2, 'Fatima Ali', 'fatima.a@example.com'),
(3, 'Youssef Hassan', 'youssef.h@example.com'),
(4, 'Amina Khalid', 'amina.k@example.com'),
(5, 'Omar Ibrahim', 'omar.i@example.com'),
(6, 'Layla Mahmoud', 'layla.m@example.com'),
(7, 'Karim Abdullah', 'karim.a@example.com'),
(8, 'Nour El-Din', 'nour.e@example.com'),
(9, 'Hana Saleh', 'hana.s@example.com'),
(10, 'Tariq Farouk', 'tariq.f@example.com');

-- Payments data
USE payments_db;
INSERT INTO payments (user_id, on_time, total) VALUES
(1, 24, 25),
(2, 35, 36),
(3, 12, 15),
(4, 40, 40),
(5, 18, 20),
(6, 30, 32),
(7, 22, 25),
(8, 28, 30),
(9, 15, 18),
(10, 42, 45);

-- Debt data
USE debt_db;
INSERT INTO debt (user_id, used, credit_limit) VALUES
(1, 5000, 10000),
(2, 7500, 15000),
(3, 3000, 5000),
(4, 2000, 10000),
(5, 6000, 8000),
(6, 4000, 12000),
(7, 9000, 10000),
(8, 2500, 5000),
(9, 7000, 10000),
(10, 1000, 5000);

-- History data
USE history_db;
INSERT INTO history (user_id, account_age) VALUES
(1, 36),
(2, 48),
(3, 12),
(4, 60),
(5, 24),
(6, 42),
(7, 18),
(8, 30),
(9, 54),
(10, 72);

-- Credit mix data
USE mix_db;
INSERT INTO credit_mix (user_id, types_used, total_types) VALUES
(1, 3, 5),
(2, 2, 4),
(3, 1, 3),
(4, 4, 5),
(5, 2, 5),
(6, 3, 4),
(7, 1, 2),
(8, 2, 3),
(9, 3, 5),
(10, 4, 4);