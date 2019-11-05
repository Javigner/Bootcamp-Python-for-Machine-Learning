import sys
import datetime

class Book:
    def __init__ (self, name, last_update, creation_date, recipes_list):
        if (isinstance(name, str) == False or name == None):
            sys.exit("Invalid name")
        else:
            self.name = name
        if (isinstance(last_update, datetime.date) == False):
            sys.exit("Invalid datetime for last update")
        else:
            self.last_update
        if (isinstance(creation_date, datetime.date) == False):
            sys.exit("Invalid datetime for creation_date")
        else:
            self.creation_date
        if (isinstance(recipes_list, dict) == True):
            for key, element in recipes_list.items():
                if key != 'starter' and key != 'lunch' and key != 'dessert':
                    sys.exit("Recipe list Keys must be starter, lunch or dessert")