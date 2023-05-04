from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from  model import Base


class PokemonAlbum(Base):
    __tablename__ = 'pokemon_album'

    id = Column(Integer, primary_key=True)
    album_id = Column(Integer, ForeignKey('album.id'))
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))

    def __init__(self, album_id:int, pokemon_id:int):
        """
        Cria um Album de Pokémon

        Arguments:
            album_id: id do album
            pokemon_id: id do pokémon
        """
        self.album_id = album_id
        self.pokemon_id = pokemon_id