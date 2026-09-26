from flask import Flask, request
from werkzeug.exceptions import UnsupportedMediaType
from psycopg import connect
# from dotenv import load_dotenv
from psycopg.rows import dict_row
from flask_cors import CORS

# load_dotenv()
# postgresSQL: //NOMBRE_USUARIO: PASSWORD_USUARIO@HOST:PUERTO/NOMBRE_BD
credenciales = "postgresql://postgres:@127.0.0.1:5432/flask_db"
conexion = connect(conninfo=credenciales)
# Request nos dara informacion del cliente

# __name__ Es una variable global que sirve para indicar si el archivo en el cual nos encontramos
# se esta ejecutando directamente en la terminal
# app.py >  El valor de esta variable sera __main__
# python_01.py > y dentro de este archivo mando a llamar a app.py entonces el valor de __name__
# sera secondary y por ende no sera el archivo principal del proyecto.

# Flask se utiliza el patron de diseño de Singleton
app = Flask(__name__)

CORS(app, origins=['http://127.0.0.1:5500', 'http://localhost:5500', 'http://localhost:3000', 'http://127.0.0.1:3000'], methods=['GET','POST','PUT','DELETE'])

productos = [
    {
        "id": 1, 
        "nombre":"Vaso de vidrio"
    }, 
    {
        "id":2, 
        "nombre":"Parlante"
    },
    {
        "id":3,
        "nombre":"Botella de agua"
    }]

# Cada ruta(endpoint) Punto final (punto de acceso)
@app.route('/estado')
def estado_servidor():
    # Es de suma importancia que siempre en los endpoints retomemos algo
    return "El servidor esta vivo"

# Si no se declara el parametro methods, su valor por defecto sera 'GET'
@app.route('/productos', methods = ['GET', 'POST'])
def gestionar_productos():
    print(request.method)
    if request.method == "GET":       
    # Los controladores (es la logica del endpoint) suelen retornar diccionarios que estos sera interpretados en JSONS
    # o tambien se suelen retornar listas(arreglos)
        # Encargado de iniciar la comunicacion con la DB
        cursor = conexion.cursor()
        # Ejecutamos el comando en la DB
        cursor.execute("SELECT * FROM productos")
        
        # PARA obtener el resultado (si es necesario) usamos los metodos fetchone, fetchall, fetchmany
        productos_bd = cursor.fetchall()
        
        print(productos_bd)
        cursor.close()
        
        resultados = []
        
        for producto in productos_bd:
            resultados.append({
                "id": producto[0],
                "nombre": producto[1],
                "precio": float(producto[2]) if producto[2] else None,
                "cantidad": producto[3]
            })
              
        return {
            "message": "Los productos son:",
            "content": resultados
        }
    elif request.method == "POST":
        # Se usa para crear nueva informacion proveniente del frontend
        print(request.get_data())
        try:
            data = request.get_json()
            
            cursor = conexion.cursor()
            
            # En los strings comunes podemos usar %f para flotantes y adicionalmente el %i para convertir a enteros y asi
            # podemos evitar ataques directos y asi podemos evitar ataques directos a la base de datos (SQL INYECTION)
            # Si queremos retornar la informacion que acabamos de grabar en la base de datos se puede utilizar el comando
            # Returning columnas, es decir, si ponemos INSERT INTO ... VALUES ... RETURNING * esto devolvera toda la informacion
            # agregada a la BD
            cursor.execute("INSERT INTO productos (nombre, precio, cantidad) VALUES (%s, %s, %s) RETURNING *", (
                data.get("nombre"),
                data.get("precio"),
                data.get("cantidad")))
            
            # Para conservar la data y asegurarnos de que se guarde la informacion de manera permanente en la BD
            conexion.commit()
            
            # Para obtener el nuevo producto creado
            nuevo_producto = cursor.fetchone()
            
            print(nuevo_producto)
            cursor.close()
            
            return {
            "message": "Producto Creado Exitosamente"
             }                       
            
        except UnsupportedMediaType:
            return {
                "message": "Debes enviar informacion en formato JSON"
                # Handler (manejador de errores)
        }
  
# En el endpoint cuando se coloca <Variable> significa que esa parte recibira un valor diferente y ese valor se almacenara
# en la variable de ese nombre   
@app.route('/producto/<id>', methods = ['GET', 'PUT', 'DELETE'])
def gestionar_producto_por_id(id):
    if request.method == 'GET':
        cursor = conexion.cursor(row_factory=dict_row)
        cursor.execute("SELECT * FROM productos WHERE id = %s",(id,))

        resultado = cursor.fetchone()

        print(resultado)

        cursor.close()

        # Si el producto no existe retornar un mensaje que el producto no existe, caso contrario mostrar el mensaje ok
        if not resultado:
            return {
                "message":"Producto no encontrado"
            }, 404 # Not found (no encontrado)

        # En mssql-python (SQL SERVER) ya viene implementada la funcion de diccionario, es decir al ingresar al resultado puedo acceder como si fueran atributos como por ejemplo resultado.get("id")

        return {
            "content": resultado
        }

    elif request.method == 'PUT':
        # cuando tenemos un error en unuestra operacion y hacemos un commit se queda "pegado" y no permite realizar otra operacion ya que esta bloqueado, entonces para liberar esa operacion y dejarla sin efecto usamos el rollback para deshacer todos los cambios y si no hay ningun error no tendra efecto este comando pero tampoco lanzara error
        conexion.rollback()

        cursor = conexion.cursor(row_factory=dict_row)
        cursor.execute("SELECT id FROM productos WHERE id = %s", (id,))

        producto_existente = cursor.fetchone()

        if not producto_existente:
            return {
                "message": "Producto a actualizar no existe"
            },404

        # Ahora obtenemos la data proveniente del body
        data = request.get_json()

        # EL UPDATE SIEMPRE DEBE TENER UN WHERE
        cursor.execute("UPDATE productos SET nombre = %s, precio= %s, cantidad = %s WHERE id = %s RETURNING *",(
            data.get("nombre"),
            data.get("precio"),
            data.get("cantidad"),
            id
        ))

        # En MSSQL primero obtenemos la data y luego hacemos commit sino nos retornara data nula

        # Guardamos los cambios en la base de datos de manera permanente
        conexion.commit()

        # Obtenemos la info actualizada
        producto_actualizado = cursor.fetchone()

        cursor.close()

        return {
            "message":"Producto actualizado exitosamente",
            "content": producto_actualizado 
        }

    elif request.method =='DELETE':
        conexion.rollback()
        cursor = conexion.cursor(row_factory=dict_row)

        cursor.execute("SELECT id FROM productos WHERE id = %s", (id,))
        producto_existente = cursor.fetchone()

        if not producto_existente:
            return {
                "message":"Producto no encontrado"
            }, 404

        cursor.execute("DELETE FROM productos WHERE id = %s", (id,))

        conexion.commit()

        return {
            "message": "Producto eliminado"
        }


# QUERY PARAMS
# parametros enviados por la URL en el cual el cliente pone el nombre de parametro y su valor, esto generalmente se usa para metodos GET porque en los GET JAMAS se envia BODY
@app.route('/buscar-producto')
def buscar_producto():
    print(request.args)

    return {
        "content": []
    }



# ESTO SIEMPRE VA AL FINAL!!!!!
if __name__ == "__main__":
    # el metodo run ejecuta el servidor y lo mantiene escuchando peticiones
    # debug significa que con cada cambio que guardemos los archivos automaticamente se reiniciara el servidor
    app.run(port=5000, debug=True)