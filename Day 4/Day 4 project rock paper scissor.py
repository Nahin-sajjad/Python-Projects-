import random
user_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
game=["Rock","Paper","Scissors"]
print(f"user choice {game[user_choice]}")

computer_choice = random.randint(0,2)
compiler_choice = game[computer_choice]
print(f"Computer chose {compiler_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")    
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw")
elif user_choice > 2 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:    
    print("You lose")
    
    
        