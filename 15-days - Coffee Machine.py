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


def is_available_resources(drink):
    drink_resources = MENU[drink]["ingredients"]
    for item in drink_resources:
        if drink_resources[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def insert_coins():
    print("Please insert coins? ")
    quarters = int(input("how many quarters?: "))
    total_q = quarters * 0.25
    dimes = int(input("how many dimes?: "))
    total_d = dimes * 0.10
    nickles = int(input("how many nickles?: "))
    total_n = nickles * 0.05
    pennies = int(input("how many pennies?: "))
    total_p = pennies * 0.01
    total = total_d + total_q + total_n + total_p
    return total


def if_enough_coins(user_coins, cost):
    if user_coins >= cost:
        print(f"Here is ${(user_coins - cost):.2f} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        print(f"You need {cost - user_coins} to order the product")
        return False


def make_coffee(drink):
    global profit
    profit += drink_cost
    withdrew_resources(drink)

    print(f"Here is your {drink} \N{hot beverage} Enjoy!")


def withdrew_resources(drink):
    list_ingredients = MENU[drink]["ingredients"]

    for ingredient in list_ingredients:
        withdraw_resources = list_ingredients[ingredient]
        resources[ingredient] -= withdraw_resources


def shows_the_resources(resources_in_machine, current_profit):
    result = f"Water: {resources_in_machine['water']}\n" \
             f"Milk: {resources_in_machine['milk']}\n" \
             f"Coffee: {resources_in_machine['coffee']}\n" \
             f"Money: ${current_profit}"
    return result


profit = 0
order = ''

while order != "off":
    print("You can order from the Coffee Machine named Fernando: Espresso: $1.50, Latte: $2.50, Cappuccino: $3.0")
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "espresso" or order == "latte" or order == "cappuccino":
        drink_cost = MENU[order]["cost"]
        if is_available_resources(order):
            if if_enough_coins(insert_coins(), drink_cost):
                make_coffee(order)
    elif order == "report":
        print(shows_the_resources(resources, profit))
    elif order == "off":
        print("The machine is currently not available.")
        break
    else:
        print("Please choice between espresso/latte/cappuccino!!!")
