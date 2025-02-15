# json.dump and json.load with files
import json
import os

FILE_NAME = 'aula177.json'
ABSOLUTE_PATH_FILE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        FILE_NAME
    )
)
# print(__file__) #arquivo absoluto(sem a extens json)
# print(os.path.dirname(__file__)) #aqui o diretorio sem o nome file
# print(ABSOLUTE_PATH_FILE) #Já com a extensão json

movie = {
    'title': 'O Senhor dos Anéis: A sociedade do Anel', 'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
    'is_movie': True, 
    'imdb_rating': 8.8, 
    'year': 2001, 
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'], 'budget': None
}

with open(ABSOLUTE_PATH_FILE, 'w') as file:
    json.dump(movie, file, ensure_ascii=False)

with open(ABSOLUTE_PATH_FILE, 'r') as file:
    json_s_movie = json.load(file)
    print(json_s_movie)