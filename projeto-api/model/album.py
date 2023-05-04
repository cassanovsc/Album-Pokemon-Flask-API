from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from  model import Base


class Album(Base):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True)
    pokemons = relationship('Pokemon', secondary='pokemon_album', back_populates='albuns')


    def __init__(self):
        """
        Cria um Album

        Arguments:
        """
        pass
