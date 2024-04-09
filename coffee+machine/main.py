"""
Coffee Machine Simulator

This script simulates the operation of a coffee machine. Users can select a beverage (espresso, latte, or cappuccino),
view a report of available resources, or turn off the machine.

Dependencies:
    - menu: A module containing the menu of available beverages and their ingredients.
    - resources: A dictionary containing the initial resources of the coffee machine.

Usage:
    Run this script to start the Coffee Machine Simulator by: >> python3 main.py
    Follow the prompts to choose a beverage, view a resources report, or turn off the machine.

"""

from menu import MENU, resources

process = True

# printing a resources report
def print_report():
    print("\n---REPORT---")
    print(f"---Water:  {resources['water']} ml")
    print(f"---Milk:   {resources['milk']} ml")
    print(f"---Coffee: {resources['coffee']} g")
    print(f"---Money:  {resources['money']} $")

# check if we have enought resources for making a beverage
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False 
    return True           

def make_beverage(beverage):
    item =  MENU[beverage]['ingredients']
    for i in item:
        resources[i] -= item[i]
    print(f"Here is your {beverage}. Enjoy!")

def pay(beverage):
    price =  MENU[beverage]['cost']
    print(f"You choose {beverage}, the price is {price}")
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    print(f"You've given: {total}")
    if total < price:
        print("Sorry that's not enough money. Money refunded.")
        return 'NO'
    else:
        change = total - price
        resources['money'] += price
        print("Here is {:.2f} in change.".format(change))
        return 'OK'

# Process Loop
while process:
    user_answer = input("\nWhat would you like? (espresso/latte/capuccino): ")
    if user_answer == 'report':
        print_report()
    elif user_answer == 'off':
        print("\nSwitching off the coffee machine...")
        process = False
    else:
        if is_resource_sufficient(MENU[user_answer]['ingredients']) and pay(user_answer) == 'OK':
            make_beverage(user_answer)