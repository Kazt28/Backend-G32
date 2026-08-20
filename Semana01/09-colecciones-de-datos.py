# Listas (Arreglos)
# Coleccion de datos ordenadas y editables
frutas = ['manzana', 'pera', 'platano', 'kiwi']

# Ordenada(La posicion empieza desde el 0)
print(frutas[0])

# Se puede recorrer las listas tanto de izq a der como viceversa
print(frutas[-1])

# puedo sacar una sublista

print(frutas[1:3])

# Si no se le pone posicion inicial agarrara desde el comienzo

print(frutas[:3])

print(frutas[3:])

# Los metodos mas usados de las listas
# agregamos nuevos elementos al final de la lista

frutas.append("sandia")

# Inserta el elemento a la posicion deseada

frutas.insert(1, "mango")

# remove elimina el valor si lo encuentra

# frutas.remove(1)

# metodo pop elimina el contenido por su indice y devuelve el valor eliminado

eliminado = frutas.pop(5)

print(eliminado)

# Ordena alfabeticamente los elementos de la lista

frutas.sort()
print(frutas)

# Reverse invierte el orden actual

frutas.reverse()
print(frutas)

# Si queremos eliminar una lista
frutas.clear()
print(frutas)

# Len devuelve la cantidad de elementos que hay en una lista
longitud = len(frutas)
print(longitud)