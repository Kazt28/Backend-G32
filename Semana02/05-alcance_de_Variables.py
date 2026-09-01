# Scope (Alcance) Como puedo utilizar mis variables dentro de la funcion

def calcular():
    resultado = 100
    print(resultado)
# calcular()

# La variable resultado solo existe dentro de la funcion

# Las variables globales (no estan dentro de la funcion) si pueden ser leidas dentro de la funcion

nombre = "Manuel"

def mostrar():
    print(nombre)

# mostrar()

def incrementar():
    global contador
    contador += 1

# incrementar()
# incrementar()
# incrementar()

# print(contador)

# la forma correcta de evitar el uso de "global"
contador = 0

def incrementar_en_uno(valor):
    return valor + 1

contador = incrementar_en_uno(contador)
contador = incrementar_en_uno(contador)
contador = incrementar_en_uno(contador)
contador = incrementar_en_uno(contador)
print(contador)