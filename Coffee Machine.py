# Anoushka Saha
# Coffee Machine
# May 11th, 2024
# Day 15 Project

# List of menu items and amount of ingredients required to make them
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

# Ingredients available to use
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Setting sales to 0
sales = 0

# Function to check if there are enough resources to complete order
def enough_resources(order_ing):
    for item in order_ing:
        if order_ing[item] > resources[item]:
            print(f"Sorry, we don't have enough {item} to complete your order")
            return False
    return True

# Function to calculate value of coins inserted
def count_coins():
    print("Please insert coins.")
    total = int(input("How many toonies?: ")) * 2
    total += int(input("How many loonies?: "))
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    return total

# Function to check if user paid enough
def check_pay(pay, price):
    if pay >= price:
        global sales
        sales += price
        change = pay - price
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Insufficient funds. Money refunded")
        return False

# Ask user for their order
while True:
    order = input("What would you like? (espresso/latte/cappuccino): ")

    # Print list of ingredients available if user types report
    if order == "report":
        for key in resources:
            print(str(key) + ": " + str(resources[key]))
    elif order == "off":
        break
    else:
        drink = MENU.get(order)
        if drink:
            if enough_resources(drink["ingredients"]):
                user_pay = count_coins()
                if check_pay(user_pay, drink['cost']):
                    for item in drink["ingredients"]:
                        resources[item] -= drink["ingredients"][item]
                    print(f"Here is your {order}. Enjoy!")
        else:
            print("Sorry, that's not a valid choice. Please try again.")
