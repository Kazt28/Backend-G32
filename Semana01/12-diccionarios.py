# Coleccion de datos
# Ordenada(por llaves) y editable

alumno = {
    "nombre": "juan",
    "apellido": "zegarra",
    "curso": "python",
    "hobbies": ["nadar", "programar", "trabajar"],
    "edad": 35,
    "jubilado": False,
    "padres": {
        "nombre": "Alberto",
        "apellido": "Zegarra",
        
    },
    "madre":{
        "nombre": "Lucia",
        "apellido": "Hinojosa"
    }
}

print(alumno["hobbies"])
print(alumno["hobbies"][1])
print(alumno["padres"]["nombre"])

# print(alumno["nombre"])
# print(alumno.get("nombre", "No existe"))
# print(alumno.get("nacionalidad"))

# Retorna todas las llaves del diccionario
# print(alumno.keys())

# Retorna todos los valores del diccionario
# print(alumno.values())

# Para hacer asignaciones SI O SI usamos los corchetes y no el metodo GET, ese es solo para el obtener info
# alumno['nacionalidad'] = 'Boliviano'

