from IngredientManager import IngredientManager
import sqlite3

if __name__ == "__main__":
    # conn = sqlite3.connect("Kitchenet.db")
    #
    # conn.execute("DELETE FROM Fridge")
    #
    # conn.commit()
    # conn.close()

    manager = IngredientManager()
    print(manager.db_contents())
    manager.close()