-- Skapa databas
CREATE DATABASE Inlamning_1;

-- Använd databas
USE Inlamning_1;

-- Skapa tabell
CREATE TABLE `users` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(100) NOT NULL,
    `password` VARCHAR(100) NOT NULL,
    `name` VARCHAR(250) NOT NULL,
    `email` VARCHAR(250) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE `username_unique` (`username`),
    UNIQUE `email_unique` (`email`)
);

-- Lägg till en testanvändare
INSERT INTO users (username, password, name, email)
VALUES ('testuser', 'testpass123', 'Test Användare', 'test@example.com');