from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from random import randrange

from model import Session, Pokemon, Album
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Álbum Pokémon API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Documentação Swagger")
pokemon_tag = Tag(name="Pokémon", description="Adição, visualização e remoção de pókemons à base")
album_tag = Tag(name="Álbum Pokémon", description="Adição, visualização e remoção de pókemons do álbum à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi/swagger, tela de documentação.
    """
    return redirect('/openapi/swagger')


@app.post('/pokemon', tags=[pokemon_tag],
          responses={"200": PokemonViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_pokemon(form: PokemonSchema):
    """Adiciona um novo Pókemon à base de dados

    Retorna uma representação dos pókemons.
    """
    pokemon = Pokemon(
        id = form.id,
        nome = form.nome,
        pre_evolucao_id = form.pre_evolucao_id if (form.pre_evolucao_id) else None
        )
    logger.debug(f"Adicionando pókemon de nome: '{pokemon.nome}'")
    try:
        #criando conexão com a base
        session = Session()
        #adicionando pókemon
        session.add(pokemon)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado pókemon de nome: '{pokemon.nome}'")

        return apresenta_pokemon(pokemon), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Pókemon de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar pókemon '{pokemon.nome}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar pókemon '{pokemon.nome}', {error_msg}")
        return {"message": error_msg}, 400


@app.get('/pokemons', tags=[pokemon_tag],
         responses={"200": ListagemPokemonsSchema, "404": ErrorSchema})
def get_pokemons():
    """Faz a busca por todos os Pokémons cadastrados

    Retorna uma representação da listagem de pókemons.
    """
    logger.debug(f"Coletando pókemons ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    pokemons = session.query(Pokemon).all()

    if not pokemons:
        # se não há pokemonos cadastrados
        return {"pókemons": []}, 200
    else:
        logger.debug(f"%d pókemons econtrados" % len(pokemons))
        # retorna a representação de pókemon
        return apresenta_pokemons(pokemons), 200


@app.get('/pokemon', tags=[pokemon_tag],
         responses={"200": PokemonViewSchema, "404": ErrorSchema})
def get_pokemon(query: PokemonBuscaSchema):
    """Faz a busca por um Pokémon a partir do nome do pokémon

    Retorna uma representação dos pokémons.
    """
    pokemon_nome = unquote(unquote(query.nome))
    logger.debug(f"Coletando dados sobre pókemon #{pokemon_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    pokemon = session.query(Pokemon).filter(Pokemon.nome == pokemon_nome).first()

    if not pokemon:
        # se o pókemon não foi encontrado
        error_msg = "Pókemon não encontrado na base :/"
        logger.warning(f"Erro ao buscar pókemon '{pokemon_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Pókemon econtrado: '{pokemon.nome}'")
        # retorna a representação de pókemon
        return apresenta_pokemon(pokemon), 200


@app.delete('/pokemon', tags=[pokemon_tag],
            responses={"200": PokemonDelSchema, "404": ErrorSchema})
def del_pokemon(query: PokemonBuscaSchema):
    """Deleta um Pókemon a partir do nome de pókemon informado

    Retorna uma mensagem de confirmação da remoção.
    """
    pokemon_nome = unquote(unquote(query.nome))
    logger.debug(f"Deletando dados sobre pókemon #{pokemon_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Pokemon).filter(Pokemon.nome == pokemon_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado pókemon #{pokemon_nome}")
        return {"message": "Pókemon removido", "nome": pokemon_nome}
    else:
        # se o pókemon não foi encontrado
        error_msg = "Pókemon não encontrado na base :/"
        logger.warning(f"Erro ao deletar pókemon #'{pokemon_nome}', {error_msg}")
        return {"message": error_msg}, 404



@app.get('/album_pokemon', tags=[album_tag],
         responses={"200": AlbumViewSchema, "404": ErrorSchema})
def get_album(query: AlbumBuscaSchema):
    """Faz a busca por um Álbum a partir do id do álbum

    Retorna uma representação dos álbums e pokémons associados.
    """
    album_id = query.id
    logger.debug(f"Coletando dados sobre álbum #{album_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    album = session.query(Album).filter(Album.id == album_id).first()

    if not album:
        # se o album não foi encontrado
        error_msg = "Album não encontrado na base :/"
        logger.warning(f"Erro ao buscar album '{album_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Album econtrado: '{album_id}'")
        # retorna a representação de album
        return apresenta_album(album), 200


@app.get('/pacote_pokemons', tags=[pokemon_tag],
         responses={"200": PokemonViewSchema, "404": ErrorSchema})
def get_pacote_pokemon(query: PacotePokemonBuscaSchema):
    """Faz a busca por uma quantidade de Pokémons a partir da quantidade informada

    Retorna uma representação da listagem da quantidade de pokémons solicitados.
    """
    pacote_qtde = query.qtde
    logger.debug(f"Coletando dados sobre #{pacote_qtde} pókemons")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    pokemons = session.query(Pokemon).all()

    if not pokemons or not pacote_qtde:
        # se não existir pokémons
        error_msg = "Pókemons não encontrados na base :/"
        logger.warning(f"Erro ao buscar pókemons, {error_msg}")
        return {"message": error_msg}, 404
    else:
        pokemons_catched = []
        for i in range(pacote_qtde):
            pokemons_catched.append(pokemons.pop(randrange(len(pokemons))))
        logger.debug(f"Pókemons obtidos ({pacote_qtde})")
        # retorna a representação de pókemon
        return apresenta_pokemons(pokemons_catched), 200


@app.post('/album_pokemon', tags=[album_tag],
          responses={"200": AlbumViewSchema, "404": ErrorSchema})
def add_album_pokemon(form: AlbumPokemonSchema):
    """Adicionade um novo pokémon a um álbum na base identificados pelo id

    Retorna uma representação dos pókemons do álbum.
    """
    pokemon_id  = form.pokemon_id
    album_id  = form.album_id
    logger.debug(f"Adicionando pokémon #{pokemon_id} ao álbum #{album_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca pelo álbum
    album = session.query(Album).filter(Album.id == album_id).first()

    if any(pokemon.id == pokemon_id for pokemon in album.pokemons):
        error_msg = "Pokémon repetido no álbum"
        logger.warning(f"Erro ao adicionar pokémon '{pokemon_id}' ao álbum '{album_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        album.pokemons.append(session.query(Pokemon).filter(Pokemon.id == pokemon_id).first())
        session.commit()

    # retorna a representação de album
    return apresenta_album(album), 200


@app.delete('/album_pokemon', tags=[album_tag],
            responses={"200": AlbumPokemonDelSchema, "404": ErrorSchema})
def del_album_pokemon(query: AlbumPokemonBuscaSchema):
    """Deleta um Pókemon de um álbum a partir do id do pokémon e do álbum informado

    Retorna uma mensagem de confirmação da remoção.
    """
    album_id = 1
    pokemon_id = query.pokemon_id
    logger.debug(f"Deletando pokémon #{pokemon_id} no álbum {album_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    album = session.query(Album).filter(Album.id == album_id).first()
    
    pokemon = session.query(Pokemon).filter(Pokemon.id == pokemon_id).first()

    if pokemon in album.pokemons:
        album.pokemons.remove(pokemon)
        session.commit()
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado pókemon #{album_id} no álbum {album_id}")
        return {"message": "Pókemon removido", "album_id": album_id, "pókemon_id": pokemon_id}
    else:
        # se o pókemon não foi encontrado
        error_msg = "Pókemon não encontrado na base :/"
        logger.warning(f"Erro ao deletar pókemon #'{pokemon_id} no álbum {album_id}', {error_msg}")
        return {"message": error_msg}, 404