import random
import art
import time

EASY = 1
HARD = 2

def show_header():
    """Prints the game header"""
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("-------------------------------------------")

def set_game_level():
    """Defines the game level"""
    game_level = int(input("Choose a difficulty level:\n[1] Easy\n[2] Hard\nR: "))
    print("-------------------------------------------")
    return game_level

def set_number_of_attempts(game_level):
    """Defines the number of attempts the player will have"""
    if game_level == EASY:
        return 10
    elif game_level == HARD:
        return 5

def clear_screen():
    """Clear the screen"""
    print("\n" * 50)

def winner_message():
    """Prints when the player get the guess right"""
    clear_screen()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("You've got it! Congratulations!!!")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    time.sleep(3)
    clear_screen()

def high_message():
    """Prints when the player takes a high guess"""
    clear_screen()
    print("**********************")
    print("Too high! Guess again.")
    print("**********************")
    time.sleep(3)
    clear_screen()

def low_message():
    """Prints when the player takes a low guess"""
    clear_screen()
    print("**********************")
    print("Too low! Guess again.")
    print("**********************")
    time.sleep(3)
    clear_screen()

def failure_message():
    """Prints when the player got wrong all guesses"""
    clear_screen()
    print("*********************************")
    print("You did not guessed :( Try again!")
    print("*********************************")
    time.sleep(3)
    clear_screen()

def check_guess(user_guess, actual_answer, chances):
    """Verifies if the player got the guess right, returning if he can continue guessing"""
    if user_guess == actual_answer:
        winner_message()
        return False

    elif (user_guess > actual_answer) and (there_are_more_attempts(chances)):
        high_message()
        return True

    elif (user_guess < actual_answer) and (there_are_more_attempts(chances)):
        low_message()
        return True

    else:
        failure_message()
        return False

def there_are_more_attempts(chances):
    """Verifies if there are any more guessing attempts"""
    if chances > 0:
        return True
    else:
        return False

def game():
    """Starts the Number Guessing Game"""
    show_header()
    level = set_game_level()
    should_continue = True
    attempts = set_number_of_attempts(level)
    answer = random.randint(1, 100)

    while should_continue:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        attempts -= 1
        should_continue = check_guess(guess, answer, attempts)

        if not should_continue:
            play_again = input("Do you want to play again?\n[Y] Yes\n[N] No\nR: ")
            if play_again.lower() == "y":
                clear_screen()
                show_header()
                level = set_game_level()
                should_continue = True
                attempts = set_number_of_attempts(level)
                answer = random.randint(1, 100)
            else:
                clear_screen()
                print("======================")
                print("Closing application...")
                print("======================")

game()
