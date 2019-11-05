import sys

class Recipe:
    def __init__(self, name, cooking_level, cooking_time, ingredients, recipe_type, description=""):
        if (isinstance(name, str) == False or name == None):
            sys.exit("Invalid name")
        else:
            self.name = name
        if (isinstance(cooking_level, int) == False or cooking_level == None):
            sys.exit("Cooking level must be numeric")
        elif(cooking_level < 1 or cooking_level > 5):
            sys.exit("Cooking level must be a number between 1 and 5")
        else:
            self.cooking_level = int(cooking_level)
        if (isinstance(cooking_time, int) == False or cooking_time == None):
            sys.exit("Cooking time must be numeric")
        elif(cooking_time < 0):
            sys.exit("Cooking time must be a positive number")
        else:
            self.cooking_time = int(cooking_time)
        if (isinstance(ingredients, list) == False or ingredients == None):
            for element in ingredients:
                if (isinstance(element, str) == False):
                    sys.exit("Each ingredients must be a string")
            sys.exit("Ingredients must be a List")
        else:
            self.ingredients = ingredients
        if (isinstance(description, str) == False):
            sys.exit("Description muste be a String")
        else:
            self.description = description
        if (recipe_type == 'lunch' or recipe_type == 'starter' or recipe_type == 'dessert'):
            self.recipe_type = recipe_type
        else:    
            sys.exit("Recype type must be a lunch, starter or dessert")
           
    def __str__(self):
        txt = "Recipe of the " + self.name + ' :\n' + 'Cooking level: ' + str(self.cooking_level) + '\n' + 'Cooking time: ' + str(self.cooking_time) + ' minutes' + '\n' + "List des ingredients: " + str(self.ingredients) + '\n' + self.description + '\n' + 'Recipe type: ' + self.recipe_type
        return txt