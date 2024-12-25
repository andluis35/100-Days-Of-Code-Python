import random
import hangman_words
import hangman_art

def set_initial_placeholder():
    print(hangman_art.logo)
    placeholder = ""
    for position in range(word_length):
        placeholder += "_"
    print("Word to guess: " + placeholder)

def check_guess():
    display = ""

    if guess in correct_letters:
        print(f"You've already guessed {guess}.")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)
    return display

def update_lives(number_of_lives):
    if guess not in chosen_word:
        number_of_lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    return number_of_lives

def update_game_situation():
    if lives == 0:
        defeat_message()
        return True

    if guessed_all_letters(word_display):
        winning_message()
        return True

def guessed_all_letters(display):
    if "_" not in display:
        return True

def defeat_message():
    print(f"***********************YOU LOSE**********************")
    print(f"The word was: {chosen_word}")

def winning_message():
    print("****************************YOU WIN****************************")

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
game_over = False
correct_letters = []
lives = 6

set_initial_placeholder()

while not game_over:
    print(f"****************************{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    word_display = check_guess()

    lives = update_lives(lives)

    game_over = update_game_situation()

    print(hangman_art.stages[lives])
