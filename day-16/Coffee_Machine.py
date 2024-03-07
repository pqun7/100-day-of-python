from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_money_machine = MoneyMachine()
my_menu = Menu()
my_coffeemaker = CoffeeMaker()
loop = True
while loop == True:
    options = my_menu.get_items()
    ask = input(f"What do want {options} ")
    if ask == "report":
        my_coffeemaker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(ask)
        if my_coffeemaker.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                my_coffeemaker.make_coffee(drink)
                  
                    
        