-- EJERCICIO 5
-- Se tienen las siguientes tablas (relacion muchos a muchos, tal como se trabajo en clase con alumnos, cursos y la tabla puente alumnos_cursos):
-- CREATE TABLE alumnos ( id SERIAL PRIMARY KEY, nombre TEXT );
-- CREATE TABLE cursos ( id SERIAL PRIMARY KEY, nombre TEXT );
-- CREATE TABLE alumnoscursos ( alumnoid INT, cursoid INT, nota FLOAT, CONSTRAINT fkalumno FOREIGN KEY (alumnoid) REFERENCES alumnos(id), CONSTRAINT fkcurso FOREIGN KEY (cursoid) REFERENCES cursos(id), PRIMARY KEY (alumnoid, curso_id) );
-- Considera que puede haber alumnos que aun no se han matriculado en ningún curso, y cursos que todavía no tienen ningún alumno matriculado.

-- Escribe las siguientes consultas SQL:

-- a) Usando JOIN (INNER JOIN), muestra el nombre del alumno junto con el nombre del curso y la nota, solo para los alumnos que si estan matriculados en algun curso.
-- b) Usando LEFT JOIN, muestra el nombre de TODOS los alumnos junto con el nombre del curso en el que están matriculados (si un alumno no tiene curso, el nombre del curso debe aparecer como NULL).
-- c) Usando RIGHT JOIN, muestra el nombre de TODOS los cursos junto con el nombre de los alumnos matriculados en cada uno (si un curso no tiene alumnos, el nombre del alumno debe aparecer como NULL).
-- d) Usando el JOIN entre las 3 tablas, escribe una consulta que muestre, por cada curso, el promedio de las notas de los alumnos matriculados (usa AVG y GROUP BY sobre el nombre del curso).


CREATE TABLE alumnos (
    id SERIAL PRIMARY KEY,
    nombre TEXT
);

CREATE TABLE cursos (
    id SERIAL PRIMARY KEY,
    nombre TEXT
);


CREATE TABLE alumnos_cursos (
    alumno_id INT,
    curso_id INT,
    nota FLOAT,
    CONSTRAINT fk_alumno FOREIGN KEY (alumno_id) REFERENCES alumnos(id),
    CONSTRAINT fk_curso FOREIGN KEY (curso_id) REFERENCES cursos(id),
    PRIMARY KEY (alumno_id, curso_id)
);

INSERT INTO alumnos (nombre)
VALUES ('Amy Valentine'),
	   ('Rodolfo Rodriguez'),
	   ('Ricardo Mendoza'),
	   ('Teofilo Gutierrez'),
	   ('Carmen Perez'),
	   ('Valentina Colmenares');

INSERT INTO cursos (nombre)
VALUES ('Calculo'),
	   ('Estadistica'),
	   ('Microeconomia'),
	   ('Econometria'),
	   ('Macroeconomia'),
	   ('Finanzas Corporativas');

INSERT INTO alumnos_cursos (alumno_id, curso_id, nota)
VALUES (1, 1, 15.5),
	   (1, 2, 18.0),
	   (2, 1, 11.0),
	   (3, 4, 16.5),
	   (5, 3, 09.5),
	   (6, 6, 14.0);


-- a) Usando JOIN (INNER JOIN), muestra el nombre del alumno junto con el nombre del curso 
-- y la nota, solo para los alumnos que si estan matriculados en algun curso.

SELECT a.nombre AS alumno, c.nombre AS curso, ac.nota AS notas
FROM alumnos a INNER JOIN alumnos_cursos ac  ON a.id = ac.alumno_id
INNER JOIN cursos c ON ac.curso_id = c.id;

-- b) Usando LEFT JOIN, muestra el nombre de TODOS los alumnos junto con el nombre del 
-- curso en el que están matriculados (si un alumno no tiene curso, el nombre del curso 
-- debe aparecer como NULL).

SELECT a.nombre AS alumno, c.nombre AS curso FROM alumnos a 
LEFT JOIN alumnos_cursos ac ON a.id = ac.alumno_id
LEFT JOIN cursos c ON ac.curso_id = c.id;

-- c) Usando RIGHT JOIN, muestra el nombre de TODOS los cursos junto con el nombre de los
-- alumnos matriculados en cada uno (si un curso no tiene alumnos, el nombre del alumno 
-- debe aparecer como NULL).

SELECT c.nombre AS curso, a.nombre AS alumno FROM alumnos a
RIGHT JOIN alumnos_cursos ac ON a.id = ac.alumno_id
RIGHT JOIN cursos c ON ac.curso_id = c.id;

-- d) Usando el JOIN entre las 3 tablas, escribe una consulta que muestre, por cada curso, 
-- el promedio de las notas de los alumnos matriculados (usa AVG y GROUP BY sobre el nombre del curso).

SELECT c.nombre AS curso, AVG(ac.nota) AS promedio_nota FROM cursos c
INNER JOIN alumnos_cursos ac ON c.id = ac.curso_id
INNER JOIN alumnos a ON ac.alumno_id = a.id GROUP BY c.nombre;
