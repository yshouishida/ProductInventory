CREATE DATABASE IF NOT EXISTS dbstore;

USE dbstore;

CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_code VARCHAR(20) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    qty INT NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

INSERT INTO products
(product_code, product_name, description, qty, price)
VALUES
('P001', 'Wireless Mouse', '2.4GHz Wireless Mouse', 25, 450.00),
('P002', 'USB Keyboard', 'Standard USB Keyboard', 15, 650.00),
('P003', 'USB Cable', 'Type-C USB Cable', 30, 150.00),
('P004', 'Flash Drive', '64GB USB Flash Drive', 20, 350.00),
('P005', 'Webcam', 'HD USB Webcam', 10, 850.00);