from flask import Flask
#from flask_socketio import socketIO
 
from app.db import db, configure_db  # Importa la instancia de SQLAlchemy y la función configure_db desde db.py
from sqlalchemy import text  # Importa la función text de SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



# Importa tus modelos y controladores aquí dentro del contexto de la aplicación





app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.debug = True  # Activar el modo de depuración

#socketio = SocketIO(app)
 
#configuraciones
db = configure_db(app)
login_manager = LoginManager(app)
login_manager.login_view = 'user.login' # es la ruta donde sera redirigido el usuario al entrar a una pantalla a la cual no tiene permisos.


#importacion de vistas
from app.controllers import general # import de Blueprint de controllers
from app.user.userController import usuarioBP
from app.asosaciones.asosacionesController import asosacionesBP







# Configura la base de datos usando la función configure_db importada
app.register_blueprint(general)
app.register_blueprint(usuarioBP)
app.register_blueprint(asosacionesBP)


