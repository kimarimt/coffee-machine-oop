from util import clear


class MoneyHandler:

    def __init__(self, coffee_machine):
        self.coffee_machine = coffee_machine

    def collect_money(self, drink):
        cost = drink['price']

        while True:
            print(f'Your total is: ${cost:.2f}')
            try:
                quarters = int(input('Enter quarters: ')) * 0.25
                dimes = int(input('Enter dimes: ')) * 0.10
                nickels = int(input('Enter nickels: ')) * 0.05
                pennies = int(input('Enter pennies: ')) * 0.01
                amount = quarters + dimes + nickels + pennies

                if amount < drink['price']:
                    clear()
                    print('Sorry not enough money! Please try again')
                    clear(1)
                    continue
                else:
                    change = 0
                    if amount > cost:
                        change = amount - cost

                    self.coffee_machine.profit += cost
                    return change
            except ValueError:
                clear()
                print('Please enter a number for each coin')
                clear(1)
                continue
