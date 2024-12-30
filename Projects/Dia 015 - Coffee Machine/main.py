import art
import time
from coffee_data import resources
from coffee_data import MENU

ESPRESSO = 1
LATTE = 2
CAPPUCCINO = 3
RESOURCES = 4
TURN_OFF = 5

ESPRESSO_PRICE = MENU["espresso"]["cost"]
LATTE_PRICE = MENU["latte"]["cost"]
CAPPUCCINO_PRICE = MENU["cappuccino"]["cost"]

def print_header():
    """Prints the Coffee Machine's header"""
    print(art.logo)

def set_user_choice():
    """Returns the user's choice"""
    return int(input("What would you like?\n"
                   "[1] Espresso\n"
                   "[2] Latte\n"
                   "[3] Cappuccino\n"
                   "[4] Show report\n"
                   "[5] Turn machine off\n"
                   "R: "))

def make_drink(drink):
    """Update the resources by making the drink"""
    print_order_confirmation()
    making_drink_animation(drink)
    update_resources(drink)

def update_resources(drink):
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]

def is_resource_sufficient(drink):
    """Verifies if the resources are sufficient to make the drink"""
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
            return False
    return True

def print_missing_ingredients(drink):
    """Prints the missing ingredients"""
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
            print("----------------------------------------")
            if resources[ingredient] == 0:
                print(f"Sorry, we're out of {ingredient}.")
            else:
                print(f"Sorry, there is not enough {ingredient}.")
            print("----------------------------------------")
    time.sleep(3)

def making_drink_animation(drink):
    """Writes an animation of the drink being made"""
    print("Making drink", end=" ")

    for dot in range(1, 6):
        print(".", end=" ")
        time.sleep(1)

    clear_screen()
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print(f"Here's your {drink}. Enjoy!")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    time.sleep(2)

def ask_for_payment():
    """Returns the total inserted by the user"""
    print("----------------------------------------")
    quarters = int(input("Insert the QUARTERS: "))
    dimes = int(input("Insert the DIMES: "))
    nickles = int(input("Insert the NICKLES?: "))
    pennies = int(input("Insert the PENNIES?: "))
    print("----------------------------------------")
    return calculate_amount_to_pay(quarters, dimes, nickles, pennies)

def calculate_amount_to_pay(quarters, dimes, nickles, pennies):
    """Calculates how much the user paid based on his quantity of each coin"""
    return (0.25 * quarters)  + (0.10 * dimes) + (0.05 * nickles)  + (0.01 * pennies)

def print_refund_message():
    """Prints a refund message when the user insert less coins than the drink price"""
    print("Sorry, that's not enough money. Money refunded.")
    print("----------------------------------------")
    time.sleep(2)
    clear_screen()

def print_order_confirmation():
    """Prints a confirmation message when is everything OK with the order"""
    print("Order accepted. Thank you!")
    print("----------------------------------------")
    time.sleep(2)
    clear_screen()

def give_change(money, drink):
    """Defines the change to be given to the user"""
    if drink == "espresso":
        change = money - ESPRESSO_PRICE
    elif drink == "latte":
        change = money - LATTE_PRICE
    else:
        change = money - CAPPUCCINO_PRICE
    print(f"Here is ${change:.2f} in change.")

def add_money_to_resources(money):
    """Adds the received money to the profit"""
    resources["money"] = money

def make_order(drink, drink_price):
    """Executes the order made by the user"""
    if is_resource_sufficient(drink):
        print_new_tab("payment")
        amount_to_pay = ask_for_payment()

        if amount_to_pay < drink_price:
            print_refund_message()

        elif amount_to_pay == drink_price:
            add_money_to_resources(ESPRESSO_PRICE)
            make_drink(drink)

        else:
            give_change(amount_to_pay, drink)
            add_money_to_resources(drink_price)
            make_drink(drink)
    else:
        print_missing_ingredients(drink)

def print_resources():
    """Shows all the resources available"""
    print_new_tab("resources")
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")
    time.sleep(3)

def print_shutdown_message():
    """Prints a message when the machine is about to be turned off"""
    print_new_tab("shutdown")
    print("+-+-+-+-+-+-+-+")
    print("Turning off...")
    print("+-+-+-+-+-+-+-+")

def clear_screen():
    """Clear the screen by adding 50 empty lines"""
    print("\n" * 50)

def print_new_tab(tab):
    """Prints custom titles based on the current tab"""
    if tab == "payment":
        print(art.payment_tab)
    elif tab == "resources":
        print(art.resources_tab)
    elif tab == "shutdown":
        print(art.shutdown_tab)

def print_invalid_choice():
    """Prints an error message when the user types an unavailable option in the menu"""
    print("------------------------------------------")
    print("You've typed an invalid option. Try again!")
    print("------------------------------------------")
    time.sleep(2)

def turn_coffee_machine_on():
    """Turns the Coffee Machine on"""
    should_continue = True

    while should_continue:
        clear_screen()
        print_header()
        choice = set_user_choice()
        clear_screen()

        if choice == ESPRESSO:
            make_order("espresso", ESPRESSO_PRICE)
        elif choice == LATTE:
            make_order("latte", LATTE_PRICE)
        elif choice == CAPPUCCINO:
            make_order("cappuccino", CAPPUCCINO_PRICE)
        elif choice == RESOURCES:
            print_resources()
        elif choice == TURN_OFF:
            print_shutdown_message()
            should_continue = False
        else:
            print_invalid_choice()

turn_coffee_machine_on()
