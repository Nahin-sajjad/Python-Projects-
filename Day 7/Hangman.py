from hangman_art import stages, logo
from hangman_words import word_list
#word_list = ["aardvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list)



display = []
word_length = len(chosen_word)
lives = 6 

print(logo)
print(chosen_word) 
for i in range(word_length):
    display += "_"
print(display)    

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()    
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position]=letter
    print(display)  
    
    if guess not in chosen_word:
        lives-= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
          
    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    print(stages[lives])           
    
