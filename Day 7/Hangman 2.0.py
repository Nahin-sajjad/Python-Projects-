from hangman_art import stages, logo
from hangman_words import word_list
import random

def check_guess(guess, chosen_word, display, lives):
    """Check if the guess is correct and update the display and lives."""
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
    return display, lives

# Set up the game
chosen_word = random.choice(word_list)
display = ["_" for _ in range(len(chosen_word))]
lives = 6 

# Start the game
print(logo)
print(chosen_word) 
print(display)    
while True:
    # Get the user's guess
    guess = input("Guess a letter: ").lower()    
    
    # Check the guess and update the display and lives
    display, lives = check_guess(guess, chosen_word, display, lives)
    print(display)  
    
    # Check if the game has ended
    if lives == 0:
        print(stages[lives])
        print("You lose.")
        break
    elif "_" not in display:
        print("You win.")
        break
    else:
        print(stages[lives])