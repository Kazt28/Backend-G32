from app.extensions import db
from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship

class LibroCategoria(db.Model):
    __tablename__='libros_categorias'
    
    libroId = Column(ForeignKey(column='libros.id'), 
                    nullable=False, 
                    name='libro_id', 
                    primary_key=True)
    categoriaId = Column(ForeignKey(column='categorias.id'),
                         nullable=False, 
                         name='categoria_id', 
                         primary_key=True, 
                         type_=types.Integer)
    
    
    libro = relationship('Libro', backref='libro_categoria')
    categoria = relationship('Categoria', backref='libro_categoria')