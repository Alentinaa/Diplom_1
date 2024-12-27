from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_get_available_buns(self):
        database_buns = Database()
        available_buns = database_buns.available_buns()
        assert len(available_buns) == 3

    def test_get_all_available_ingredients(self):
        database_ingredients = Database()
        available_ingredients = database_ingredients.available_ingredients()
        assert len(available_ingredients) == 6

    def test_get_available_sauces_from_ingredients(self):
        database_sauces_ingredients = Database()
        available_sauces_in_ingredients = database_sauces_ingredients.available_ingredients()
        type_sauce = [i for i in available_sauces_in_ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(type_sauce) == 3

    def test_get_available_fillings_from_ingredients(self):
        database_fillings_ingredients = Database()
        available_fillings_in_ingredients = database_fillings_ingredients.available_ingredients()
        type_filling = [i for i in available_fillings_in_ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(type_filling) == 3

