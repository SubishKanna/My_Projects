from Coffee_Machine_DB import MENU, resources

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
money = 0
ingredients = {}
u_water = 0
u_milk = 0
u_coffee = 0
u_cost = 0

coin_type = [0.25, 0.10, 0.05, 0.01]
u_quarters = 0
u_dimes = 0
u_nickles = 0
u_pennies = 0


def details():
    global ingredients, u_milk, u_coffee, u_water, u_cost
    u_cost = MENU[user_choice]["cost"]
    ingredients = MENU[user_choice]["ingredients"]
    if len(ingredients) == 2:
        u_water = ingredients["water"]
        u_coffee = ingredients["coffee"]
    else:
        u_water = ingredients["water"]
        u_milk = ingredients["milk"]
        u_coffee = ingredients["coffee"]
    check_ingredients()


def coins():
    global u_quarters, u_dimes, u_nickles, u_pennies
    print("Please insert coins")
    u_quarters = int(input("how many quarters? : "))
    u_dimes = int(input("how many dimes? : "))
    u_nickles = int(input("how many nickles? : "))
    u_pennies = int(input("how many pennies? : "))
    check_coins()


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_coins():
    total_coins = (coin_type[0] * u_quarters) + (coin_type[1] * u_dimes) + (coin_type[2] * u_nickles) + (
            coin_type[3] * u_pennies)

    if total_coins < u_cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        global money
        total_coins -= u_cost
        money += u_cost
        print(f"Here is your ${round(total_coins, 2)} in change.")
        print(f"Here is your {user_choice} ☕. Enjoy!")


def check_ingredients():
    if len(ingredients) == 2:
        if resources['water'] >= u_water and resources['coffee'] >= u_coffee:
            coins()
            resources['water'] -= u_water
            resources['coffee'] -= u_coffee
        elif resources['water'] >= u_water:
            print("Sorry there is not enough coffee.")
        elif resources['coffee'] >= u_coffee:
            print("Sorry there is not enough water.")
        else:
            print("Sorry there is not enough coffee and water.")
    else:
        if resources['water'] >= u_water and resources['milk'] >= u_milk and resources['coffee'] >= u_coffee:
            coins()
            resources['water'] -= u_water
            resources['milk'] -= u_milk
            resources['coffee'] -= u_coffee
        elif resources['water'] >= u_water and resources['milk'] >= u_milk:
            print("Sorry there is not enough coffee.")
        elif resources['water'] >= u_water and resources['coffee'] >= u_coffee:
            print("Sorry there is not enough milk.")
        elif resources['milk'] >= u_milk and resources['coffee'] >= u_coffee:
            print("Sorry there is not enough water.")
        elif resources['water'] >= u_water:
            print("Sorry there is not enough milk and coffee.")
        elif resources['milk'] >= u_milk:
            print("Sorry there is not enough water and coffee.")
        elif resources['coffee'] >= u_coffee:
            print("Sorry there is not enough water and milk.")
        else:
            print("Sorry there is not enough water, milk and coffee.")


M = True
while M:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "report":
        report()
    elif user_choice == "off":
        M = False
        print("GoodBye!!")
    elif user_choice == "espresso":
        details()
    elif user_choice == "latte":
        details()
    elif user_choice == "cappuccino":
        details()

    # print("Balance water :", machine['water'])
    # print("Balance milk :", machine['milk'])
    # print("Balance coffee :", machine['coffee'])
