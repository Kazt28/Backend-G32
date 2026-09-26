# EJERCICIO 2
# Dada la siguiente lista de diccionarios:

# productos = [ {"nombre": "Cuaderno", "precio": 4.5, "stock": 20}, {"nombre": "Lapicero", "precio": 1.2, "stock": 0}, {"nombre": "Mochila", "precio": 85.0, "stock": 5} ]

# a) Crea una funcion llamada mostrar_disponibilidad(productos) que recorra la lista con un for y, 
# por cada producto, imprima: - "PRODUCTO tiene stock disponible" si el stock es 
# mayor a 0 - "PRODUCTO no tiene stock" si el stock es igual a 0 
# (reemplaza PRODUCTO por el nombre real de cada producto)

# b) Crea una función llamada clasificar_nota(nota) que reciba una nota del 0 al 20 y 
# retorne (usando if-elif-else): - "Excelente" si la nota es entre 17 y 20 - 
# "Bueno" si la nota es entre 14 y 16 - "Regular" si la nota es entre 11 y 13 - 
# "Desaprobado" si la nota es menor a 11 Prueba la funcion con al menos 3 notas diferentes e 
# imprime los resultados.

productos = [ {"nombre": "Cuaderno", "precio": 4.5, "stock": 20}, 
              {"nombre": "Lapicero", "precio": 1.2, "stock": 0}, 
              {"nombre": "Mochila", "precio": 85.0, "stock": 5} ]


def mostrar_disponibilidad(productos):
    for producto in productos:
        if producto["stock"] > 0:
            print(f"{producto["nombre"]} tiene stock disponible")
        else:
            print(f"{producto["nombre"]} no tiene stock")

mostrar_disponibilidad(productos)

def clasificar_nota(nota):
    if nota >= 17 and nota <= 20:
        print(f"Excelente")
    elif nota >= 14 and nota <= 16:
        print(f"Bueno")
    elif nota >= 11 and nota <= 13:
        print(f"Regular")
    elif nota < 11:
        print("Desaprobado")

clasificar_nota(18)
clasificar_nota(15)
clasificar_nota(12)
clasificar_nota(6)