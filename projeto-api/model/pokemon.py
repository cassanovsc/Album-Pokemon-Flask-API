from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from typing import Union

from  model import Base


class Pokemon(Base):
    __tablename__ = 'pokemon'
    id = Column(Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    pre_evolucao_id = Column(Integer, ForeignKey('pokemon.id'))
    evolucao = relationship('Pokemon', remote_side=id, backref='pre_evolucao')
    tipos = relationship('Tipo', secondary='pokemon_tipo', back_populates='pokemons')
    albuns = relationship('Album', secondary='pokemon_album', back_populates='pokemons')


    def __init__(self, id:int, nome:str, pre_evolucao_id:Union[int, None] = None):
        """
        Cria um Pókemon

        Arguments:
            id: id do pókemon
            nome: nome do pókemon
            pre_evolucao_id: id da evolucao do pókemon
        """
        self.id = id
        self.nome = nome
        
        if pre_evolucao_id:
            self.pre_evolucao_id = pre_evolucao_id
