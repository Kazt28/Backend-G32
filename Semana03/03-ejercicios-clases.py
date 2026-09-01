# 1. Crear una clase Producto en el cual su constructor reciba el nombre, precio, 
# stock. Agregar un metodo esta_disponible en el cual muestre True si lo esta o no.


class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def esta_disponible(self):
        if self.stock >= 1:
            return True
        return False
    
producto1 = Producto("Vasija", 39, 3)
print(producto1.esta_disponible())

# 2. Crear una clase CarritoCompras en la cual en el constructor reciba el cliente y que
# inicialice una lista vacia de productos. Asi mismo, tener los metodos agregar_producto(nombre, precio),
# y cada producto se debe de guardar en un diccionario {"nombre":nombre, "precio":precio} a la lista. 
# Y otro metodo llamado calcular_total en el cual recorrera la lista de productos y me dara el precio 
# a pagar. 
# Y un metodo llamado limpiar_carrito en el cual limpiara todos los productos de la lista

class CarritoCompras:
    
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []
    
    def agregar_producto(self, nombre, precio):
        producto ={
            "nombre": nombre,
            "precio": precio
        }
        self.productos.append(producto)

    def calcular_total(self):
        sum_stock = 0
        for p in self.productos:
            sum_stock += p['precio']
        return f"El precio a pagar es: S/. {sum_stock}"
    
    def limpiar_carrito(self):
        self.productos.clear()

new_producto = CarritoCompras("Oswaldo")
new_producto.agregar_producto("leche", 20)
new_producto.agregar_producto("azucar", 30)
new_producto.agregar_producto("harina", 40)
new_producto.agregar_producto("polvo de hornear", 10)

print(new_producto.calcular_total())

# 3. Crear una clase Sesion (simular el login y logout)  en la cual en el 
# constructor recibamos un usuario y un atributo que sea activa = False. 
# Agregar el metodo iniciar_sesion que cambia activa = True y cerrar_sesion cambia activa 
# = False y un metodo 
# verificar_acceso que imprima "Acceso Permitido" si activa = True o "Acceso Denegado" 
# si activa = False

class Sesion:
    
    def __init__(self, usuario):
        self.usuario = usuario
        self.activa = False

    def iniciar_sesion(self):
        self.activa = True
    
    def cerrar_sesion(self):
        self.activa = False
    
    def verificar_acceso(self):
        if self.activa:
            print("Acceso permitido")
        else:
            print("Acceso Denegado")
            
sesion1 = Sesion("admin")

sesion1.iniciar_sesion()
sesion1.verificar_acceso()

sesion1.cerrar_sesion()
sesion1.verificar_acceso()