# secreto = 10

# ad_bool = True

# while ad_bool:
#     ad_numero = int(input("Adivina un numero entre el 1 y el 20: "))
#     if ad_numero == secreto:
#         print("adivinaste")
#         ad_bool = False
#     else:
#         print("Sigue intentando")


lista_precios = []

while len(lista_precios) < 5:
    nuevo_precio = int(input("Ingresa un precio: "))
    if nuevo_precio <= 0:
        continue
    lista_precios.append(nuevo_precio)
print(lista_precios)
    