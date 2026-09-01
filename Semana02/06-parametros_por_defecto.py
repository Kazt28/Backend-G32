# si al crear una funcion le colocamos su valor al parametro, entonces si al momento
# de llamar a la funcion no se le da el parametro, usara el valor por defecto

def saludar(saludo="buenas noches"):
    print(saludo)

saludar()
saludar("holis")
saludar(saludo="Aloha")

# Nota: Si queremos utilizar parametros y parametros con valor predeterminado, los parametros
# con valores predeterminados van al final

def registrar_alumno(nombre, curso='backend'):
    print(f"el alumno {nombre} fue registrado al curso de {curso}")
    
# registrar_alumno("Manuel")
# registrar_alumno("Martita", "frontend")


def calcular_descuento(precio, porcentaje = 10):
    desc_precio = precio * (porcentaje / 100)
    return desc_precio

print(f"el descuento es de : {calcular_descuento(200, 50)}")
print(f"el descuento es de : {calcular_descuento(200)}")