from prettytable import PrettyTable


class Menu:

    def __init__(self):
        self.board = PrettyTable()
        self.board.field_names = ['Hot Drinks', 'Price']
        self.board.align = 'l'
        self.board.add_rows(
            [
                ["Espresso", "$1.50"],
                ["Latte", "$2.50"],
                ["Cappucino", "$3.00"]
            ]
        )    
    
