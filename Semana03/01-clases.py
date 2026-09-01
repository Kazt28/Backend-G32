# Persona

class persona:
    nombre = ""
    edad = 0

# Instancia > crea una copia completa de toda la clase
# Al momento de crear una instancia TODOS lOS ATRIBUTOS Y METODOS van a ser propios de la variable

p1 = persona()
p2 = persona()

# Como se puede acceder a los atributos de la clase
p1.nombre = "Eduardo"

p2.nombre = "Ana"
# Al editar un atributo de la instancia solamente se va a modificar en esa instancia y no en las otras

# print(p1.nombre)
# print(p2.nombre)

class Gato:
    # Cuando creamos una funcion dentro de una clase, esta se pasa a llamar metodo (porque solo va a funcionar dentro de la clase)
    # En python el primer parametro SIEMPRE el primer parametro de un metodo es SELF (asi mismo), sirve para indicar que los cambios
    # que hagamos se realicen en la misma instancia de la clase
    sexo = "Masculino"
    def __init__(self, nombre, raza, peso):
        self.nombre = nombre
        self.raza = raza
        self.peso = peso
        # las variables que yo cree dentro de __main__  seran creados como atributos de clase
        # y podran ser usados en todos sus metodos
g1 = Gato("Michi", "Persa", 2.5)

print(g1.nombre)

print(g1.sexo)