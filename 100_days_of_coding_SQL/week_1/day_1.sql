#!/usr/bin/sql

-- starting mysql
sudo service mysql start

-- creating database
CREATE DATABASE database_name;

-- creating a user
CREATE USER 'name'@'host' identified WITH mysql_native_password BY 'password';

-- creating table
CREATE TABLE categories( 
	id INT PRIMARY KEY AUTO_INCREMENT, 
	name VARCHAR(215) NOT NULL);

CREATE TABLE product( 
	id INT PRIMARY KEY AUTO_INCREMENT, 
	name VARCHAR(215) NOT NULL, 
	price DECIMAL(10, 2) DEFAULT 0.00, 
	category_id INT, 
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	FOREIGN KEY(category_id) REFERENCES categories(id));
