#Hanan M
#11/29
#Simple Calculator

#Init
#Functions
print("Welcome to Simple Calculator, sponsored by Texas Instruments c.2023")
print("Please choose an operation: (Type in a number between 1 - 6)")
print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Modulus \n6. Quit the Program")
option = int(input("Option: "))
num1 = float(input("What is the first number you'd like to input?: "))
num2 = float(input("What is the second number you'd like to input?: "))

def addition(num1, num2):
    solution = num1 + num2
    return solution
    simpleCalculator() #the idea is for the program to restart continously regardless of operation once its completed

def subtraction(num1, num2):
    solution = num1 - num2
    return solution
    simpleCalculator()

def multiplication(num1, num2):
    solution = num1 * num2
    return solution
    simpleCalculator()

def division(num1, num2):
    solution = num1 / num2
    return solution
    simpleCalculator()
def modulus(num1, num2):
    solution = num1 % num2
    return solution
    simpleCalculator()

def simpleCalculator():
    if option == 1:
        print(addition(num1, num2))
    if option == 2:
        print(subtraction(num1, num2))
    if option == 3:
        print(multiplication(num1, num2))
    if option == 4:
        print(division(num1, num2))
    elif option == 5:
        print(modulus(num1, num2))
    else:
        # or is it elif option == 6? --> still have to figure out how to make quit function works
        quit()
#Notes
#when theres a string you want to put in a new line you use \n
#step 1- use input funtion, dont need a print statement and ask the question
#step 2- put that input in a variable
#step 3- know what you are collecting (string, int, etc)
#quit()- this built in function ends the program at the point it is called
#float is for decimals

#Main
simpleCalculator()