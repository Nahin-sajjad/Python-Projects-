print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
combined_name_lowercase=combined_name.lower()
t=combined_name_lowercase.count("t")
r=combined_name_lowercase.count("r")
u=combined_name_lowercase.count("u")
e=combined_name_lowercase.count("e")
true=t+r+u+e
l=combined_name_lowercase.count("l")
o=combined_name_lowercase.count("o")
v=combined_name_lowercase.count("v")
e=combined_name_lowercase.count("e")
love=l+o+v+e
score = int(str(true) + str(love))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")    
    