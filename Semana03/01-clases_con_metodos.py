# Las clases SIEMPRE empiezan con Mayuscula

class Mueble:
    def __init__(self, alto, ancho, largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo
    
    def dimensiones(self):
        print("Las dimensiones son: ")
        
# m1 = Mueble(1.4, 0.7, 1.2)
# m1.dimensiones()

class Rectangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

area1 = Rectangulo(20, 30)
# print(f"Area: {area1.calcular_area()}")

class Estudiante:
    
    def __init__(self, nombre, notas, correo):
        self.nombre = nombre
        self.notas = notas
        self.correo = correo
        
    def agregar_nota(self, nota):
        self.notas.append(nota)
    
    def promedio(self):
        promedio_nota = sum(self.notas) / len(self.notas)
        print(f"Promedio: {promedio_nota:.2f}")
        
        if promedio_nota >= 13:
            print("Aprobado")
        elif promedio_nota >= 11:
            print("Subsanado")
        else:
            print("Jalado")
        return promedio_nota
    
alumno1 = Estudiante("Manuel", [14, 16, 18], "manuel@correo")
alumno1.agregar_nota(15)
promedio_final = alumno1.promedio()        
print(f"{alumno1.nombre} obtuvo un promedio de {promedio_final}")

print(alumno1.notas)