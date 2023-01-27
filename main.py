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

# TODO : 1. input("What would you like? (espresso/latte/cappuccino) : show every time action has completed. for serve to the next customer.
# TODO : 2. turn off the coffe machine by entering "off" to the prompt : Maintainers can use "off" as the secret word to turn off the machine
# TODO : 3. print report : when the user enters "report" to the prompt, a report should be generated that shows the current resource values : water, milk, coffee, money
# TODO : 4. check resources sufficient : not enough resources to make something. print : "Sorry there is not enough water(or milk, coffee)."
# TODO : 5. Calculate coins inserted by user. and compare with cost of selected menu. (quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01)

# TODO : 6. not enough money : print "Sorry that's not enough money. Money refunded."
# TODO : 7, enough money : get the money and add profit. and reflected the "report"

# TODO : 8 if user has inserted too much money, the machine should offer change. print "Here is {$2.45} dollars in change." (rounded to 2 decimal places)

# TODO : 9. if All of that are success, tell the user "Here is your {latte}. Enjoy!"