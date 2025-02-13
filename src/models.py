import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    especie: Mapped[str]
    bando: Mapped[str]
    planeta_id: Mapped[int] = mapped_column(nullable=False)

    planeta_id = Column(Integer, ForeignKey('planetas.id'), nullable=False)
    usuarios_favoritos = relationship("Favoritos", back_populates="personaje")

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str]
    clima: Mapped[str]
    poblacion: Mapped[str] = mapped_column(nullable=False)

    personajes = relationship("Personajes", back_populates="planeta")

class Usuarios(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str]
    email: Mapped[str]
    contrasena: Mapped[str] = mapped_column(nullable=False)

    favoritos = relationship("Favoritos", back_populates="usuario")

class Favoritos(Base):
    __tablename__= 'favoritos'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_usuario: Mapped[int] = mapped_column(Integer, ForeignKey('usuarios.id'), nullable=False)
    id_personaje: Mapped[int] = mapped_column(Integer, ForeignKey('personajes.id'), nullable=True)
    id_planeta: Mapped[int] = mapped_column(Integer, ForeignKey('planetas.id'), nullable=True)


    usuario = relationship("Usuarios", back_populates="favoritos")
    personaje = relationship("Personajes", back_populates="usuarios_favoritos")
    planeta = relationship("Planetas")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
