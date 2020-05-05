import spoonacular as sp

class ApiManager:
    def __init__(self):
        # This is the key we access the api with
        self.key = ""
        self.api = None
        self.active = False

    def __repr__(self):
        return "ApiManager"

    def get_key(self):
        self.key = input("Please enter your api key: ")
        self.api = sp.API(self.key)
        self.active = True

    def activation_failed(self):
        return "This manager is not active yet. Please input a key."

    def joke(self):
        if self.active:
            response = self.api.get_a_random_food_joke()
            data = response.json()
            return data['text']
        else:
            return self.activation_failed()