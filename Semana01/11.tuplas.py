# Coleccion de datos que es ordenada pero no es codificable
# Una vez que se crea ya no se puede modificar

persona = ["Eduardo", 30, "Arequipa"]

print(persona[0])

# No se puede modificar el contenido de las posiciones
# Desempaquetar los datos variables independientes
nombre, edad, ciudad = persona
nombre = "Ramoncito"
edad = persona[1]

# Cuidado al crear las tuplas de un solo elemento

numeros = (1)
# Cuando yo creo una tupla de un solo elemento y este no tiene una coma al final,
# los parentesis representantes de la tupla no son considerados y al final se eliminan

# Para crear una tupla de un solo elemento
ages = (23, )
print(type(ages)) # TUPLA

