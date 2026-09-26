# EJERCICIO 3
# a) Crea una clase llamada Libro que en su constructor (init) 
# reciba: titulo, autor y paginas. Agrega un metodo llamado resumen() que imprima algo como:
# "El libro TITULO fue escrito por AUTOR y tiene PAGINAS paginas" Luego crea una instancia de la 
# clase y llama al método resumen().

# b) Crea una clase llamada CuentaBancaria con: - Atributos: titular (publico) y 
# saldo (debe ser un atributo PRIVADO, es decir, con doble guion bajo). - 
# Un getter para saldo usando el decorador @property. - Un metodo depositar(monto) que 
# aumente el saldo solo si el monto es mayor a 0 (si no, mostrar un mensaje de error). 
# - Un metodo retirar(monto) que reste el saldo solo si hay saldo suficiente (si no, 
# mostrar un mensaje de error). Crea una instancia y prueba los métodos con al menos 2 depositos 
# y 2 retiros (uno de ellos debe fallar a proposito para comprobar la validacion).

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def resumen(self):
        print(f"El libro {self.titulo} fue escrito por {self.autor} y tiene {self.paginas} paginas")

new_book = Libro("100 años de soledad", "Gabriel Garcia Marquez", 471)
new_book.resumen()


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
        
    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            return f"Se deposito {monto} el nuevo saldo es: {self.__saldo}"
        else:
            return "Error!! ingresa un monto valido"
            
    def retirar_monto(self, monto):
        if self.__saldo >= monto and monto > 0:
            self.__saldo -= monto
            return f"Se retiro {monto} el nuevo saldo es: {self.__saldo}"
        else:
            return "Error!!! monto de retiro no valido"
            
mi_bcp = CuentaBancaria("Manuel", 300)
mi_ibk = CuentaBancaria("Andrea", 200)

print(mi_bcp.depositar(500))
print(mi_bcp.depositar(700))
print(f"El saldo final de {mi_bcp.titular} es de {mi_bcp.saldo}")

print(mi_bcp.retirar_monto(800))
print(mi_bcp.retirar_monto(-80))
print(f"El saldo final de {mi_bcp.titular} es de {mi_bcp.saldo}")