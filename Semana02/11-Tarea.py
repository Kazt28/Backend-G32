
# BONUS!
# 8. Crear una funcion con while True que pida numeros al usuario y los sume manejando un try-except en el que caso que se ingrese un texto en vez de numeros y que al escribir Salir, termine la sumatoria sin lanzar el error


# RESOLUCION DE EJERCICIOS

# 1. Crea una funcion calcular_igv en la cual pide el precio y retorne el precio final 
# aplicado el igv (18%) - puede utilizar lambda

def calcular_igv(precio):
    igv = 18 / 100
    precio_mas_igv = precio + (precio * igv)
    return precio_mas_igv

print(round(calcular_igv(100)))

# 2. Convierte la temperatura en la funcion cambiar_temperatura de Celcius a Farenheit
# - puede utilizar lambda

def cambiar_temperatura(temp):
    conv_temp = (temp * 1.8) + 32
    return conv_temp

print(round(cambiar_temperatura(20)))

# 3. Dado un diccionario de un producto (nombre, precio, stock) utiliza if-elif-else para clasificar el stock en "Sin Stock" 
# (si el stock es 0), "Stock Bajo" (si el stock es entre 1 y 10) y "Disponible"(si el stock es mas que 10)

stock_almacen = {
    "nombre" : "rodajes",
    "precio" : 20,
    "stock" : 25  
}

def materiales(disp_stock):
    if disp_stock <= 0:
        return "Sin stock"
    elif disp_stock >= 1 and stock_almacen["stock"] <= 10:
        return "Stock Bajo"
    elif disp_stock > 10:
        return "Disponible"

print(materiales(stock_almacen["stock"]))

# 4. Usando un while, simula un cajero automatico simple que pida una clave hasta que el usuario 
# la ingrese correctamente, usando 3 intentos como maximo, sino indica que la cuenta fue bloqueada.

def cajero_automatico(clave):
    count = 0
    
    while count != 3:
        login = input("Ingresa contraseña: ")        
        if login != clave:
            count +=1
            print("Contraseña incorrecta, vuelve a ingresar")
        elif clave == login:
            return "Password correcto, puedes ingresar"
    if count == 3:
        return "muchos intentos fallidos, cuenta bloqueada"
    
print(cajero_automatico("Eureka"))       

# 5. Crear una funcion calcular_area_circulo(radio) que retorne el area (3.1415 como valor de pi) - puede utilizar lambda

def calcular_area_circulo(radio):
    pi = 3.1415
    area_rad = pi * (radio ** 2)
    return area_rad
print(f"El area del circulo es: {(calcular_area_circulo(20)):.4f}")


# 6. Crear una funcion procesar_notas(nombre, *notas) que calcule y retorne el promedio y
# luego clasifique el resultado con if-elif-else en una segunda funcion clasificar(promedio)

def clasificar(promedio):
    if promedio > 15:
        return "Excelente"
    elif promedio > 10 and promedio <= 15:
        return "Aprobado"
    else:
        return "Desaprobado"

def procesar_notas(nombre, *notas):
    promedio = sum(notas)  / len(notas)
    situacion = clasificar(promedio)
    return f"{nombre} obtuvo un promedio de: {promedio}, su status es {situacion} "


print(procesar_notas("Jose", 20, 20, 15, 4, 18)) 

# 7. En una lista de 5 elementos crear una funcion obtener_por_indice(lista, indice)
# que capture el error IndexError si el indice no existe


ingredientes = ["harina", "huevo", "azucar", "leche", "sal"]

def obtener_por_indice(lista, indice):
    try:
        print(lista[indice])
    except IndexError:
        print("El indice que buscas esta fuera de rango de la lista")

obtener_por_indice(ingredientes, 6)


