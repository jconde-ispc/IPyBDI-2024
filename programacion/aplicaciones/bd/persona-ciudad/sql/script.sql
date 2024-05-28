-- Crear tabla Ciudad
CREATE TABLE Ciudad (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    provincia VARCHAR(255) NOT NULL,
    codigo_postal VARCHAR(10) NOT NULL
);

-- Crear tabla Persona
CREATE TABLE Persona (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    dni VARCHAR(10) NOT NULL,
    email VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE,
    telefono VARCHAR(15),
    ciudad_id INT,
    FOREIGN KEY (ciudad_id) REFERENCES Ciudad(id)
);


-- Insertar ciudades
INSERT INTO Ciudad (nombre, provincia, codigo_postal) VALUES
    ('Ciudad A', 'Provincia X', '12345'),
    ('Ciudad B', 'Provincia Y', '67890');

-- Insertar personas
INSERT INTO Persona (nombre, apellido, dni, email, fecha_nacimiento, telefono, ciudad_id) VALUES
    ('Juan', 'Perez', '12345678A', 'juan@example.com', '1990-05-15', '555-123-456', 1),
    ('Maria', 'Lopez', '98765432B', 'maria@example.com', '1985-09-20', '555-789-123', 2);
