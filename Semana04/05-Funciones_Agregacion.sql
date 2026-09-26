-- Funciones de agregacion
-- Aggregate Functions sirve para poder tener un poco de logica en nuestras consultas

-- GROUP BY

SELECT categoria FROM productos GROUP BY categoria;

-- COUNT > CONTAR

SELECT activo, COUNT(activo) FROM productos GROUP BY activo;

-- SUM > SUMAR

SELECT SUM(stock) FROM productos;

SELECT categoria, SUM(stock) FROM productos WHERE activo = True GROUP BY categoria;

-- AVG > Calcular promedio

SELECT categoria, AVG(precio) FROM productos GROUP BY categoria;

-- MIN / MAX 

SELECT categoria, MAX(precio) FROM productos WHERE activo = TRUE GROUP BY categoria;

-- Si queremos usar una funcion de agregacion para condicionales entonces usamos la clausula having

SELECT categoria, SUM(stock) FROM productos WHERE activo = True GROUP BY categoria HAVING SUM(stock) >= 40 ORDER BY SUM(stock) DESC, categoria DESC;

-- En bd relaciones existen 3 tipos de relaciones entre tablas
-- 1 - 1
-- Es una relacion en la cual dos tablas tendran un registro que represente a la otran en un solo registro
-- Usuario tiene una perona
-- La clave foranea > Es la representacion del registro (pk) de la tabla A hacia la tabla B

-- La clave foranea (FK) no importa en cual de las dos tabla vaya 

-- 1 - n
-- Una persona tiene varias direcciones
-- La FK van en la tabla "varias", en este escenario la FK iria en la tabla de direcciones. Porque asi se
-- representa que ese registro le pertenece a una persona determinada

-- n - m
-- Alumno tiene varios cursos
-- Curso tiene varios alumnos
-- Al tener una relacion de muchos a muchos la FK no puede existir en alguna de las tablas y por ende se crea
-- una tabla Intermedia, Pivote, Puente en la cual en esa tablan iran las FK de las dos tablas (fk_alumno, fk_curso)