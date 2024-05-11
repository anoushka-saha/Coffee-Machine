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

# Ask user for their order
while True:
    order = input("What would you like? (espresso/latte/cappuccino): ")

    # Print list of ingredients available if user types report
    if order == "report":
        for key in resources:
            print(str(key) + ": " + str(resources[key]))
    elif order == "off":
        exit()
    else:
        # Check if resources are sufficient to make the drink
        sufficient_resources = True
        for ingredient in MENU[order]["ingredients"]:
            if resources[ingredient] < MENU[order]["ingredients"][ingredient]:
                print(f"Sorry, there is not enough {ingredient}.")
                sufficient_resources = False
                break

        # If there are sufficient resources, proceed with the order
        if sufficient_resources:
            print("Please insert coins")
            



