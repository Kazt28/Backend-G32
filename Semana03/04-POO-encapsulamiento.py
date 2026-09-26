class CuentaBancaria:
    def __init__(self, titular, saldo, cuenta):
        self.titular = titular
        self.saldo = saldo
        # cuando se crea un atributo con un subguion este es protegido, es decir no se puede acceder
        # fuera de la clase
        # Si se puede heredar
        self._cuenta = cuenta
        # cuando el atributo empieza con doble subguion este es privado, ESTE NO SE PODRA ACCEDER
        self.__entidad_financiera = "BCP"
        
cuenta1 = CuentaBancaria("Manuel", 500, "100-123123123123-32132")
# se puede modificar los atributos que son publicos
cuenta1.saldo = 2500
# print(cuenta1.saldo)
# print(cuenta1._cuenta)
# print(cuenta1.__entidad_financiera) #AtributeError > Cuando el atributo no existe

# Para exponer atributos privados/protegidos de forma controlada se suele utilizar el decorador @property en vez
# de getters y setters como Java

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    # Luego del decorador siempre se llama a un metodo porque el decorador modifica la funcion adyacente
    # con la propiedad del decorador, en este caso, el decorador property sirve para definir la devolucion
    # del contenido del atributo privado
    # Con el decorador property convertimos un metodo a un atributo y sirve mayormente para exponer
    # el contenido de atributos privados y protegidos desde fuera de la clase.
    
    @property
    def nombre(self):
        return self.__nombre
    
    # Asi mismo se puede utilizar los metodos para modificar y eliminar el contenido del atributo privado
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
# p1 = Persona("Manuel")
# print(p1.nombre)
# p1.nombre = "Renato"
# print(p1.nombre)

class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.__password = None
    
    @property
    def password(self):
        return "***********" 
                 
    @password.setter
    def password(self, nueva_password):
        if " " in nueva_password or len(nueva_password) < 8:
            return "Password invalida, no puede tener espacios ni ser menor a 8 caracteres"
        self.__password = nueva_password
        
        
usuario1 = Usuario("Manuel", "manuel@hotmail.com")
# print(usuario1.password)
# usuario1.password = "aeiou"
# usuario1.password = "1234567689"
# print(usuario1.password)


class Empleado: 
    def __init__(self, nombre, sueldo_base, horas_extras):
        self.nombre = nombre
        self.__sueldo_base = sueldo_base
        self.__horas_extras = horas_extras

    def __calcular_pago_extra(self):
        valor_hora_extra = 20
        return self.__horas_extras * valor_hora_extra

    def calcular_sueldo_total(self):
        monto_extra = self.__calcular_pago_extra()
        return self.__sueldo_base + monto_extra

    def mostrar_boleta(self):
        print(f"""Empleado: {self.nombre}
Sueldo base: {self.__sueldo_base}
Pago extra: {self.__calcular_pago_extra()}
Total: {self.calcular_sueldo_total()}""")

emp1 = Empleado("Juanito",2000, 15)
# emp1.__calcular_pago_extra() # No se puede acceder a los metodos privados
# emp1.mostrar_boleta()

class Caja:
    def __init__(self, total):
        self.__total = total

    def __validar_monto(self, monto):
        return monto > 0
   
    def agregar_venta(self, monto):
        if self.__validar_monto(monto) == True:
            self.__total += monto
            return f"Monto {monto} validado, Total acumulado {self.__total}"
        else:
            return f"Error!!! el monto es: {monto}."
        
    def mostrar_total(self):
        return f"El monto total es: {self.__total}"

comp1 = Caja(500)
print(comp1.agregar_venta(500))
print(comp1.mostrar_total())