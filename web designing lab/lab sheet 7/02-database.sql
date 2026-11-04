CREATE DATABASE bookstore;
USE bookstore;
CREATE TABLE users (
 id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(120) UNIQUE,
 password VARCHAR(255) NOT NULL, role ENUM('customer','admin') DEFAULT 'customer'
);
CREATE TABLE books (
 id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(180) NOT NULL,
 author VARCHAR(120), category VARCHAR(80), price DECIMAL(10,2) NOT NULL,
 stock INT DEFAULT 0, image VARCHAR(255)
);
CREATE TABLE orders (
 id INT AUTO_INCREMENT PRIMARY KEY, user_id INT NOT NULL,
 shipping_address TEXT, total DECIMAL(10,2), status ENUM('Pending','Shipped','Delivered') DEFAULT 'Pending',
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
 FOREIGN KEY(user_id) REFERENCES users(id)
);
CREATE TABLE order_items (
 id INT AUTO_INCREMENT PRIMARY KEY, order_id INT, book_id INT,
 quantity INT, price DECIMAL(10,2),
 FOREIGN KEY(order_id) REFERENCES orders(id), FOREIGN KEY(book_id) REFERENCES books(id)
);
CREATE TABLE reviews (
 id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, book_id INT,
 rating TINYINT, comment TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE wishlist (
 id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, book_id INT,
 UNIQUE(user_id, book_id)
);
INSERT INTO books(title,author,category,price,stock) VALUES
('Learn PHP','A. Kumar','Technology',350,10),
('Web Design Basics','R. Shah','Technology',250,8),
('Short Stories','M. Ali','Fiction',180,12);