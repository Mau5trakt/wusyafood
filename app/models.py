from sqlalchemy import Column, String, Integer, Sequence, VARCHAR
from app.db import Base, engine


class Usuarios(Base):
    __tablename__ = 'Usuarios'
    id = Column(Integer, autoincrement=True, primary_key=True)
    nombre = Column(VARCHAR(70))

Base.metadata.create_all(engine)