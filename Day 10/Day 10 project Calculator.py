from art import logo
def add(a1,a2):
    return a1+a2
def subtract(a1,a2):
    return a1-a2
def multiply(a1,a2):
    return a1*a2
def divide(a1,a2):
    return a1/a2
# def exponent(a1,a2):
#     return a1**a2
# def modulo(a1,a2):
#     return a1%a2
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    }
def calculator():
    print(logo)
    num1=float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
    should_continue=True
    while should_continue:
        
        operation_symbol=input("Pick an operation : ")
        num2=float(input("What is the next number? "))
        calculate_function=operations[operation_symbol]
        answer=calculate_function(num1,num2)
        if input(f"Type 'y' to continue calculating with {answer} or Type 'n' to calculate with new numbers.: ")== "y":
            num1=answer
        else:
            should_continue=False
            calculator()    

    

    print(f"{num1} {operation_symbol} {num2} = {answer}")    
calculator()

          