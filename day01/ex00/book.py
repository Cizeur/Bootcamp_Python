import datetime
from recipe import Recipe


class Book:
    """
Book of recipes class:
created from a single attribute:
    -name of the cookbook
it stores:
    - name (str)
    - last_update ([datetime])
    - creation_date ([datetime])
    - recipes_list (dict) : a dictionnary \
with 3 keys: "starter", "lunch", "dessert".
methods :
    def get_recipe_by_name(self, name):
        Print a recipe with the name `name` \
and return the instance
    def get_recipes_by_types(self, recipe_type):
        Get all recipe names for a given recipe_type
    def add_recipe(self, recipe):
        Add a recipe to the book and update last_update
"""
    recipes_list = {"starter": {}, "lunch": {}, "dessert": {}}

    def __error_print(self, msg=""):
        raise Exception(msg)

    def __init__(self, name=""):
        if not name or not isinstance(name, str):
            self.__error_print("Missing a book name as a string")
        name = name.lower()
        self.creation_date = datetime.datetime.now()
        self.last_update = self.creation_date
        self.name = name.lower()

    def add_recipe(self, recipe=""):
        if not isinstance(recipe, Recipe):
            self.__error_print("Element added should be a Recipe")
        r_type = recipe.recipe_type
        for dic in self.recipes_list.values():
            if recipe.name in dic.keys():
                self.__error_print("Already a recipe of that name")
        self.recipes_list[r_type][recipe.name] = recipe
        self.last_update = datetime.datetime.now()

    def remove_recipe_by_name(self, name=""):
        if not name or not isinstance(name, str):
            self.__error_print("Need a recipe name")
        name = name.lower()
        for rtype, dic in self.recipes_list.items():
            if name in dic.keys():
                self.recipes_list[rtype].pop(name)
        self.last_update = datetime.datetime.now()

    def get_recipe_by_name(self, name=""):
        if not name or not isinstance(name, str):
            self.__error_print("Need a recipe name")
        name = name.lower()
        for rtype, dic in self.recipes_list.items():
            if name in dic.keys():
                return self.recipes_list[rtype][name]
        self.__error_print("No Recipes of that name")

    def get_recipe_by_types(self, recipe_type=""):
        if not recipe_type or not isinstance(recipe_type, str):
            self.__error_print("Need a recipe type")
        recipe_type = recipe_type.lower()
        if recipe_type not in self.recipes_list.keys():
            self.__error_print("Invalid recipe type")
        return list(self.recipes_list[recipe_type].keys())
