from flask_login import UserMixin
from app.db import db
from werkzeug.security import check_password_hash
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship
from app.asosaciones.models import usuario_sucursal



class Usuarios(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    username = db.Column(db.String(100))
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    password = db.Column(db.String(150))
    admin = db.Column(Boolean,default=False)
    def check_password(self,password):
     return check_password_hash(self.password,password)
    
    sucursales = relationship('Sucursal', secondary=usuario_sucursal, back_populates='usuarios')

    
    