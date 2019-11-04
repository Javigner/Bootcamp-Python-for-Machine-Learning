import sys

cookbook= {'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'lunch', 'prep_time': '10'},
          'cake': {'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': '60'},
          'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': '15'}}

def print_recipe(name):
    for element, value in cookbook.items():
        if (element == name):
            print("Recipe for cake:")
            print("Ingredients list: " + str(value['ingredients']))
            print("To be eaten for " + value['meal'] + '.')
            print("Takes " + str(value['prep_time']) + " minutes of cooking.")
    
def delete_recipe(name):
    try:
        cookbook.pop(name)
    except:
        return ('echec')
    
def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = {'ingredients': ingredients, 'meal': meal, 'prep_time': prep_time}
    
def print_name_recipe():
    print("Book's Recipes:")
    for element in cookbook:
        print(element)
while(1):
    print('Please select an option by typing the corresponding number:\n', '1: Add a recipe\n','2: Delete a recipe\n','3: Print a recipe\n','4: Print the cookbook\n','5: Quit')
    #add_recipe('Pad Thai', ['Nouille', 'Poulet', 'cacahuetes'], 'Diner', '30')
    choice = input()
    if choice == '1':
        name = input("Enter recipe name: ")
        ingredients = input("Enter ingredients separate by spaces: ")
        list_ingredients = list(ingredients.split(" "))
        meal = input("For which meal?: ")
        prep_time = input("Enter preparation time: ")
        add_recipe(name, list_ingredients, meal, prep_time)
        print('\nYour recipes has been added to the book\n')
    elif choice == '2':
        name = input("Enter recipe name: ")
        result = delete_recipe(name)
        if (result == 'echec'):
            print("Recipe doesn't exist")
        else:
            print("Recipe deleted\n")
    elif choice == '3':
        name = input("Please enter the recipe's name to get its details: ")
        print_recipe(name)
    elif choice == '4':
        print_name_recipe()
    elif choice == '5':
        print('Cookbook closed.')
        sys.exit()
    else:
        print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")
