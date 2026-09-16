CREATE DATABASE IF NOT EXISTS dbstore;

USE dbstore;

CREATE TABLE IF NOT EXISTS tblProducts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(20) NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    qty INT NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS tblUsers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'user'
);

INSERT INTO tblProducts
(code, name, description, qty, price)
VALUES
('P001', 'Wireless Mouse', '2.4GHz Wireless Mouse', 25, 450.00),
('P002', 'USB Keyboard', 'Standard USB Keyboard', 15, 650.00),
('P003', 'USB Cable', 'Type-C USB Cable', 30, 150.00),
('P004', 'Flash Drive', '64GB USB Flash Drive', 20, 350.00),
('P005', 'Webcam', 'HD USB Webcam', 10, 850.00);
