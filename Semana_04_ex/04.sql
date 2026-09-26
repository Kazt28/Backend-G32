-- EJERCICIO 04
-- Usando como referencia la siguiente tabla trabajada en clase:
-- CREATE TABLE productos ( id SERIAL PRIMARY KEY, nombre TEXT NOT NULL, categoria VARCHAR(30), precio FLOAT, stock INT, activo BOOLEAN DEFAULT TRUE );
-- Escribe las siguientes sentencias SQL:
-- a) Inserta un producto llamado 'Cuaderno A4', categoria 'Utiles', precio 3.50, stock 100 y activo TRUE.
-- b) Muestra todos los productos cuyo precio sea mayor a 10 y que esten activos.
-- c) Muestra todos los productos cuyo nombre contenga la palabra "leche" (sin distinguir mayusculas de minusculas).
-- d) Escribe una consulta que muestre, por cada categoria, la suma total del stock (usa SUM y GROUP BY), mostrando solo las categorias cuya suma de stock sea mayor a 20 (usa HAVING).

SELECT nombre FROM productos;

INSERT INTO productos (nombre, categoria, precio, stock, activo)
VALUES	('Cuaderno A4', 'Utiles', 3.50, 100, TRUE);

SELECT * FROM productos WHERE precio > 10 AND activo = True;

SELECT * FROM productos WHERE nombre ILIKE '%leche%';

SELECT categoria, SUM(stock) FROM productos GROUP BY categoria HAVING SUM(stock) > 20;


