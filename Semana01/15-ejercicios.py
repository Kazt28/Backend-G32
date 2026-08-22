# 1.  Dado la lista numeros = [4, 8, 15, 16, 23, 42] Usando un For calcula la suma total

numeros = [4, 8, 15, 16, 23, 42]
sum_num = 0

for n in numeros:
    sum_num += n

print(f"The total is {sum_num}")

# 2. Dado la lista de nombres = ["Joshua", "Judith", "Eduardo","Jean Pierre", "Luis"] 
# quiero convertir todos los nombres a mayuscula (.upper())

nombres = ["Joshua", "Judith", "Eduardo","Jean Pierre", "Luis"]

for name in nombres:
    cap_name = name.upper()
    print(cap_name, end = ", ")

# 3. Dado la lista de precios = [10.5, 14.8, 17.2, 19.45] Calcular el promedio 
# y la cantidad de elementos de la lista

precios = [10.5, 14.8, 17.2, 19.45]

for p in precios:
    average = sum(precios) / len(precios)
print(average)

# 4. Tengo la siguiente lista de tuplas estudiantes = [("Juana", 26), ("David", 30), ("Ronaldo",18), ("Fatima", 23)] 
# usando un for desempaquete la tupla e imprime usando el formato "NOMBRE tiene EDAD años"

estudiantes = [("Juana", 26), ("David", 30), ("Ronaldo",18), ("Fatima", 23)] 


for name, edad in estudiantes:
    print(f"{name} tiene {edad} años")

# 5. Tengo el diccionario >>>>>> Ver lineas abajo
# Necesito saber cuantos pros tengo y cuantos contras tengo, 
# asi mismo quiero saber que paise_procedencia es y cual es el ultimo contras

producto = {
    "nombre":"Tarjeta Grafica",
    "precio":3020.52,
    "especificaciones":"Tarjeta grafica de ultima generacion",
    "pros":["Economica","Moderna","Sencilla instalacion"],
    "contras": ["No hay garantia", "Se sobrecalienta","No tiene drivers"],
    "info_adicional":{
        "pais_procedencia":"China",
        "estado":"Nuevo",
        "caja":False
    }
} 

print(f"La cantidad de contras son: {len(producto['contras'])} y la cantidad de pros son: {len(producto['pros'])}")
print(f"El pais de procedencia es {producto['info_adicional']['pais_procedencia']}")


# 6. Tengo una lista de tuplas ventas = [("enero", 1500), ("febrero", 2300), ("marzo",1800)] 
# recorrela en un for y construye un diccionario ventas_dic donde la clave sea el mes y el valor 
# sea el monto. Es decir, el resultado final debe ser 
# ventas_dic = {"enero":1500, "febrero":2300, "marzo":1800}

ventas = [("enero", 1500), ("febrero", 2300), ("marzo",1800)] 
ventas_dic = {}

for mes, monto in ventas:
    ventas_dic.update({mes:monto})

print(ventas_dic)












