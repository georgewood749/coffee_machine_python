import menu
import sys

water = menu.resources["water"]
milk = menu.resources["milk"]
coffee = menu.resources["coffee"]
money = 0
coins = [0.01, 0.05, 0.1, 0.25]


def report():
    print(water)
    print(milk)
    print(coffee)
    print(money)


def espresso():
    global water
    global coffee
    water -= 50
    coffee -= 18
    return 1.5  # profit


def latte():
    global water
    global coffee
    global milk
    water -= 200
    coffee -= 24
    milk -= 150
    return 2.5  # profit


def cappuccino():
    global water
    global coffee
    global milk
    water -= 250
    coffee -= 24
    milk -= 100
    return 3  # profit


def check_resources(water_needed, coffee_needed, milk_needed):
    global water
    global coffee
    global milk
    if water >= water_needed\
            and coffee >= coffee_needed\
            and milk >= milk_needed:
        return True
    else:
        return False


def calculate_money(penny, nickel, dime, quarter):
    total = 0
    total += (penny * 0.01)
    total += (nickel * 0.05)
    total += (dime * 0.1)
    total += (quarter * 0.25)
    return "{:.2f}".format(total)


def correct_money(money_given, money_needed):
    if float(money_given) >= float(money_needed):
        change = float(money_given) - float(money_needed)
        return "{:.2f}".format(change)
    else:
        return False


# def calculate_change(money_given, money_needed):
#     if float(money_given) > float(money_needed):
#         return float(money_given) - float(money_needed)


continue_using = True
while continue_using:
    coffee_selected = input("Would you like an espresso, latte or cappuccino?\n").lower()
    if coffee_selected == "off":
        continue_using = False
    if coffee_selected == "report":
        report()
    pennies = float(input("How many pennies?  "))
    nickels = float(input("How many nickels?  "))
    dimes = float(input("How many dimes?  "))
    quarters = float(input("How many quarters?    "))
    total = calculate_money(pennies, nickels, dimes, quarters)
    if coffee_selected == "espresso":
        if check_resources(50, 18, 0) and float(correct_money(total, 1.5)) > 0:
            money += espresso()
            print(f"Here is your change, ${correct_money(total, 1.5)}")
            print("Here is your espresso.")
        elif not correct_money(total, 1.5):
            print("You have not entered the correct change, money refunded")
        else:
            print("There are not enough resources.")
    elif coffee_selected == "latte":
        if check_resources(200, 24, 150) and float(correct_money(total, 2.5)) > 0:
            money += latte()
            print(f"Here is your change, ${correct_money(total, 2.5)}")
            print("Here is your latte.")
        elif not correct_money(total, 2.5):
            print("You have not entered the correct change, money refunded.")
        else:
            print("There are not enough resources.")
    elif coffee_selected == "cappuccino":
        if check_resources(250, 24, 100) and float(correct_money(total, 3)) > 0:
            money += cappuccino()
            print(f"Here is your change, ${correct_money(total, 3)}")
            print("Here is your cappuccino.")
        elif not correct_money(total, 3):
            print("You have not entered the correct change, money refunded.")
        else:
            print("There are not enough resources.")
