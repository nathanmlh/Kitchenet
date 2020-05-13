import sqlite3


class IngredientManager:
    def __init__(self):
        # The ingredients we have inputted
        self.ingredients = {}
        # The filename of the database
        self.filename = "../data/Kitchenet.db"
        # The connection object for the class
        self.conn = sqlite3.connect(self.filename)

    def __repr__(self):
        return "Ingredient Manager: %s" % self.ingredients

    def get_ingredients(self):
        """
        Gets in gredients and adds them to the list of ingredients.
        :return: None
        """
        while True:
            # Get the input
            ingredient = input("Please input an ingredient...new line for exit: ")
            # If it is a blank line...
            if ingredient == "":
                # ...break the loop
                break
            # Getting quantity
            quantity = int(input("Please enter a quantity for your item: "))
            self.ingredients[ingredient] = quantity

    def db_contents(self):
        """
        Returns the database contents as a string
        :return: List object of all contents
        """
        return list(self.conn.execute('''SELECT * FROM Fridge'''))

    def commit(self):
        """
        Pushes all the ingredients we have in the fridge to our database and commits
        :return: None
        """
        for key in self.ingredients.keys():
            self.conn.execute('''INSERT INTO Fridge (Ingredient, Quantity) VALUES (?, ?)''', (key, self.ingredients[key]))
        self.conn.commit()

    def close(self):
        """
        Closes the connection to the database
        :return:
        """
        self.conn.close()