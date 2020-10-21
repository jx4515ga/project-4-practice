import nutritionix
import random

def get_drink_info(search_term):
    search_drink = nutritionix.get_drink(search_term)
    print('This is the drink you wanna to see. ')
    print(f'Drink Name: {search_drink}')
    return search_drink