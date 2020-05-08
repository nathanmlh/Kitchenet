from IngredientManager import IngredientManager
from ApiManager import ApiManager

# import sqlite3
import json

if __name__ == "__main__":
    apimanager = ApiManager()
    apimanager.get_key()

    response = apimanager.get_recipes(["apples"]).json()
    print(type(response))
    print(response)
    # for key in response.keys():
    #     print("{} : {}".format(key, response[key]))