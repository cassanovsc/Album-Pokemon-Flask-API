from pydantic import BaseModel
from typing import List
from model.album import Album

from schemas import PokemonSchema


class AlbumPokemonSchema(BaseModel):
    """ Define como um novo pókemon e o álbum a ser inserido devem ser representados
    """
    album_id:int = 1
    pokemon_id:int = 1


class AlbumBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca de um álbum. Que será
        feita apenas com base no id do álbum.
    """
    id:int = 1

class AlbumPokemonBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca de um pokémon em um álbum. Que será
        feita apenas com base no id do álbum e do pokémon.
    """
    album_id:int = 1
    pokemon_id:int = 1


class ListagemAlbunsSchema(BaseModel):
    """ Define como uma listagem de álbuns será retornada.
    """
    albuns:List[AlbumPokemonSchema]


def apresenta_albuns(albuns: List[Album]):
    """ Retorna uma representação do pókemon seguindo o schema definido em
        PokemonViewSchema.
    """
    result = []
    for album in albuns:
        result.append({
            "id": album.id,
            "pokemons": [{"id": p.id, 'nome': p.nome, 'pre_evolucao': p.pre_evolucao, 'tipos': [{'nome': t.nome} for t in p.tipos]} for p in album.pokemons]
        })

    return {"albuns": result}


class AlbumViewSchema(BaseModel):
    """ Define como um álbum será retornado: album + pokémons.
    """
    id:int = 1
    pokemon:List[PokemonSchema]


class AlbumPokemonDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    album_id: int
    pokemon_id: int

def apresenta_album(album: Album):
    """ Retorna uma representação do álbum seguindo o schema definido em
        AlbumViewSchema.message
    """
    
    pokemons = [{"id": p.id, 'nome': p.nome, 'pre_evolucao_id': p.pre_evolucao_id, 'tipos': [{'nome': t.nome} for t in p.tipos]} for p in album.pokemons]
    return {
        "id": album.id,
        "pokemons": pokemons
    }
