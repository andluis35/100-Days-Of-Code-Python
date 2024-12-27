import random
import art
import time

def set_user_initial_cards():
    """Sets the user's two initial cards of the game"""
    set_one_card(user_cards)
    set_one_card(user_cards)

def set_computer_initial_cards():
    """Sets the computer's two initial cards of the game"""
    set_one_card(computer_cards)
    set_one_card(computer_cards)

def check_initial_blackjack():
    """Checks for a blackjack in the starting game"""
    if computer_score == 21:
        report_final_scoreboard()
        print("\n************************************")
        print("COMPUTER HAS A BLACKJACK. IT WINS!!!")
        print("************************************")
        make_count()
        clear_screen()
        return False

    elif user_score == 21 and computer_score < 21:
        report_final_scoreboard()
        print("\n********************************")
        print("YOU HAVE A BLACKJACK. YOU WIN!!!")
        print("********************************")
        make_count()
        clear_screen()
        return False

    else:
        return True

def set_one_card(list_of_cards):
    """Add a random card from the deck in the list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    list_of_cards.append(random_card)

def report_partial_scoreboard():
    """Prints the partial game scoreboard"""
    print("----------------------------------")
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    print("----------------------------------")

def update_score(list_of_cards):
    """Updates the list's score"""
    return sum(list_of_cards)

def report_final_scoreboard():
    """Prints the final game scoreboard"""
    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

def define_winner():
    """Prints who won the game"""
    print("\n**************************")
    if user_score > computer_score:
        print("--- YOU WIN!!! ---")
    elif user_score < computer_score:
        print("--- COMPUTER WINS!!! ---")
    else:
        print("--- DRAW!!! ---")
    print("**************************")

def make_count():
    """Prints a count from 5 to 1"""
    print("\n")
    for i in range(5, 0, -1):
        print(f"[ {i} ]", end=" ")
        time.sleep(1)

def let_computer_play(c_score):
    """Allows computer to add cards to its deck"""
    while c_score < 16:
        set_one_card(computer_cards)
        c_score = update_score(computer_cards)
    return c_score

def clear_screen():
    """Clear the terminal"""
    print("\n" * 50)


user_score = 0
computer_score = 0
should_continue = True

print(art.logo)
play = int(input("Press [1] to start the game.\n"))

while play == 1:
    clear_screen()
    print(art.logo)

    user_cards = []
    computer_cards = []
    set_user_initial_cards()
    set_computer_initial_cards()
    user_score = update_score(user_cards)
    computer_score = update_score(computer_cards)

    should_continue = check_initial_blackjack()

    while should_continue:
        report_partial_scoreboard()

        if user_score <= 21:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if get_another_card == "y":
                set_one_card(user_cards)
                user_score = update_score(user_cards)
            else:
                clear_screen()
                computer_score = let_computer_play(computer_score)
                report_final_scoreboard()

                if computer_score > 21:
                    print("\n******************************")
                    print("Computer went over. YOU WIN!!!")
                    print("******************************")
                else:
                    define_winner()

                make_count()
                clear_screen()
                should_continue = False

        else:
            clear_screen()
            report_final_scoreboard()
            print("\n**************************")
            print("You went over. YOU LOSE!!!")
            print("**************************")
            should_continue = False
            make_count()
            clear_screen()

    play = int(input("Do you want to play again?\n[1] Yes\n[2] No\nR: "))
    if play == 1:
        should_continue = True
    else:
        clear_screen()
        print("======================")
        print("Closing application...")
        print("======================")
