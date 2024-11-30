create database libManagement
use libManagement
-- Drop existing tables to remove all data and definitions
DROP TABLE IF EXISTS Borrowed_Books;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Borrow;
DROP TABLE IF EXISTS Staff;
DROP TABLE IF EXISTS Author;
DROP TABLE IF EXISTS _Member;

-- Create Users table to store user credentials
CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    role ENUM('user', 'admin') DEFAULT 'user'
);

-- Create Books table to store book details
CREATE TABLE Books (
    isbn VARCHAR(20) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(100) NOT NULL,
    publication_date DATE,
    genre VARCHAR(50)
);

-- Create Borrowed_Books table to store records of borrowed books
CREATE TABLE Borrowed_Books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    isbn VARCHAR(20) NOT NULL,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (isbn) REFERENCES Books(isbn)
);
