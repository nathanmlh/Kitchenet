from IngredientManager import IngredientManager
from ApiManager import ApiManager

# import sqlite3
import json

if __name__ == "__main__":
    apimanager = ApiManager()
    apimanager.get_key()

    # A dictionary of all our jokes
    jokes = {}
    jokes['jokes'] = []

    # Outputting 140 random jokes to our dictionary object
    for i in range(10):
        jokes['jokes'].append(apimanager.joke())

    with open('Jokes.json', 'w') as outfile:
        json.dump(jokes, outfile)