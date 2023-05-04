from pydantic import BaseModel
from typing import Optional, List
from model.pokemon import Pokemon

from schemas import TipoSchema


class PokemonSchema(BaseModel):
    """ Define como um novo pókemon a ser inserido deve ser representado
    """
    id:int = 1
    nome:str = "Bubassauro"
    pre_evolucao_id:Optional[int] = 0


class PokemonBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do pókemon.
    """
    nome: str = "Bubassauro"

class PacotePokemonBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base na quantidade requisitada de pókemon.
    """
    qtde: int = 5

class ListagemPokemonsSchema(BaseModel):
    """ Define como uma listagem de pókemons será retornada.
    """
    pokemons:List[PokemonSchema]


def apresenta_pokemons(pokemons: List[Pokemon]):
    """ Retorna uma representação do pókemon seguindo o schema definido em
        PókemonViewSchema.
    """
    result = []
    for pokemon in pokemons:
        result.append({
            "id": pokemon.id,
            "nome": pokemon.nome,
            "pre_evolucao_id": pokemon.pre_evolucao_id,
            "total_tipos": len(pokemon.tipos),
            "tipos": [{"nome": p.nome} for p in pokemon.tipos]
        })

    return {"pokemons": result}


class PokemonViewSchema(BaseModel):
    """ Define como um pókemon será retornado: pókemon + tipos.
    """
    id: int = 1
    nome: str = "Bubassauro"
    pre_evolucao_id: Optional[int] = 0
    total_tipos: int = 1
    tipos:List[TipoSchema]


class PokemonDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    nome: str

def apresenta_pokemon(pokemon: Pokemon):
    """ Retorna uma representação do pókemon seguindo o schema definido em
        PókemonViewSchema.
    """
    return {
        "id": pokemon.id,
        "nome": pokemon.nome,
        "pre_evolucao_id": pokemon.pre_evolucao_id,
        "total_tipos": len(pokemon.tipos),
        "tipos": [{"nome": p.nome} for p in pokemon.tipos]
    }
