from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from  model import Base


class PokemonTipo(Base):
    __tablename__ = 'pokemon_tipo'

    id = Column(Integer, primary_key=True)
    tipo_id = Column(Integer, ForeignKey('tipo.id'))
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))

    def __init__(self, tipo_id:int, pokemon_id:int):
        """
        Cria um Tipo de Pokemon

        Arguments:
            tipo_id: id do tipo
            pokemon_id: id do pokémon
        """
        self.tipo_id = tipo_id
        self.pokemon_id = pokemon_id