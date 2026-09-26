-- DML DATA MANIPULATION LANGUAGE (Lenguaje de Manipulacion de Datos)
--  \c pruebas Para acceder a la base de datos pruebas

-- INSERT : Ingresar nuevos registros a una tabla
-- SELECT : Obtener la informacion de determinados registros de una o varias tablas
-- UPDATE : Actualizar informacion registrada
-- DELETE : Elimina de manera permanente los registros en base a condiciones

-- INSERT INTO nombre_tabla(nomb_col_1, nomb_col_2...) VALUES (val1, val2, val3.....)

INSERT INTO personas(id, nombre, apellido, correo, fecha_nacimiento)
VALUES      (DEFAULT, 'Juan', 'Perez', 'J.perez@gmail.com', '1984-06-12');

-- Si voy a insertar usando el orden de las columnas con el que 
--la cree puedo precindir del nombre de las columnas PERO si o si 
--tengo que declarar todas las columnas

INSERT INTO personas(id, nombre, apellido, correo, fecha_nacimiento)
VALUES      (DEFAULT, 'Martha', 'Escobedo', 'mescobedo@gmail.com', '2005-02-14'),
            (DEFAULT, 'Rodrigo','Jimenez', 'rjimenez@gmail.com', '1989-06-15'),
            (DEFAULT, 'Marge', 'Marquez', 'mmarquez@gmail.com', '2006-09-07');


-- DEFAULT > INDICAMOS EL VALOR POR DEFECTO DEFINIDO EN LA COLUMNA
-- En las columnas SERIAL agarra el valor por defecto definido en la columna
-- En SQL comillas simples para informacion de texto
-- Comillas dobles para nombres de tablas, columnas, etc.
-- En SQL se usa el ISO 8601, para las fechas en el cual el formato es yyyy-mm-dd HH-MM-SS-mmmm

SELECT nombre FROM personas;

SELECT * FROM personas;

SELECT * FROM personas WHERE id > 2;

SELECT * FROM personas WHERE id > 2 AND nombre = 'Rodrigo' OR nombre = 'Marge';

-- Los alias sirven para evitar poner el nombre completo de la tabla o relacion
SELECT p.id FROM personas AS p;

-- El AS es opcional
SELECT p.id FROM personas p;

-- Si se desea hacer una busqueda en una columna numerica por limites(Desde Hasta)
-- BETWEEEN AND
-- ESTO ES MEJOR QUE HACER UN AND
SELECT * FROM personas WHERE id BETWEEN 2 AND 4;

SELECT * FROM personas WHERE id >= 2 AND id


-- Si se quiere hacer la busqueda por unos determinados valores
-- IN
-- Esta busqueda no solo es para texto, es para numeros, fechas, y otros.
-- Esto seria interpretado como un OR
SELECT * FROM personas WHERE nombre IN ('Eduardo', 'Rodrigo');

-- Si deseo hacer una busqueda pero no me se el valor exacto LIKE
-- el % indica que es lo que viene despues, puede ser 'rodrigo', 'rodriguez' o quedar en 'rodri' PERO el like sigue siendo sensible a mayus y minus
SELECT * FROM personas WHERE nombre LIKE 'rodri%';
SELECT * FROM personas WHERE nombre ILIKE '%rodri%';

-- Si queremos obtener los resultados que tengan valores NULOS
-- IS > si es
-- IS NOT > no es
SELECT * FROM personas WHERE peso IS NULL;