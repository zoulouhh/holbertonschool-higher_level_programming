-- create database usa if doesnt exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use database usa
USE hbtn_0d_usa;

-- create table states if doesnt exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);