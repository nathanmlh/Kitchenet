from src.managers.ApiManager import ApiManager

# import sqlite3

if __name__ == "__main__":
    apimanager = ApiManager()
    apimanager.get_key()

    response = apimanager.get_recipes(["apples"])
    json_response = response.json()
    for item in json_response:
        print(item)

    print("----------Taking one recipe----------")

    first_recipe = json_response.pop(0)
    print("This is your first recipe: ")
    print(first_recipe)

    for item in first_recipe:
        print("{} : {}".format(item, first_recipe[item]))
    # for key in json_response.keys():
    #     print("{} : {}".format(key, json_response[key]))