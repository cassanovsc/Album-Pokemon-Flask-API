from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os elementos definidos no modelo
from model.base import Base
from model.pokemon import Pokemon
from model.tipo import Tipo
from model.pokemon_tipo import PokemonTipo
from model.album import Album
from model.pokemon_album import PokemonAlbum

db_path = "database/"
# Verifica se o diretorio não existe
if not os.path.exists(db_path):
   # então cria o diretorio
   os.makedirs(db_path)

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir 
if not database_exists(engine.url):
    create_database(engine.url) 

# cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)

session = Session()

pokemons = [
{"id": 1, "nome": 'Bulbassauro', "pre_evolucao_id": None, "tipos": [{"nome": 'Grama'}, {'nome': 'Venenoso'}]},
{"id": 2, "nome": 'Ivyssauro', "pre_evolucao_id": 1, "tipos": [{"nome": 'Grama'}, {'nome': 'Venenoso'}]},
{"id": 3, "nome": 'Venussauro', "pre_evolucao_id": 2, "tipos": [{"nome": 'Grama'}, {'nome': 'Venenoso'}]},
{"id": 4, "nome": 'Charmander', "pre_evolucao_id": None, "tipos": [{"nome": 'Fogo'}]},
{"id": 5, "nome": 'Charmeleon', "pre_evolucao_id": 4, "tipos": [{"nome": 'Fogo'}]},
{"id": 6, "nome": 'Charizard', "pre_evolucao_id": 5, "tipos": [{"nome": 'Fogo'}, {'nome': 'Voador'}]},
{"id": 7, "nome": 'Squirtle', "pre_evolucao_id": None, "tipos": [{"nome": 'Água'}]},
{"id": 8, "nome": 'Wartortle', "pre_evolucao_id": 7, "tipos": [{"nome": 'Água'}]},
{"id": 9, "nome": 'Blastoise', "pre_evolucao_id": 8, "tipos": [{"nome": 'Água'}]},
{"id": 10, "nome": 'Caterpie', "pre_evolucao_id": None, "tipos": [{"nome": 'Inseto'}]},
{"id": 11, "nome": 'Metapod', "pre_evolucao_id": 10, "tipos": [{"nome": 'Inseto'}]},
{"id": 12, "nome": 'Butterfree', "pre_evolucao_id": 11, "tipos": [{"nome": 'Inseto'}, {'nome': 'Voador'}]},
{"id": 13, "nome": 'Weedle', "pre_evolucao_id": None, "tipos": [{"nome": 'Inseto'}, {'nome': 'Venenoso'}]},
{"id": 14, "nome": 'Kakuna', "pre_evolucao_id": 13, "tipos": [{"nome": 'Inseto'}, {'nome': 'Venenoso'}]},
{"id": 15, "nome": 'Beedrill', "pre_evolucao_id": 14, "tipos": [{"nome": 'Inseto'}, {'nome': 'Venenoso'}]},
{"id": 16, "nome": 'Pidgey', "pre_evolucao_id": None, "tipos": [{"nome": 'Normal'}, {'nome': 'Voador'}]},
{"id": 17, "nome": 'Pidgeotto', "pre_evolucao_id": 16, "tipos": [{"nome": 'Normal'}, {'nome': 'Voador'}]},
{"id": 18, "nome": 'Pidgeot', "pre_evolucao_id": 17, "tipos": [{"nome": 'Normal'}, {'nome': 'Voador'}]},
{"id": 19, "nome": 'Rattata', "pre_evolucao_id": None, "tipos": [{"nome": 'Normal'}]},
{"id": 20, "nome": 'Raticate', "pre_evolucao_id": 19, "tipos": [{"nome": 'Normal'}]},
{"id": 21, "nome": 'Spearow', "pre_evolucao_id": None, "tipos": [{"nome": 'Normal'}, {'nome': 'Voador'}]},
{"id": 22, "nome": 'Fearow', "pre_evolucao_id": 21, "tipos": [{"nome": 'Normal'}, {'nome': 'Voador'}]},
{"id": 23, "nome": 'Ekans', "pre_evolucao_id": None, "tipos": [{"nome": 'Venenoso'}]},
{"id": 24, "nome": 'Arbok', "pre_evolucao_id": 23, "tipos": [{"nome": 'Venenoso'}]},
{"id": 25, "nome": 'Pikachu', "pre_evolucao_id": None, "tipos": [{"nome": 'Elétrico'}]},
{"id": 26, "nome": 'Raichu', "pre_evolucao_id": 25, "tipos": [{"nome": 'Elétrico'}]},
{"id": 27, "nome": 'Sandshrew', "pre_evolucao_id": None, "tipos": [{"nome": 'Terrestre'}]},
{"id": 28, "nome": 'Sandslash', "pre_evolucao_id": 27, "tipos": [{"nome": 'Terrestre'}]},
{"id": 29, "nome": 'Nidoran♀', "pre_evolucao_id": None, "tipos": [{"nome": 'Venenoso'}]},
{"id": 30, "nome": 'Nidorina', "pre_evolucao_id": 29, "tipos": [{"nome": 'Venenoso'}]},
{"id": 31, "nome": 'Nidoqueen', "pre_evolucao_id": 30, "tipos": [{"nome": 'Venenoso'}, {'nome': 'Terrestre'}]},
{"id": 32, "nome": 'Nidoran♂', "pre_evolucao_id": None, "tipos": [{"nome": 'Venenoso'}]},
{"id": 33, "nome": 'Nidorino', "pre_evolucao_id": 32, "tipos": [{"nome": 'Venenoso'}]},
{"id": 34, "nome": 'Nidoking', "pre_evolucao_id": 33, "tipos": [{"nome": 'Venenoso'}, {'nome': 'Terrestre'}]},
{"id": 35, "nome": 'Clefairy', "pre_evolucao_id": None, "tipos": [{"nome": 'Fada'}]},
{"id": 36, "nome": 'Clefable', "pre_evolucao_id": 35, "tipos": [{"nome": 'Fada'}]},
{"id": 37, "nome": 'Vulpix', "pre_evolucao_id": None, "tipos": [{"nome": 'Fogo'}]},
{"id": 38, "nome": 'Ninetales', "pre_evolucao_id": 37, "tipos": [{"nome": 'Fogo'}]},
{"id": 39, "nome": 'Jigglypuff', "pre_evolucao_id": None, "tipos": [{"nome": 'Normal'}, {'nome': 'Fada'}]},
{"id": 40, "nome": 'Wigglytuff', "pre_evolucao_id": 39, "tipos": [{"nome": 'Normal'}, {'nome': 'Fada'}]},
{"id": 41, "nome": 'Zubat', "pre_evolucao_id": None, "tipos": [{"nome": 'Venenoso'}, {'nome': 'Voador'}]},
{"id": 42, "nome": 'Golbat', "pre_evolucao_id": 41, "tipos": [{"nome": 'Venenoso'}, {'nome': 'Voador'}]},
{"id": 43, "nome": 'Oddish', "pre_evolucao_id": None, "tipos": [{"nome": 'Grama'}, {'nome': 'Venenoso'}]},
{"id": 44, "nome": 'Gloom', "pre_evolucao_id": 43, "tipos": [{"nome": 'Grama'}, {'nome': 'Venenoso'}]},
{"id": 45, "nome": 'Vileplume', "pre_evolucao_id": 44, "tipos": [{"nome": 'Grama'}, {'nome': 'Venenoso'}]},
{"id": 46, "nome": 'Paras', "pre_evolucao_id": None, "tipos": [{"nome": 'Inseto'}, {'nome': 'Grama'}]},
{"id": 47, "nome": 'Parasect', "pre_evolucao_id": 46, "tipos": [{"nome": 'Inseto'}, {'nome': 'Grama'}]},
{"id": 48, "nome": 'Venonat', "pre_evolucao_id": None, "tipos": [{"nome": 'Inseto'}, {'nome': 'Venenoso'}]},
{"id": 49, "nome": 'Venomoth', "pre_evolucao_id": 48, "tipos": [{"nome": 'Inseto'}, {'nome': 'Venenoso'}]},
{"id": 50, "nome": 'Diglett', "pre_evolucao_id": None, "tipos": [{"nome": 'Terrestre'}]},
{"id": 51, "nome": 'Dugtrio', "pre_evolucao_id": 50, "tipos": [{"nome": 'Terrestre'}]},
{"id": 52, "nome": 'Meowth', "pre_evolucao_id": None, "tipos": [{"nome": 'Normal'}]},
{"id": 53, "nome": 'Persian', "pre_evolucao_id": 52, "tipos": [{"nome": 'Normal'}]},
{"id": 54, "nome": 'Psyduck', "pre_evolucao_id": None, "tipos": [{"nome": 'Água'}]},
{"id": 55, "nome": 'Golduck', "pre_evolucao_id": 54, "tipos": [{"nome": 'Água'}]},
{"id": 56, "nome": 'Mankey', "pre_evolucao_id": None, "tipos": [{"nome": 'Lutador'}]},
{"id": 57, "nome": 'Primeape', "pre_evolucao_id": 56, "tipos": [{"nome": 'Lutador'}]},
{"id": 58, "nome": 'Growlithe', "pre_evolucao_id": None, "tipos": [{"nome": 'Fogo'}]},
{"id": 59, "nome": 'Arcanine', "pre_evolucao_id": 58, "tipos": [{"nome": 'Fogo'}]},
{"id": 60, "nome": 'Poliwag', "pre_evolucao_id": None, "tipos": [{"nome": 'Água'}]},
{"id": 61, "nome": 'Poliwhirl', "pre_evolucao_id": 60, "tipos": [{"nome": 'Água'}]},
{"id": 62, "nome": 'Poliwrath', "pre_evolucao_id": 61, "tipos": [{"nome": 'Água'}, {'nome': 'Lutador'}]},
{"id": 63, "nome": 'Abra', "pre_evolucao_id": None, "tipos": [{"nome": 'Psíquico'}]},
{"id": 64, "nome": 'Kadabra', "pre_evolucao_id": 63, "tipos": [{"nome": 'Psíquico'}]},
{"id": 65, "nome": 'Alakazam', "pre_evolucao_id": 64, "tipos": [{"nome": 'Psíquico'}]},
{"id": 66, "nome": 'Machop', "pre_evolucao_id": None, "tipos": [{"nome": 'Lutador'}]},
{"id": 67, "nome": 'Machoke', "pre_evolucao_id": 66, "tipos": [{"nome": 'Lutador'}]},
{"id": 68, "nome": 'Machamp', "pre_evolucao_id": 67, "tipos": [{"nome": 'Lutador'}]},
{"id": 69, "nome": 'Bellsprout', "pre_evolucao_id": None, "tipos": [{"nome": 'Grama'}, {'nome': 'Venenoso'}]},
{"id": 70, "nome": 'Weepinbell', "pre_evolucao_id": 69, "tipos": [{"nome": 'Grama'}, {'nome': 'Venenoso'}]},
{"id": 71, "nome": 'Victreebel', "pre_evolucao_id": 70, "tipos": [{"nome": 'Grama'}, {'nome': 'Venenoso'}]},
{"id": 72, "nome": 'Tentacool', "pre_evolucao_id": None, "tipos": [{"nome": 'Água'}, {'nome': 'Venenoso'}]},
{"id": 73, "nome": 'Tentacruel', "pre_evolucao_id": None, "tipos": [{"nome": 'Água'}, {'nome': 'Venenoso'}]},
{"id": 74, "nome": 'Geodude', "pre_evolucao_id": None, "tipos": [{"nome": 'Pedra'}, {'nome': 'Terrestre'}]},
{"id": 75, "nome": 'Graveler', "pre_evolucao_id": 75, "tipos": [{"nome": 'Pedra'}, {'nome': 'Terrestre'}]},
{"id": 76, "nome": 'Golem', "pre_evolucao_id": 76, "tipos": [{"nome": 'Pedra'}, {'nome': 'Terrestre'}]},
{"id": 77, "nome": 'Ponyta', "pre_evolucao_id": None, "tipos": [{"nome": 'Fogo'}]},
{"id": 78, "nome": 'Rapidash', "pre_evolucao_id": 77, "tipos": [{"nome": 'Fogo'}]},
{"id": 79, "nome": 'Slowpoke', "pre_evolucao_id": None, "tipos": [{"nome": 'Água'}, {'nome': 'Psíquico'}]},
{"id": 80, "nome": 'Slowbro', "pre_evolucao_id": 79, "tipos": [{"nome": 'Água'}, {'nome': 'Psíquico'}]},
{"id": 81, "nome": 'Magnemite', "pre_evolucao_id": None, "tipos": [{"nome": 'Elétrico'}, {'nome': 'Aço'}]},
{"id": 82, "nome": 'Magneton', "pre_evolucao_id": 81, "tipos": [{"nome": 'Elétrico'}, {'nome': 'Aço'}]},
{"id": 83, "nome": "Farfetch'd", "pre_evolucao_id": None, "tipos": [{"nome": 'Normal'}, {'nome': 'Voador'}]},
{"id": 84, "nome": 'Doduo', "pre_evolucao_id": None, "tipos": [{"nome": 'Normal'}, {'nome': 'Voador'}]},
{"id": 85, "nome": 'Dodrio', "pre_evolucao_id": 84, "tipos": [{"nome": 'Normal'}, {'nome': 'Voador'}]},
{"id": 86, "nome": 'Seel', "pre_evolucao_id": None, "tipos": [{"nome": 'Água'}]},
{"id": 87, "nome": 'Dewgong', "pre_evolucao_id": 86, "tipos": [{"nome": 'Água'}, {'nome': 'Gelo'}]},
{"id": 88, "nome": 'Grimer', "pre_evolucao_id": None, "tipos": [{"nome": 'Venenoso'}]},
{"id": 89, "nome": 'Muk', "pre_evolucao_id": 88, "tipos": [{"nome": 'Venenoso'}]},
{"id": 90, "nome": 'Shellder', "pre_evolucao_id": None, "tipos": [{"nome": 'Água'}]},
{"id": 91, "nome": 'Cloyster', "pre_evolucao_id": 90, "tipos": [{"nome": 'Água'}, {'nome': 'Gelo'}]},
{"id": 92, "nome": 'Gastly', "pre_evolucao_id": None, "tipos": [{"nome": 'Fantasma'}, {'nome': 'Venenoso'}]},
{"id": 93, "nome": 'Haunter', "pre_evolucao_id": 92, "tipos": [{"nome": 'Fantasma'}, {'nome': 'Venenoso'}]},
{"id": 94, "nome": 'Gengar', "pre_evolucao_id": 93, "tipos": [{"nome": 'Fantasma'}, {'nome': 'Venenoso'}]},
{"id": 95, "nome": 'Onix', "pre_evolucao_id": None, "tipos": [{"nome": 'Pedra'}, {'nome': 'Terrestre'}]},
{"id": 96, "nome": 'Drowzee', "pre_evolucao_id": None, "tipos": [{"nome": 'Psíquico'}]},
{"id": 97, "nome": 'Hypno', "pre_evolucao_id": 96, "tipos": [{"nome": 'Psíquico'}]},
{"id": 98, "nome": 'Krabby', "pre_evolucao_id": None, "tipos": [{"nome": 'Água'}]},
{"id": 99, "nome": 'Kingler', "pre_evolucao_id": 98, "tipos": [{"nome": 'Água'}]},
{"id": 100, "nome": 'Voltorb', "pre_evolucao_id": None, "tipos": [{"nome": 'Elétrico'}]},
{"id": 101, "nome": 'Electrode', "pre_evolucao_id": 100, "tipos": [{"nome": 'Elétrico'}]},
{"id": 102, "nome": 'Exeggcute', "pre_evolucao_id": None, "tipos": [{"nome": 'Grama'}, {'nome': 'Psíquico'}]},
{"id": 103, "nome": 'Exeggutor', "pre_evolucao_id": 102, "tipos": [{"nome": 'Grama'}, {'nome': 'Psíquico'}]},
{"id": 104, "nome": 'Cubone', "pre_evolucao_id": None, "tipos": [{"nome": 'Terrestre'}]},
{"id": 105, "nome": 'Marowak', "pre_evolucao_id": 104, "tipos": [{"nome": 'Terrestre'}]},
{"id": 106, "nome": 'Hitmonlee', "pre_evolucao_id": None, "tipos": [{"nome": 'Lutador'}]},
{"id": 107, "nome": 'Hitmonchan', "pre_evolucao_id": None, "tipos": [{"nome": 'Lutador'}]},
{"id": 108, "nome": 'Lickitung', "pre_evolucao_id": None, "tipos": [{"nome": 'Normal'}]},
{"id": 109, "nome": 'Koffing', "pre_evolucao_id": None, "tipos": [{"nome": 'Venenoso'}]},
{"id": 110, "nome": 'Weezing', "pre_evolucao_id": 109, "tipos": [{"nome": 'Venenoso'}]},
{"id": 111, "nome": 'Rhyhorn', "pre_evolucao_id": None, "tipos": [{"nome": 'Terrestre'}, {'nome': 'Pedra'}]},
{"id": 112, "nome": 'Rhydon', "pre_evolucao_id": 111, "tipos": [{"nome": 'Terrestre'}, {'nome': 'Pedra'}]},
{"id": 113, "nome": 'Chansey', "pre_evolucao_id": None, "tipos": [{"nome": 'Normal'}]},
{"id": 114, "nome": 'Tangela', "pre_evolucao_id": None, "tipos": [{"nome": 'Grama'}]},
{"id": 115, "nome": 'Kangaskhan', "pre_evolucao_id": None, "tipos": [{"nome": 'Normal'}]},
{"id": 116, "nome": 'Horsea', "pre_evolucao_id": None, "tipos": [{"nome": 'Água'}]},
{"id": 117, "nome": 'Seadra', "pre_evolucao_id": 116, "tipos": [{"nome": 'Água'}]},
{"id": 118, "nome": 'Goldeen', "pre_evolucao_id": None, "tipos": [{"nome": 'Água'}]},
{"id": 119, "nome": 'Seaking', "pre_evolucao_id": 118, "tipos": [{"nome": 'Água'}]},
{"id": 120, "nome": 'Staryu', "pre_evolucao_id": None, "tipos": [{"nome": 'Água'}]},
{"id": 121, "nome": 'Starmie', "pre_evolucao_id": 120, "tipos": [{"nome": 'Água'}, {'nome': 'Psíquico'}]},
{"id": 122, "nome": 'Mr. Mime', "pre_evolucao_id": None, "tipos": [{"nome": 'Psíquico'}, {'nome': 'Fada'}]},
{"id": 123, "nome": 'Scyther', "pre_evolucao_id": None, "tipos": [{"nome": 'Inseto'}, {'nome': 'Voador'}]},
{"id": 124, "nome": 'Jynx', "pre_evolucao_id": None, "tipos": [{"nome": 'Gelo'}, {'nome': 'Psíquico'}]},
{"id": 125, "nome": 'Electabuzz', "pre_evolucao_id": None, "tipos": [{"nome": 'Elétrico'}]},
{"id": 126, "nome": 'Magmar', "pre_evolucao_id": None, "tipos": [{"nome": 'Fogo'}]},
{"id": 127, "nome": 'Pinsir', "pre_evolucao_id": None, "tipos": [{"nome": 'Inseto'}]},
{"id": 128, "nome": 'Tauros', "pre_evolucao_id": None, "tipos": [{"nome": 'Normal'}]},
{"id": 129, "nome": 'Magikarp', "pre_evolucao_id": None, "tipos": [{"nome": 'Água'}]},
{"id": 130, "nome": 'Gyarados', "pre_evolucao_id": 129, "tipos": [{"nome": 'Água'}, {'nome': 'Voador'}]},
{"id": 131, "nome": 'Lapras', "pre_evolucao_id": None, "tipos": [{"nome": 'Água'}, {'nome': 'Gelo'}]},
{"id": 132, "nome": 'Ditto', "pre_evolucao_id": None, "tipos": [{"nome": 'Normal'}]},
{"id": 133, "nome": 'Eevee', "pre_evolucao_id": None, "tipos": [{"nome": 'Normal'}]},
{"id": 134, "nome": 'Vaporeon', "pre_evolucao_id": 133, "tipos": [{"nome": 'Água'}]},
{"id": 135, "nome": 'Jolteon', "pre_evolucao_id": 133, "tipos": [{"nome": 'Elétrico'}]},
{"id": 136, "nome": 'Flareon', "pre_evolucao_id": 133, "tipos": [{"nome": 'Fogo'}]},
{"id": 137, "nome": 'Porygon', "pre_evolucao_id": None, "tipos": [{"nome": 'Normal'}]},
{"id": 138, "nome": 'Omanyte', "pre_evolucao_id": None, "tipos": [{"nome": 'Pedra'}, {'nome': 'Água'}]},
{"id": 139, "nome": 'Omastar', "pre_evolucao_id": 138, "tipos": [{"nome": 'Pedra'}, {'nome': 'Água'}]},
{"id": 140, "nome": 'Kabuto', "pre_evolucao_id": None, "tipos": [{"nome": 'Pedra'}, {'nome': 'Água'}]},
{"id": 141, "nome": 'Kabutops', "pre_evolucao_id": 140, "tipos": [{"nome": 'Pedra'}, {'nome': 'Água'}]},
{"id": 142, "nome": 'Aerodactyl', "pre_evolucao_id": None, "tipos": [{"nome": 'Pedra'}, {'nome': 'Voador'}]},
{"id": 143, "nome": 'Snorlax', "pre_evolucao_id": None, "tipos": [{"nome": 'Normal'}]},
{"id": 144, "nome": 'Articuno', "pre_evolucao_id": None, "tipos": [{"nome": 'Gelo'}, {'nome': 'Voador'}]},
{"id": 145, "nome": 'Zapdos', "pre_evolucao_id": None, "tipos": [{"nome": 'Elétrico'}, {'nome': 'Voador'}]},
{"id": 146, "nome": 'Moltres', "pre_evolucao_id": None, "tipos": [{"nome": 'Fogo'}, {'nome': 'Voador'}]},
{"id": 147, "nome": 'Dratini', "pre_evolucao_id": None, "tipos": [{"nome": 'Dragão'}]},
{"id": 148, "nome": 'Dragonair', "pre_evolucao_id": 147, "tipos": [{"nome": 'Dragão'}]},
{"id": 149, "nome": 'Dragonite', "pre_evolucao_id": 148, "tipos": [{"nome": 'Dragão'}, {'nome': 'Voador'}]},
{"id": 150, "nome": 'Mewtwo', "pre_evolucao_id": None, "tipos": [{"nome": 'Psíquico'}]},
{"id": 151, "nome": 'Mew', "pre_evolucao_id": None, "tipos": [{"nome": 'Psíquico'}]}
]

#popula tabela pokemon e tabela tipo
for pokemon in pokemons:
    if (not session.query(Pokemon).filter(Pokemon.id == pokemon['id']).first()):
        session.add(Pokemon(pokemon['id'], pokemon['nome'], pokemon['pre_evolucao_id']))
    for tipo in pokemon['tipos']:
        if (not session.query(Tipo).filter(Tipo.nome == tipo['nome']).first()):
            session.add(Tipo(tipo['nome']))
session.commit()

#popula tabela pokemon_tipo (relação n-n)
for pokemon in pokemons:
    pkm = session.query(Pokemon).filter(Pokemon.id == pokemon['id']).first()
    for tipo in pokemon['tipos']:
        pkm.tipos.append(session.query(Tipo).filter(Tipo.nome == tipo['nome']).first())
session.commit()

#cria único álbum caso não exista
if (not session.query(Album).filter(Album.id == 1).first()):
    album = Album()
    session.add(album)
    session.commit()
