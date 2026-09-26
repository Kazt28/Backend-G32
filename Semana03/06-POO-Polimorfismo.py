class Animal:
    def hacer_sonido(self):
        print("Este animal hace un sonido")

class Perro(Animal):
    def hacer_sonido(self):
        print("guau guau")

class Gato(Animal):
    def hacer_sonido(self):
        super().hacer_sonido
        return "miau miau"
        
class Vaca(Animal):
    def hacer_sonido(self):
        print("Muuu")

animales = [Perro(), Gato(), Vaca()]

# for animal in animales:
#     # El mismo metodo tiene diferente resultado(forma)
#     animal.hacer_sonido()


michi = Gato()
print(michi.hacer_sonido())