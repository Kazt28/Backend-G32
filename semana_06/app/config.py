from os import getenv


#El archivo config servira para asignar las variables que se usaran en flask
#Ya bien sea en development o produccion

class Base:
    # Esta propiedad sirve para poder indicar si SQL Alchemy nos muestre el seguimiento de las modificaciones en la base de datos
    SQLALCHEMY_TRACK_MODIFICATION = False
    
class Development(Base):
    # Esta propiedad permitira que se actualice automaticamente el servidor al guardar cualquier cambio
    DEBUG = True
    # Esta variable sirve para obtener la cadena de conexion a nuestra base de datos
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL")
    
class Production(Base):

    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL")
 
# Diccionario con el mapeo de todas las opciones de configuracion, se puede tener mas en el caso que tengamos
# Staging, Prepoduction, Debugging, etc   
config_map = {
    "development": Development,
    "production": Production
}