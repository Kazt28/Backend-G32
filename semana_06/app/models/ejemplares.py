from app.extensions import db
from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum

class EstadoEjemplar(Enum):
    DISPONIBLE = 'Disponible'
    PRESTADO = 'Prestado'
    NO_DISPONIBLE = 'NO_DISPONIBLE'


class Ejemplar(db.Model):
    __tablename__ = 'ejemplares'
     
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    codigo_inventario = Column(type_=types.VARCHAR(100), nullable=False, name='codigo_inventario')
    estado = Column(type_=types.Enum(EstadoEjemplar), default=EstadoEjemplar.DISPONIBLE)
    libroId = Column(ForeignKey(column='libros.id'), type_=types.Integer, nullable=False, name='libro_id') 

    
    libro = relationship('libros', backref='libros_ejemplaresz')
