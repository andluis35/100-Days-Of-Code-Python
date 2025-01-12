import art
import game_data
import random
import time

FIRST_WINS = 1
SECOND_WINS = 2
DRAW = 0

def print_header(scoreboard):
      """Prints the game's header"""
      print(art.logo)
      print(f"SCORE: {scoreboard}")
      print("------------------------------------------")

def print_duel(first_acc, second_acc):
      """Prints the duel between the two accounts"""
      print_account(first_acc, 1)
      print(art.vs)
      print_account(second_acc, 2)

def print_account(account, position):
      """Prints the account at the given index"""
      print(f"[{position}] {account["name"]}, "
            f"a {account["description"]}, "
            f"from {account["country"]}")

def define_winner_account(first_acc, second_acc):
      """Define which account has more followers"""
      if first_acc["follower_count"] > second_acc["follower_count"]:
            return FIRST_WINS
      elif first_acc["follower_count"] < second_acc["follower_count"]:
            return SECOND_WINS
      else:
            return DRAW

def set_player_guess():
      """Returns the player's guess"""
      print("------------------------------------------")
      return int(input("Who has more followers? Type '1' or '2': "))

def clear_screen():
      """Clear the screen"""
      print("\n" * 50)

def print_correct_answer_message():
      """Prints a message when the player guesses correctly"""
      clear_screen()
      print("**********************")
      print("You're right! +1 point")
      print("**********************")
      time.sleep(2)
      clear_screen()

def print_defeat_message(first_acc, second_acc, scoreboard):
      """Prints a message when the player loses the game"""
      print("**********************************************************")
      print("Wrong answer :( You LOSE!")
      print(f"\n→ {first_acc["name"]} has {first_acc["follower_count"]} million followers.")
      print(f"→ {second_acc["name"]} has {second_acc["follower_count"]} million followers.")
      print(f"\nFINAL SCORE: {scoreboard}")
      print("**********************************************************")

def player_got_right(guess, winner_acc):
      """Returns True if the player guessed correctly"""
      return guess == winner_acc

def first_account_won(winner_acc):
      """Returns True if the first account has more followers"""
      return winner_acc == FIRST_WINS

def second_account_won(winner_acc):
      """Returns True if the second account has more followers"""
      return winner_acc == SECOND_WINS

def start_game():
      """Gets the Higher or Lower Game started"""
      accounts_list = game_data.data
      score = 0
      should_continue = True

      print_header(score)

      first_account = random.choice(accounts_list)
      second_account = random.choice(accounts_list)

      while should_continue:
            print_duel(first_account, second_account)
            winner_account = define_winner_account(first_account, second_account)
            choice = set_player_guess()

            if player_got_right(choice, winner_account):
                  print_correct_answer_message()
                  score += 1
                  clear_screen()
                  print_header(score)

                  if first_account_won(winner_account):
                        accounts_list.remove(second_account)
                        second_account = random.choice(accounts_list)

                  elif second_account_won(winner_account):
                        accounts_list.remove(first_account)
                        first_account = second_account
                        second_account = random.choice(accounts_list)

            else:
                  clear_screen()
                  print_defeat_message(first_account, second_account, score)
                  should_continue = False

start_game()
