from sqlalchemy import String
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from app.db import db
from app.asosaciones.models import usuario_sucursal
class Sucursal(db.Model):
    __tablename__ = 'sucursal'
    id_sucursal =db.Column(db.Integer, primary_key=True)
    nombre_sucursal =db.Column(String(255))
    
    usuarios = relationship('Usuarios', secondary=usuario_sucursal, back_populates='sucursales')
    
    
        