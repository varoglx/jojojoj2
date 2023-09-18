from app.db import db
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

usuario_sucursal = Table(
    'usuario_sucursal',
    db.metadata,
    db.Column('usuario_id', db.Integer, db.ForeignKey('usuarios.id')),
    db.Column('sucursal_id', db.Integer, db.ForeignKey('sucursal.id_sucursal'))
)


