from app.extensions import db
from sqlalchemy import Column, types

# Las tablas de las bases de datos van a ser Clases en Python
# Al heredar la clase model estamos indicando a SQLALCHEMY que esta clase va a ser
# mapeada como una tabla en la bd
class Usuario(db.Model):
    # La clase model usa el atributo __tablename__ para indicar como se llamara esta 
    # tabla en la base de datos
    __tablename__ = "usuarios"
    
    # Ahora mapeamos todas las columnas como si fueran atributos de la clase, en este caso
    # no se usa constructores ya que la clase Model lo maneja diferente
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text)
    apellidoPaterno = db.Column(name='apellido_pat', type_=db.Text, nullable=False)
    apellidoMaterno = Column(name='apellido_mat', type_=types.Text)
    correo = Column(type_=types.Text, unique=True, nullable=False)
    fechaNacimiento = Column(name='fecha_nacimiento', type_=types.Date)