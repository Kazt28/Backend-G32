# EJERCICIO 1
# Crea un programa en Python que:

# a) Solicite por teclado el precio de un producto (usar input()) y lo convierta a 
# numero decimal (float). b) Si el precio es mayor o igual a 50, aplique un descuento del 15%; 
# si no, no aplique descuento. c) Imprima el precio final usando f-strings, con 2 decimales. 
# Ejemplo de salida: "El precio final es: 42.50"

# Adicionalmente, dada la siguiente lista de precios: precios = [12.5, 8.9, 25.0, 3.75, 40.2]
# d) Usando un bucle for, calcula e imprime la suma total y el promedio de los precios 
# (el promedio con 2 decimales).

prod_price = float(input("Por favor ingrese el precio del producto: \n"))

if prod_price >= 50:
    desc_prod = prod_price - (prod_price * 0.15) 
else:
    desc_prod = prod_price

print(f"El precio final es: {desc_prod}")

precios = [12.5, 8.9, 25.0, 3.75, 40.2]
total = 0

for num in precios:
    total += num

avg_total = float(total / len(precios))

print(f"El total es: {total}")
print(f"El promedio es: {avg_total}")