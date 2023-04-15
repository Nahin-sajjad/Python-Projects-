from random import randint
from art import logo 
#Number Guessing Game Objectives:
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
# Include an ASCII art logo.
print(logo)
# Allow the player to submit a guess for a number between 1 and 100.
# Track the number of turns and reduce by 1 if they get it wrong.

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
def check_answer(guess,answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else :
        print("You got it! The answer was {}.".format(answer))
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,101)
    print(f"Pssst, the correct answer is {answer}")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print("You have {} attempts remaining to guess the number.".format(turns))
        guess = int(input("Make a guess: "))
        check_answer(guess,answer)
        turns-=1
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()        