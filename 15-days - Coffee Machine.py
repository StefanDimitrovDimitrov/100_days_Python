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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def available_resources(drink):
    result = "yes"
    drink_resources = MENU[drink]["ingredients"]

    for item in drink_resources:
        if drink_resources[item] > resources[item]:
            result = item

    return result


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


def withdrew_resources(drink):
    list_ingredients = MENU[drink]["ingredients"]

    for ingredient in list_ingredients:
        withdraw_resources = list_ingredients[ingredient]
        current_resources = resources[ingredient]
        current_resources -= withdraw_resources


def shows_the_resources(resources_in_machine, current_profit):
    result = f"Water: {resources_in_machine['water']}\n" \
             f"Milk: {resources_in_machine['milk']}\n" \
             f"Coffee: {resources_in_machine['coffee']}\n" \
             f"Money: ${current_profit}"
    return result


print("You can order from the Coffee Machine named Fernando: Espresso: $1.50, Latte: $2.50, Cappuccino: $3.0")

order = ''

while order != "off":
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "espresso" or order == "latte" or order == "cappuccino":
        if available_resources(order) == "yes":
            user_coins = insert_coins()
            cost_product = MENU[order]["cost"]
            if user_coins >= cost_product:
                profit += cost_product
                withdrew_resources(order)
                print(f"Here is ${(current_coins - cost_product):.2f} in change.")
                print(f"Here is your {order} \N{hot beverage} Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
                print(f"You need {cost_product - current_coins} to order the product")
                continue
        else:
            print(f"Sorry there is not enough {available_resources(order)}.")
    elif order == "report":
        print(shows_the_resources(resources, profit))
        continue
    elif order == "off":
        print("The machine is currently not available.")
        break
    else:
        print("Please choice between espresso/latte/cappuccino!!!")
        continue
