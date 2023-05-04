from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from  model import Base


class Tipo(Base):
    __tablename__ = 'tipo'

    id = Column(Integer, primary_key=True)
    nome = Column(String(20))
    pokemons = relationship('Pokemon', secondary='pokemon_tipo', back_populates='tipos')


    def __init__(self, nome:str):
        """
        Cria um Tipo

        Arguments:
            nome: o nome de um tipo.
        """
        self.nome = nome
