# 1. Ingresa por teclado el monto a pagar y que me imprima por consola 
# el monto de propina que debo de dar siendo el 10%

# monto_pago = float(input("Ingresa el monto a pagar: \n"))

# propina = (monto_pago * 10) / 100

# print(f"La propina es: % {propina}")

# 2. Dado un total de segundos (3746), Calcula cuentas horas, minutos 
# y segundos representan usando los operadores aritmeticos // y %

segundos = 3746

minutos = segundos // 60
print(minutos)
horas = minutos // 60
print(horas)
segundoss = segundos % 60
print(segundoss)

# 3. Ingresa un numero y quiero que me diga si es PAR o IMPAR (use el operador aritmetico %)

numero_desc = float(input("Ingresa tu numero: \n"))

impar_par = numero_desc % 2

print(f"Tu numero {numero_desc} es {impar_par}")

# 4. Ingresa un monto por teclado y luego haga lo siguiente: 1. aumente 250, 
# luego retire 400 y luego genere un cobro de interes del 5% (multiplicar por 1.05)

# monto = float(input("Ingresa el monto: \n"))

# nuevo_monto = ((monto + 250) - 400) * 1.05

# print(nuevo_monto)