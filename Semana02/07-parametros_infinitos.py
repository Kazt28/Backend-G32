# en el caso que nosotros recibiesemos una cantidad indeterminada de parametros usamos el *args (arguments)
def promedio_notas(*notas):
    # el parametro * es una tupla que nunca la voy a poder editar
    print(notas)
    # quiero sacar el promedio de todas las notas
    promedio = sum(notas) / len(notas)
    return promedio

# al pasarle los parametros seran con ,
promedio_notas(15,20,6,12,8.5)
promedio_notas(15,20,8.5)
promedio_notas(13,10)

# se puede tambien combinar los parametros con los *args
# No se puede colocar otro parametro luego de los *args
# Para el tipado de una coleccion de datos si queremos indicar que todos los
# elementos van a ser int, entonces [int,...]
# Si queremos indicar que la tupla va a tener solo 2 Elementos y esos van a ser
# int y str, entonces [int, str]

def promedio_nota_alumno(nombre, *notas: tuple[int, ...]):
    print(nombre)
    print(notas)

promedio_nota_alumno("Eduardo", 10, 20, 5)

