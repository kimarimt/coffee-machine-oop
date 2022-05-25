from menu import Menu
from money_handler import MoneyHandler
from util import clear


class CoffeeMachine:
    drinks = {
        'espresso': {
            'ingredients': {
                'water': 50,
                'coffee': 18,
            },
            'price': 1.50,
        },
        'latte': {
            'ingredients': {
                'water': 200,
                'coffee': 24,
                'milk': 150.
            },
            'price': 2.50
        },
        'cappuccino': {
            'ingredients': {
                'water': 250,
                'coffee': 24,
                'milk': 100,
            },
            'price': 3.00
        }
    }

    def __init__(self):
        self.money_handler = MoneyHandler(self)
        self.menu = Menu()
        self.ingredients = {
            'water': 300,
            'coffee': 100,
            'milk': 200,
        }
        self.profit = 0

    def check_resources(self):
        print('====== COFFEE MACHINE ======')
        for ingredient, amount in self.ingredients.items():
            unit = 'g' if ingredient == 'milk' else 'ml'
            print(f'\t{ingredient.upper()}: {amount}{unit}')
        print(f'\tPROFIT: ${self.profit:.2f}')
        print('============================')

    def has_enough_resources(self, drink):
        drink_ingredients = drink['ingredients']

        for ingredient, amount in self.ingredients.items():
            if 'milk' not in drink_ingredients:
                continue
            else:
                if drink_ingredients[ingredient] > amount:
                    return False

        return True

    def dispense(self, drink):
        drink_ingredients = drink['ingredients']

        for ingredient in self.ingredients.keys():
            if ingredient not in drink_ingredients:
                continue
            self.ingredients[ingredient] -= drink_ingredients[ingredient]

    def operate(self):
        while True:
            print(f'\n{self.menu.board}\n')

            choice = input('Which drink would you like? ').lower()
            if choice == 'check':
                clear()
                self.check_resources()
                clear(1)
                continue
            elif choice == 'quit':
                clear()
                print('Thanks for using the Python Coffee Machine')
                clear(1)
                break
            elif choice not in self.drinks.keys():
                clear()
                print('Please enter a drink from one of the choices on the menu')
                clear(1)
                continue

            drink = self.drinks[choice]
            clear()

            if self.has_enough_resources(drink):
                change = self.money_handler.collect_money(drink)
                clear(1)

                if change != 0:
                    print(f'Here\'s your change: ${change:.2f}')

                self.dispense(drink)
                print(f'Here\'s your {choice} ☕️. Enjoy!')
                clear(1)
            else:
                clear()
                print('Please check machine for enough resources')
                clear(1)
                continue
