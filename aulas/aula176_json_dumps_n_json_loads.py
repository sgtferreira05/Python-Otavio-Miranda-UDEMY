# json.dumps and json.loads with strings + typing.TypedDict
# Converting from Python to JSON:
# Python            JSON
# dict              object
# list, tuple       array
# str               string
# int, float        number
# True              true
# False             false
# None              null  

import json
from pprint import pprint
from typing import TypedDict

class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


string_json = '''
{
    "title": "O Senhor dos Anéis: A sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
}
'''
movie: Movie = json.loads(string_json) #transf para python
# pprint(movie, width=30)
# print(movie['title'])
# print(movie['characters'][0])
# print(movie['characters']) # agora está tipado por causa da class

print(json.dumps(movie, ensure_ascii=False, indent=2)) #voltou a ser json
