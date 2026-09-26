-- En el archivo SQL solo se ejecutaran las lineas que no empiecen con --
-- Asi mismo en SQL SIEMPRE se debe terminar la instruccion con ;
-- Cuando en la terminal aparece un '=' luego de el nombre de usuario del servidor
-- esto significa que esta esperando una nueva consulta

-- Cuando aparecer '-' significa que ya hemos empezado una consulta y esta esperando o mas
-- o mas indicaciones o la finalizacion

-- Cuando aparece una `'` significa que he abierto una pero aun no la he cerrado

-- En SQL NO ES LO MISMO, comilla simple que comilla doble, la comilla simple se usa para texto
-- es decir para mostrar o almacenar texto mientras que la comilla Doble se usa para llamar el 
-- nombre de tablas, columnas y nombres reservados.

-- Tenemos dos subconjuntos de Lenguaje
-- DDL : Data Definition Language (Lenguaje de definicion de datos)
-- CREATE: Crear Entidades (Bases de datos, Tablas, Usuarios, Columnas, trigger)
-- Alter : Alterar (modifica), tablas, bases de datos, Usuarios, etc
-- DROP : Eliminar entidades (tabla, bd, etc)
-- TRUNCATE : Elimina la data dentro de la tabla sin elimnar la tabla
-- RENAME : Cambiar el nombre de las entidades

CREATE DATABASE pruebas;

-- Cuando usamos un comando de psql no estamos obligados a poner ; es opcional

\c pruebas -- Para acceder a la DB pruebas

-- Sirve para ejecutar cualquier comando de la terminal fuera
-- Limpiaremos la terminal

\! Clear -- Para limpiar la terminal

CREATE TABLE personas (
    -- Ahora definimos las columnas
    -- nombre_columna tipo_de_dato opciones_adicionales
    id SERIAL PRIMARY KEY,  -- Solamente puede existe una columna SERIAL en toda la tabla
    -- UNIQUE > Indica que un registro no pueda tener el mismo valor de otro registro en esa columna
    -- NOT NULL > Indica que la columna jamas podra tener valores nulos
    -- NULL > Si podra tener valores nulos (config por defecto)
    -- PRIMARY KEY > Indica que la columna sera escogida como representacion del registro y se usara para encontrar el registro mas rapido, aca generalmente suelen ser los ID's
    -- DEFAULT valor > Indica que al momento de registrar o actualizar el valor de la columna si no se ingresa nada se podra el valor como valor predeterminada 
    nombre TEXT NOT NULL, -- TEXT No tiene limites, es decir podemos almacenar grandes cantidades de texto y este variara su almacenamiento en base al texto almacenado
    apellido VARCHAR(50),
    correo TEXT NOT NULL UNIQUE,
    fecha_nacimiento TIMESTAMP WITH TIME ZONE
);

-- Para ver las tablas creadas en las BD
\dt -- Se usa este comando

-- para ver las tablas y sus secuenciales (autoincrementales)
\d

-- nos mostrara la definicion de toda la configuracion de esa tabla
\d "nombre de la tabla"
