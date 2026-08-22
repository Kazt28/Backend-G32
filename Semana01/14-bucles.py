# For plano (sin el uso de ninguna coleccion de datos)
# range(x, y, z)
# Si solo utilizamos un parametro
# x > TOPE, es decir hasta que numero va a incrementar menor que desde 0
# y > INICIO, es decir desde que numero va a empezar
# z > MODIFICADOR, es decir de cuanto en cuanto se va a incrementar/decrementar, su valor por defecto es 1

# for numero in range(10):
#     print(numero, end = ' ')

# for numero in range(5, 10):
#     print(numero, end = ' ')

# for numero in range(5, 10, 2):
#     print(numero, end = ' ')

# Todas las colecciones de datos son iterables

numeros = [10, 15, 7, 20, 13, 9]

for x in numeros:
    print(x, end=", ")
