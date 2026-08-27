# edad = int(input("Que edad tienes? "))


# if edad >= 18:
#     print("Puedes ingresar a la pagina")
# # Tambien se puede agregar un esceneario en el cual no se cumpla la condicion
# else:
#     print("No puedes ingresar")

# # Lo que se coloca fuera del bloque de identacion siempre se va a ejecutar.
# print("Gracias por usar el programa")

# edad_input = int(input("Ingresa tu numero: "))

# if edad_input >= 0:
#     print("Es positivo")
# else:
#     print("No es positivo")
    
# ventas = float(input("Cuanto vendiste?: \n"))

# if ventas >= 100:
#     descuento = ventas * 0.10
#     desc_ventas = ventas - descuento
#     print(desc_ventas)
# else:
#     print(ventas)

# # Operador Ternario 
# # Se usa si en el IF, ELSE, solo vamos a tener una sola linea de codigo
# # variable = RESULTADO_SI_ES_VERDADERA if CONDICION else RESULTADO_SI_NO_ES_VERDADERA

# monto_a_pagar = ventas * 0.9 if ventas >= 100 else ventas
# print(f"El monto a pagar es: {monto_a_pagar}")

# numero = 5

# impar_par = "par" if numero %2 == 0 else "No es par"
# print(f"El numero es: {impar_par}")

# notas = float(input("Que notas obtuviste: "))

# if notas >= 90:
#     print("")
    
    
numero1 = int(input("Ingrese primer numero: "))
numero2 = int(input("Ingrese segundo numero: "))

pedir_operacion = input("Que operacion deseas realizar? escribe el simbolo '+', '-', '*', '/': ").lower()

if pedir_operacion == "+":
    resultado = numero1 + numero2
    print(resultado)
elif pedir_operacion == "-":
    resultado = numero1 - numero2
    print(resultado)
elif pedir_operacion == "*":
    resultado = numero1 * numero2
    print(resultado)
elif pedir_operacion == "/":
    resultado = numero1 / numero2
    print(resultado)
else:
    print("INCORRECTO")