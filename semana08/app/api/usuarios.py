from flask_restful import Resource, request
from app.extensions import db
from app.Schemas import RegistroUsuarioSchema, LoginUsuarioSchema, UsuarioSchema, ResetPasswordSchema, ChangePasswordSchema
from pydantic import ValidationError
from app.models import Usuario
from bcrypt import gensalt, hashpw, checkpw
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from cryptography import fernet
from os import getenv
from json import dumps
from datetime import timedelta, datetime
from app.util import enviar_correo


class RegistroController(Resource):
    def post(self):
        try:
            dataValidada = RegistroUsuarioSchema.model_validate(request.get_json())
            print(dataValidada)

            usuarioExistente = db.session.query(Usuario).with_entities(Usuario.id).filter(Usuario.correo == dataValidada.correo).first()
            
            if usuarioExistente:
                return {
                    'message': "usuario ya existe"
                }, 400
            
            # Proceso del hashing de la password
            # 1. Generamos el texto de ayuda (salt)
            
            salt = gensalt()
            
            # 2. Convertimos el password a bytes
            password = dataValidada.password.encode()
            
            # 3. Hacemos el hashing de la password
            password_hasheada_bytes = hashpw(password, salt)
            
            # 4. Convertimos el hashing del password en bytes a str
            password_hasheada = password_hasheada_bytes.decode()
            
            # TODO ESTE PROCESO SE PUEDE RESUMIR EN UN SOLO PAASO
            # password_hasheada = hashpw(dataValidada.password.encode(),gensalt()).decode()
            
            print(password_hasheada)
            
            nuevoUsuario = Usuario(
                # correo = dataValidada.correo,
                # password = password_hasheada,
                # nombre = dataValidada.nombre,
                # apellido = dataValidada.apellido
                **dataValidada.model_dump(exclude={"password"}),
                password = password_hasheada
                )
            db.session.add(nuevoUsuario)
            db.session.commit()
            
            return {
                'message': 'Usuario registrado exitosamente'
            }, 201
            
        except ValidationError as error:
            return {
                'message': 'Error al crear al usuario',
                'content': error.errors(include_context=False)
            },400
    
class LoginController(Resource):
    def post(self):
        try:
            dataValidada = LoginUsuarioSchema.model_validate(request.get_json())
            usuarioEncontrado = db.session.query(Usuario).filter(Usuario.correo == dataValidada.correo).first()
            
            if not usuarioEncontrado:
                return {
                    'message': 'Usuario no existe'
                }, 404
            password = dataValidada.password.encode()
            hashedPassword = usuarioEncontrado.password.encode()
            
            esLaPassword = checkpw(password, hashedPassword)
            
            if esLaPassword:
                jwt = create_access_token(usuarioEncontrado.id,
                                    fresh=False,
                                    expires_delta=timedelta(hours=8, minutes=5))
                return {
                    'content': jwt
                }
            else:
                return {
                    'message': 'Credenciales Incorrectas'
                }, 400
            
        except ValidationError as error:
            return{
                'message': 'Error al hacer login',
                'content': error.errors(include_context=False)
            }        

class UsuarioController(Resource):
    @jwt_required()
    def get(self):
        id = get_jwt_identity()
        
        usuarioEncontrado = db.session.query(Usuario).filter(Usuario.id == id).first()
        
        resultado = UsuarioSchema.model_validate(usuarioEncontrado).model_dump(mode='json')
        
        return {
            'content': resultado
        }

class ChangePasswordController(Resource):
    @jwt_required()
    def post(self):
        try:
            id = get_jwt_identity()
            dataValidada = ChangePasswordSchema.model_validate(request.get_json())
            usuarioEncontrado = db.session.query(Usuario).filter(Usuario.id == id).first()
            hashPassword = usuarioEncontrado.password.encode()
            passwordActual = dataValidada.passwordActual.encode()
            
            if not checkpw(passwordActual, hashPassword):
                return {
                    'message': 'La password actual no es la correcta'
                }, 403
            
            salt = gensalt()
            nuevaPassword = dataValidada.nuevaPassword.encode()
            nuevaPasswordHasheada = hashpw(nuevaPassword, salt).decode()
            
            usuarioEncontrado.password = nuevaPasswordHasheada
            db.session.commit()
        
            return {
                    'message': 'Password cambiada exitosamente'
                }
        except ValidationError as error:
            return {
                'message': 'Error al cambiar password',
                'content': error.errors(include_context=False)
            }
            
class ResetPasswordController(Resource):
    def post(self):
        try:
            
            dataValidada = ResetPasswordSchema.model_validate(request.get_json())
            usuarioEncontrado = db.session.query(Usuario).filter(Usuario.correo == dataValidada.correo).first()
            if not usuarioEncontrado:
                return {
                    'message': 'Usuario no existe en el sistema'
                },400
                
            # Comenzamos iniciando fernet con nuestra llave
            encriptador = fernet.Fernet(getenv('FERNET_KEY'))
            horaActual = datetime.now()
            fechaVencimiento = horaActual + timedelta(minutes=30)
            data = {
                "usuarioId": str(usuarioEncontrado.id),
                "vence": fechaVencimiento.strftime("%Y-%m-%d %H:%M:%S")
            }
            dataConvertida = dumps(data).encode()
            dataEncriptada = encriptador.encrypt(dataConvertida)
            print(dataEncriptada)
            
            cuerpo = f"""
                <h1>Hola! </h1>
                <p>Haz solicitado restaurar tu password, para hacerlo haz click en el siguiente enlace: {dataEncriptada.decode()}. </br>
                Si no has sido tu, haz caso omiso a este correo. </p>
                """
            
            enviar_correo(usuarioEncontrado.correo, "Resetear Correo", cuerpo)
            
            return {
                'message': 'Se envio el correo para la restauracion'
            }
            
        except ValidationError as error:
            return {
                'message': 'Error al resetear password',
                'content': error.errors(include_context=False)
            },400
            
        