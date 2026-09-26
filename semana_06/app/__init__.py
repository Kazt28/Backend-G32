from flask import Flask
from flask_restful import Api
from .config import config_map
from .extensions import db, migrate
from .models import *
from .api import CategoriaController

def create_app(env = "development"):
    app = Flask(__name__)
    api = Api(app)
    # From object> Actualiza los valores que le pasemos en el parametro para que la instancia
    # de Flask  arranque con esas modificaciones de sus parametros, por ejemplo debug, entre otros.
    app.config.from_object(config_map[env])
    
    # inicializamos la instancia de la base de datos pasandole la instancia de flask
    # para que utilice las variables que hemos configurado en la instancia (config_map)
    db.init_app(app)
    
    
    # Inicializamos la instancia de las migraciones para ahora declarar nuestra
    # configuracion de la instancia de flask y nuestra configuracion de la base de datos.
    migrate.init_app(app, db)
    
    api.add_resource(CategoriaController, "/categorias")
    
    return app
