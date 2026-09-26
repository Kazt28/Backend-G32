-- Crear una base de datos tienda
-- Ingresar a la bd tienda
-- Crear una tabla llamada productos cuyas columnas son
-- id autoincrementable pk
-- nombre texto no nulo
-- categoria texto hasta 30 caracteres
-- precio float con 2 decimales
-- stock entero
-- activo BOOLEAN DEFAULT TRUE

-- Insertar los datos
INSERT INTO productos (nombre, categoria, precio, stock, activo)
VALUES
    ('Arroz Costeño 5kg', 'Abarrotes', 22.50, 40, TRUE),
    ('Fideos Don Vittorio', 'Abarrotes', 4.20, 0, TRUE),
    ('Coca Cola 1.5L', 'Bebidas', 6.50, 25, TRUE),
    ('Inca Kola 500ml', 'Bebidas', 3.00, 15, TRUE),
    ('Leche Gloria Evaporada', 'Lácteos', 4.80, 60, TRUE),
    ('Yogurt Gloria 1L', 'Lácteos', 8.90, 0, FALSE),
    ('Detergente Ariel 1kg', 'Limpieza', 15.90, 8, TRUE),
    ('Lejía Clorox 1L', 'Limpieza', 5.50, 30, TRUE),
    ('Atún Florida', 'Abarrotes', 6.90, 12, TRUE),
    ('Cerveza Cusqueña 620ml', 'Bebidas', 8.50, 0, FALSE);

-- Consultas
-- 1. Mostrar todos los productos con todas sus columnas
-- 2. Mostrar solo el nombre y precio
-- 3. Mostrar nombre y precio pero cambiar el nombre de la columna a nombre_producto y precio_soles
-- 4. Mostrar los productos cuya categoria sea 'Bebidas'
-- 5. Mostrar los productos cuyo precio sea mayor a 10.00
-- 6. Mostrar los productos cuyo stock sea 0
-- 7. Mostrar los productos cuyo precio sea entre 5 y 15 y cuyo nombre contenga la palabra Leche (sin sensible a mayus)
-- 8. Mostrar los productos cuya categoria no sea 'limpieza'
-- OPCIONAL
-- 9. Mostrar los productos que no esten activos

CREATE DATABASE tienda;
\c tienda

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre TEXT NO NULL,
    categoria VARCHAR(30) NOT NULL,
    precio NUMERIC(6, 2),
    stock INT,
    activo BOOLEAN DEFAULT TRUE
);

SELECT * FROM productos;
SELECT nombre AS nombre_producto, precio AS precio_soles FROM productos;
SELECT * FROM productos WHERE categoria in ('Bebidas');
SELECT * FROM productos WHERE precio > 10;
SELECT * FROM productos WHERE stock = 0;
SELECT * FROM productos WHERE nombre ILIKE 'Leche' AND precio BETWEEN 5 AND 15;
SELECT * FROM productos WHERE categoria NOT IN ('Limpieza');