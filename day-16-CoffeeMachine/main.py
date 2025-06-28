MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

income = 0.0

def calc_payment(coins):
    total = 0.0
    for coin in coins.keys():
        if coin == "quarters": total += 0.25 * coins[coin]
        if coin == "dimes": total += 0.1 * coins[coin]
        if coin == "nickels": total += 0.05 * coins[coin]
        if coin == "pennies": total += 0.01 * coins[coin]
    return total

def order_drink(drink):
    enough, resource = check_resources(drink)
    if not enough:
        print(f"Sorry there is not enough {resource}.")
    else:
        coins = {"quarters": 0, "dimes": 0, "nickels": 0, "pennies": 0}

        try:
            for coin in coins:
                coins[coin] = int(input(f"Insert {coin}: "))
        except ValueError as e:
            print(f"You must enter a valid integer")

        check_transaction(drink, calc_payment(coins))


def print_report():
    for k in resources.keys():
        measurement = "g" if k == "coffee" else "ml"
        print(f"{k.capitalize()}: {resources[k]}{measurement}")
    print(f"Money: ${"{:.2f}".format(income)}")

def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]

    for k in ingredients.keys():
        if ingredients[k] > resources[k]: return False, k
    return True, None

def check_transaction(drink, payment):
    refund = payment - MENU[drink]["cost"]
    if refund >= 0:
        global income
        income += payment - refund

        if refund > 0:
            print(f"Here is your change: ${"{:.2f}".format(refund)}")
        make_coffee(drink)
    else:
        print("Sorry that's not enough money. Money refunded.")

def make_coffee(drink):
    ingredients = MENU[drink]["ingredients"]

    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]

    print(f"Here is your {drink}. Enjoy!")

def main():
    user_input = ""

    while user_input != "off":
        try:
            user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

            if user_input == "off": continue

            if user_input == "report":
                print_report()
                continue

            if user_input not in MENU:
                raise ValueError(f"{user_input} is an invalid input")

        except ValueError as e:
            print(repr(e))
            continue
        order_drink(user_input)

main()