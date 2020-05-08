import spoonacular as sp
import requests

class ApiManager:
    def __init__(self):
        # This is the key we access the api with
        self.key = ""
        self.api = None
        self.active = False

    def __repr__(self):
        return "ApiManager"

    def get_key(self):
        """
        Gets the api key and sets it to active
        :return: None
        """
        self.key = input("Please enter your api key: ")
        self.api = sp.API(self.key)
        self.active = True

    def print_key(self):
        """
        Prints your api key
        :return: None
        """
        print("This is your")

    def activation_failed(self):
        """
        Do this is we need to fail to process
        :return: None
        """
        return "This manager is not active yet. Please input a key."

    def joke(self):
        """
        Gets a random joke
        :return: The joke
        """
        if self.active:
            response = self.api.get_a_random_food_joke()
            data = response.json()
            return data['text']
        else:
            return self.activation_failed()

    def get_recipes(self, ingredients):
        """
        This function returns a list of all recipes you can make
        with the ingredients in your fridge
        :param ingredients: The ingredients we have in our fridge
        :return: A list of all recipes you can make
        """
        if self.active:
            ingredients = ",".join(ingredients)
            payload = {
                'ingredients': ingredients,
                'number': 5,
                'ranking': 1
            }
            endpoint = "https://api.spoonacular.com/recipes/findByIngredients"
            headers = {
                "X-Mashape-Key": self.key,
                "X-Mashape-Host": "mashape host"
            }
            response = requests.get(endpoint, params=payload, headers=headers)
            return response
        else:
            return self.activation_failed()