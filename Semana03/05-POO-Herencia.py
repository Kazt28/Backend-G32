class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    
    
    def mostrar_info(self):
        print(f"{self.nombre} gana {self.sueldo}")

# Heredo mi clase
class EmpleadoVentas(Empleado):
    pass

# Al heredar de una clase jalaremos toda su configuracion (metodos y atributos publicos y protegidos)
vendedor = EmpleadoVentas("Roxana", 2000)
# vendedor.mostrar_info()

# Clase padre / superclase > La clase origina (empleado)
# Clase hija / subclase > La clase que hereda (EmpleadoVentas)
# Herencia > La hija obtiene automaticamente atributos y metodos del padre

class EmpleadoMKT(Empleado):
    def __init__(self, nombre, sueldo, comision):
        super().__init__(nombre, sueldo)
        self.comision = comision

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} esta comiendo :p")
    
    def dormir(self):
        print(f"{self.nombre} esta durmiendo zzzz")

class Gato(Animal):
    def __init__(self, nombre, edad):
        self.edad = edad
        super().__init__(nombre)
    
    def araniar(self):
        print(f'{self.nombre} esta arañando')

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def ladrar(self):
        print(f"{self.nombre} esta ladrando")

    def comer(self):
        print(f"{self.nombre} esta comiendo")

g = Gato("Michi", "15 meses")
p = Perro("Firulais")

# g.comer()

class Figura:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def metodo_area(self):
        return 0

class Cuadrado(Figura):
    
    def __init__(self, nombre, lado):
        self.lado = lado
        super().__init__(nombre)
    
    def metodo_area(self):
        return self.lado ** 2
    
class Triangulo(Figura):
    
    def __init__(self, nombre, base, altura):
        self.base = base
        self.altura = altura
        super().__init__(nombre)
        
    def metodo_area(self):
        return (self.base * self.altura) / 2
    
fig1 = Triangulo("Rectangulo", 3, 40)
# print(fig1.metodo_area())


class Persona:
    def __init__(self, nombre, vida=100):
        self.nombre = nombre
        self.vida = vida
    
    def recibir_danio(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            self.vida = 0
            return f"{self.nombre} recibió {cantidad} de daño. ¡Ya se murió!"
        
        # Siempre retornamos un mensaje para evitar el "None" al imprimir
        return f"{self.nombre} recibió {cantidad} de daño. Vida restante: {self.vida}"

class Guerrero(Persona):
    def __init__(self, nombre, fuerza, vida=100):
        super().__init__(nombre, vida)
        self.fuerza = fuerza
    
    def atacar(self):
        return f"Tu daño es de {self.fuerza}"

class Mago(Persona):
    def __init__(self, nombre, mana, vida=100):
        super().__init__(nombre, vida)
        self.mana = mana
        
    def lanzar_hechizo(self, costo_de_mana):
        if costo_de_mana > self.mana:
            return "No se pudo lanzar hechizo por falta de mana"
        
        # Restamos el maná consumido
        self.mana -= costo_de_mana
        return f"Lanzando hechizo. Maná restante: {self.mana}"


# Pruebas
jug1 = Persona("Anakin", 250)
print(jug1.recibir_danio(300))  # Supera la vida -> Ya se murió

jug2 = Guerrero("Tora", 450, 850)
print(jug2.recibir_danio(300))  # Queda con 550 de vida