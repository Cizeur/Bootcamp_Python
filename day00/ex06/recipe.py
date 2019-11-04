

def new_recipe(cookbook:dict={}, name:str="" ,ingredients:list = ["love"], meal:str = ["anytime"], prep_time:int=42):
    if not name:
        return
    recipe = {"ingredients":ingredients, "meal":meal, "prep_time":prep_time}
    cookbook[name] = recipe

def print_recipe(cookbook:dict, name:str):
    name = name.lower()
    if not name:
        return
    print("{:#>42.42}".format(""))
    if name in cookbook.keys():
        print ("Recipe for " + name)
        print ("Ingredients list: ", cookbook[name]["ingredients"])
        print ("To be eaten for " + cookbook[name]["meal"] +".")
        if cookbook[name]["prep_time"] == 1:
            print("Takes 1 minute of cooking.")
        else:
            print("Takes {} minutes of cooking.".format(cookbook[name]["prep_time"]))
    else:
        print("No recipes under that name")
    print("{:#>42.42}".format(""))

def remove_recipe(cookbook:dict, name:str):
    name = name.lower()
    if not name:
        return
    print ("")
    print("{:#>42.42}".format(""))
    if name in cookbook.keys():
        cookbook.pop(name)
        print("Recipe " + name + " removed")
    else:
        print("No recipes under that name")
    print("{:#>42.42}".format(""))
    print ("")

def add_recipe(cookbook:dict, name:str):
    name = name.lower()
    if not name:
        return
    print ("")
    print("{:#>42.42}".format(""))
    if name in cookbook.keys():
        print("Already a recipe of that name please remove it first")
    else:
        ingredients=[]
        while not len(ingredients):
            ingredients = input("Enter ingredients separated with comma[,] at least one : ").lower()
            ingredients = list(map(str.strip,ingredients.split(",")))
            while("" in ingredients) : 
                ingredients.remove("")
        meal_type=""
        while not meal_type:
            meal_type = input("Enter the type of meal [starter, lunch, dessert, etc...] : ").lower()
        while 1:
            try:
                prep_time = int(input("Enter prep time in minutes [int] : "))   
                break
            except ValueError:
                print("Int, please.")
        new_recipe(cookbook, name, ingredients, meal_type, prep_time)
        print("Recipe added")
        print("")
        print_recipe(cookbook, name)
        print("")
    print("{:#>42.42}".format(""))
    print ("")


cookbook = {}
new_recipe(cookbook, "sandwich",
                        ["ham", "bread", "cheese", "tomatoes"] ,
                        "lunch", 10)
new_recipe(cookbook, "cake",
                        ["flour", "sugar", "eggs"] ,
                        "dessert", 60)
new_recipe(cookbook, "salad",
                        ["avocado", "arugula", "tomatoes", "spinach"] ,
                        "lunch", 15)

while 1:
    print("""Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit""")
    inval = input(">> ")
    if inval == "1":
        print("Please enter the recipe's name you wish to add:")
        inval = input(">> ")
        add_recipe(cookbook, inval)
    elif inval == "2":
        print("Please enter the recipe's name you wish to remove:")
        inval = input(">> ")
        remove_recipe(cookbook, inval)
    elif inval == "3":
        print("Please enter the recipe's name to get its details:")
        inval = input(">> ")
        print ("")
        print_recipe(cookbook, inval)
        print ("")
    elif inval == "4":
        print ("")
        for key in sorted(cookbook.keys()):
            print_recipe(cookbook, key)
        print ("")
    elif inval == "5":
        print("Cookbook closed.")
        break
    else:
        print("\n{:#>42.42}".format(""))
        print("""This option does not exist, please type the corresponding number.
To exit, enter 5.""")
        print("{:#>42.42}\n".format(""))
