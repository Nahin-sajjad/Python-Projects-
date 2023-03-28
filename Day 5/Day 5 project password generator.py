import random
letters =[chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]
numbers=[str(i) for i in range(10)]
symbols=["!","#","$","%","&","*","(",")","+","="]

print("Welcome to the PyPassword Generator!")	

nr_letters=int(input("How many letters would you like in your password?\n"))
nr_numbers=int(input(f"How many numbers would you like?\n"))
nr_symbols=int(input(f"How many symbols would you like?\n"))

password_list=[]

for char in range(1,nr_letters+1):
    password_list+=random.choice(letters)
for char in range(1,nr_numbers+1):
    password_list+=random.choice(numbers)
for char in range(1,nr_symbols+1):
    password_list+=random.choice(symbols)
random.shuffle(password_list)
for password in password_list:
    print(password,end="")

    