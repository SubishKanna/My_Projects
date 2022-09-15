from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
order = True

while order:
    user_choice = input(f"Enter your choice {menu.get_items()} : ")

    if user_choice == "off":
        order = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)