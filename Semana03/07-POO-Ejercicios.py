# 1. Crear un sistema para calcular sueldos de distintos tipos de empleados
# Clase base Empleado
# atributos: nombre (publico) y sueldo_base (privado)
# crear su getter y setter para el sueldo_base (el setter no debe permitir valores negativos)
# metodo calcular_sueldo() que retorna el sueldo_base
# mostrar_info() imprime el nombre y el sueldo calculado

# Clase hijas
# EmpleadoVentas y su atributo comision (monto fijo) y sobreescribir calcular_sueldo() para que retorne el sueldo_base + comision
# EmpleadoTiempoParcial y sus atributos horas_trabajadas y pago_por_hora y sobreescribir calcular_sueldo() para que retorne el horas_trabajas * pago_por_hora e ignora el sueldo base

# Para validar: 
# 1. crear una lista con al menos un objeto de cada clase 
# 2. Recorrer la lista con un for llamando siempre al metodo mostrar_info() 
# 3. Calcular e imprimir el total de la planilla (suma de todos los sueldos de los empleados)

class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base
    
    @property
    def sueldo_base(self):
        return self.__sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, nuevo_sueldo):
        if nuevo_sueldo < 0:
            self.__sueldo_base = 0
            print("El sueldo no puede ser negativo")
        else:
            self.__sueldo_base = nuevo_sueldo
            
    def calcular_sueldo(self):
        return self.sueldo_base
    
    def mostrar_info(self):
        print(f"Empleado {self.nombre}, su sueldo a pagar es S/.{self.calcular_sueldo()}")

class EmpleadoVentas(Empleado):
    def __init__(self, nombre, sueldo_base, comision):
        self.comision = comision
        super().__init__(nombre, sueldo_base)
    
    def calcular_sueldo(self):
        return self.sueldo_base + self.comision

class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, horas_trabajadas, pago_por_hora):
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora
        super().__init__(nombre, 0)
    
    def calcular_sueldo(self):
        return self.horas_trabajadas * self.pago_por_hora
    
planilla = [Empleado("Manuel", 9000), EmpleadoVentas("Jesus", 7000, 3000), EmpleadoTiempoParcial("Pedro", 50, 12)]
total_planilla = 0

for plani in planilla:
    plani.mostrar_info()
    total_planilla += plani.calcular_sueldo()

print(total_planilla)

# --------------------------------------

# 2. Crear un sistema de inventario simple
# Clase base Producto
# atributos: nombre, precio(privado) y stock
# crear getter y setter para el precio (no negativos)
# metodo calcular_precio_final() que por defecto retorna el precio sin cambios
# metodo vender(cantidad) que resta del stock si hay suficiente, sino, muestra un mensaje de error y no resta stock

# Clases hijas
# ProductoConDescuento: atributo porcentaje_descuento. sobreescribir calcular_precio_final() aplicar el dscto sobre el precio
# ProductoImportado: atributo impuesto_aduanero (porcentaje). sobreescribir calcular_precio_final() para sumar ese impuesto al precio

# Para validar 
# 1. crear una lista con al menos un objeto de cada clase 
# 2. Recorrer la lista con un for llamando siempre al metodo mostrar_info() 
# 3. Intentar asignar un precio negativo a alguno de ellos usando el setter y comprobar el mensaje de error

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            self.__precio = 0
            print("No ingresar montos negativos")
        else:
            self.__precio = nuevo_precio
    
    def calcular_precio_final(self):
        return self.precio
    
    def vender(self, cantidad):
        if cantidad > self.stock:
            print("No hay stock suficiente")
        else:
            self.stock -= cantidad
            
    def mostrar_info(self):
        print(f"Producto {self.nombre}, su precio es S/.{self.calcular_precio_final()} y quedan {self.stock} unidades")
        

class ProductoConDescuento(Producto):
    def __init__(self, nombre, precio, stock, porcentaje_descuento):
        self.porcentaje_descuento = porcentaje_descuento
        super().__init__(nombre, precio, stock)
    
    def calcular_precio_final(self):
        discount = self.precio * (self.porcentaje_descuento / 100)
        return self.precio - discount

class ProductoImportado(Producto):
    def __init__(self, nombre, precio, stock, impuesto_aduanero):
        self.impuesto_aduanero = impuesto_aduanero
        super().__init__(nombre, precio, stock)
    
    def calcular_precio_final(self):
        impuesto = self.precio * (self.impuesto_aduanero / 100)
        return self.precio + impuesto

Lista_productos = [Producto('TV', 1400, 5), ProductoConDescuento("Ipad", 4000, 2, 10), ProductoImportado("Dyson", 7000, 1, 8)]

for p in Lista_productos:
    p.mostrar_info()

Lista_productos[0].precio = -500

