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

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True
while is_on:
    users_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if users_choice == "off":
        is_on = False
    elif users_choice == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif users_choice != "espresso" and users_choice != "latte" and users_choice != "cappuccino":
        print("fuck you")
    else:
        drink_info = MENU[users_choice]
        if is_resource_sufficient(drink_info["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink_info["cost"]):
                make_coffee(users_choice, drink_info["ingredients"])





# TODO : 1. input("What would you like? (espresso/latte/cappuccino) : show every time action has completed. for serve to the next customer.
# TODO : 2. turn off the coffe machine by entering "off" to the prompt : Maintainers can use "off" as the secret word to turn off the machine
# TODO : 3. print report : when the user enters "report" to the prompt, a report should be generated that shows the current resource values : water, milk, coffee, money
# TODO : 4. check resources sufficient : not enough resources to make something. print : "Sorry there is not enough water(or milk, coffee)."
# TODO : 5. Calculate coins inserted by user. and compare with cost of selected menu. (quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01)

# TODO : 6. not enough money : print "Sorry that's not enough money. Money refunded."
# TODO : 7, enough money : get the money and add profit. and reflected the "report"

# TODO : 8 if user has inserted too much money, the machine should offer change. print "Here is {$2.45} dollars in change." (rounded to 2 decimal places)

# TODO : 9. if All of that are success, tell the user "Here is your {latte}. Enjoy!"