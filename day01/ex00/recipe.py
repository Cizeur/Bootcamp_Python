class Recipe:

    """Recipe Class:
Built around 5 mandatory attributes and an optionnal one
mandatory:
    - a non-empty name (str)
    - a cooking level between 1 and 5 (int)
    - a cooking cooking time (positive int)
    - ingredient list (non empty list)
    - recipe_type either starter - lunch - dessert
optionnal:
    - description
exemple of initialisation:
    tourte = Recipe("tourte", 4, ['eggs', 'bacon', 'salt', 'flour'],\
lunch, "Such tasty such lover")"""

    types = ['starter', 'lunch', 'dessert']

    def __error_print(self, msg=""):
        raise Exception(msg)

    def __init__(self, name="", c_level=0, c_time=-1,
                 i_list=[], r_type="Invalid", description=""):
        if not name or not isinstance(name, str):
            self.__error_print("Missing a recipe name as a string")
        if not isinstance(c_level, int) or c_level not in range(1, 6):
            self.__error_print("Cooking level not an int in range 1 - 5")
        if not isinstance(c_time, int) or c_level < 0:
            self.__error_print("Cooking time not a positve int")
        if not i_list or not isinstance(i_list, list):
            self.__error_print("Need a non empty LIST of ingredient")
        if not isinstance(r_type, str) or r_type.lower() not in self.types:
            print("Available types : ", self.types)
            self.__error_print("Invalid type pick one from above")
        if not isinstance(description, str):
            self.__error_print("Invalid type for"
                               "description, should be a string")
        self.name = name.lower()
        self.cooking_level = c_level
        self.cooking_time = c_time
        self.ingredients = i_list
        self.recipe_type = r_type.lower()
        self.description = description

    def __str__(self):
        output = 42 * "#" + "\n"
        output += "Recipe name   : " + self.name.capitalize() + "\n"
        output += "Recipe type   : " + self.recipe_type.capitalize() + "\n"
        output += "Cooking level : " + str(self.cooking_level) + "/5\n"
        output += "Cooking time  : " + str(self.cooking_time) + " minutes\n"
        output += "Ingredients   : " + ", ".join(self.ingredients) + "\n"
        if (self.description):
            output += "Description   : " + self.description + "\n"
        output += 42 * "#"
        return(output)
