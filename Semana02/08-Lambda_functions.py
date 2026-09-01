# En python tenemos la posibilidad de crear funciones de una sola linea y esta se
# conocen como funciones lambda

# Automaticamente retorna el resultado de la operacion

sumar = lambda num1, num2: num1 + num2 if num1 > 10 else num1 * num2

def sumar(num1, num2):
    if num1 > 10:
        return num1 + num2
    else:
        return num1 * num2

resultado = sumar(10, 20)
# print(resultado)

es_correo = lambda mail: "@" and "." in mail

print(es_correo("manuel@hotmai.com"))
 
# anidamiento de metodos        
generar_slug = lambda new_text: new_text.lower().replace(" ", "-") 

print(generar_slug("Bienvenidos a la clase"))
    