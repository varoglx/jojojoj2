from flask import  Blueprint,render_template
# from flask_socketio import socketIO
from app import app #app es la carpeta "app"
#socketio
from werkzeug.security import generate_password_hash
from app.db import db, configure_db  # Importa la instancia de SQLAlchemy y la función configure_db desde db.py
from sqlalchemy import text  # Importa la función text de SQLAlchemy
from datetime import datetime

#importacion de modelos para poblado
from app.user.models import Usuarios

#inicializacion blueprint
general = Blueprint('app',__name__)





