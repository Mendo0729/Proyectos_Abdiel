CREATE DATABASE IF NOT EXISTS Contacto;

-- Usar la base de datos recién creada
USE Contacto;

-- Crear una tabla llamada 'contactos' con columnas básicas
CREATE TABLE contactos (
    id INT AUTO_INCREMENT PRIMARY KEY,   -- Identificador único para cada contacto
    nombre VARCHAR(100) NOT NULL,        -- Columna para el nombre del contacto
    telefono VARCHAR(15) NOT NULL,       -- Columna para el número de teléfono
    correo VARCHAR(100) NOT NULL         -- Columna para el correo electrónico
);