-- Create a new database named 'my_database'
CREATE DATABASE my_database;

-- Switch to the newly created database
USE my_database;

-- Create a new table named 'users'
CREATE TABLE users (
    -- 'id' column: an integer that auto-increments and serves as the primary key
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- 'username' column: a variable character string with a maximum length of 50, cannot be null
    username VARCHAR(50) NOT NULL,
    
    -- 'email' column: a variable character string with a maximum length of 100, cannot be null
    email VARCHAR(100) NOT NULL,
    
    -- 'created_at' column: a timestamp that defaults to the current time when a new row is created
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert a sample user into the 'users' table
INSERT INTO users (username, email) VALUES ('john_doe', 'john@example.com');

-- Select all columns from the 'users' table to verify the insertion
SELECT * FROM users;