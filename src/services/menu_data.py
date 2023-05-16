from models.dish import Dish
from models.ingredient import Ingredient
import pandas as pd


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.__add_dishes(source_path)

    def __read_csv(self, source_path):
        return pd.read_csv(source_path).itertuples(index=False)

    def __add_dishes(self, source_path):
        for dish in self.__read_csv(source_path):
            self.__create_dish(dish)

    def __create_dish(self, dish):
        name, price, ingredient, amount = dish
        new_dish = Dish(name, float(price))
        if new_dish in self.dishes:
            for item in self.dishes:
                if item.name == name:
                    item.add_ingredient_dependency(
                        Ingredient(ingredient), int(amount)
                    )
        else:
            new_dish.add_ingredient_dependency(
                Ingredient(ingredient), int(amount)
            )
            self.dishes.add(new_dish)
