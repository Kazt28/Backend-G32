def saludar():
    print("Hola Soy una Funcion")

# saludar()

def calcular_promedio():
    pass # pass no hace absolutamente nada y una vez que se coloque codigo se retira,
    # Se utiliza cuando no se sabe que va dentro de la funcion
    
def obtener_tipo_de_cambio():
    dolar = 3.31
    dolar_venta = 3.48
    return {"dolar_compra": dolar, "dolar_venta": dolar_venta}

resultado = obtener_tipo_de_cambio()
# print(resultado)


# Podemos parametros sin indicar el tipo de dato.
# En las ultimas versiones se puede indicar el tipo pero no es restringido

def saludo_personalizado(nombre):
    """Funcion que sirve para devolver un saludo en base al nombre"""
    #Documentacion de las funciones
    return f"Bienvenido {nombre}"

# print(saludo_personalizado(nombre="Manuel"))

def presentacion(nombre, edad, ciudad):
    return f"Hola me llamo {nombre}, tengo {edad} años y soy de {ciudad}"

# print(presentacion(nombre="Manuel", edad=39, ciudad="Lima"))

def sumar(num1, num2):
    
    return num1 + num2

resultado = sumar(10, 5)
# print(resultado)

#ejercicios

# 1. Crear una funcion calcular_area_rectangulo(base, altura) e imprima el resultado (base x altura)

def calcular_area_rectangulo(base, altura):
    resultado = base * altura
    return resultado

# print(f"La base del rectangulo es: {calcular_area_rectangulo(base=20, altura=34)}")

# 2. Crear una funcion es_par(numero) y que retorne si es par o impar (usando el %)

def es_par(numero):
    if numero % 2 == 0:
        return "Es par"
    return "No es par"


# print(f"El numero es: {es_par(3)}")

# 3. Dado una lista de diccionarios de productos crear una funcion mostrar_info(producto) 
# y que retorne el string "Hay {stock} unidades del producto {nombre}"

productos = [
    {
        "nombre":"Tomatodo 500ml", 
        "stock": 20
    }, 
    {
        "nombre":"Ventilador", 
        "stock": 50
    }, 
    {
        "nombre":"Parlante Bluetooth", 
        "stock": 25
    }, 
    {
        "nombre":"Cafe en grano 500gr", 
        "stock": 100
    }]
 
def mostrar_info(producto):  
        return f"Hay {producto.get("stock")} unidades del producto {producto.get("nombre")}"

for producto in productos:
    print(mostrar_info(producto = producto))