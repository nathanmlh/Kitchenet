from IngredientManager import IngredientManager
import sqlite3

if __name__ == "__main__":
    Manager = IngredientManager()
    print(Manager.db_contents())

    # # Getting ingredients
    # Manager.get_ingredients()
    # print(Manager.ingredients)
    # # Pushing ingredients to database
    # Manager.commit()
    #
    # print(Manager.db_contents())

    Manager.close()