#Calculator
from replit import clear
from art import logo
#Add
def add(n1,n2):
    return n1 + n2

# Substract
def Substract(n1,n2):
    return n1 - n2
    
# Multiply
def Multiply(n1,n2):
    return n1 * n2

# Divide
def Divide(n1,n2):
    return n1 / n2

operation = { 
    "+" : add,
    "-" : Substract,
    "*": Multiply,
    "/": Divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    
    for symbol in operation:
        print(symbol )
    
    want_to_stop = False
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next  number?: "))
    answer = operation[operation_symbol](num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    while not want_to_stop:
        user_input = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
        if user_input == "n":
            want_to_stop = True
            clear()
            calculator()
        else:
            operation_symbol = input("Pick an operation: ")
            num3 = float(input("What's the next number?: "))
            answer = operation[operation_symbol](answer,num3)
            print(f"{answer} {operation_symbol} {num3} = {answer}") 

calculator()