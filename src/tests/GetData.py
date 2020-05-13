import json

with open('../data/recipes.json') as f:
  recipes_json = json.load(f)

list_of_recipes = recipes_json["recipe"]

for recipe in list_of_recipes:
    print(recipe["name"])