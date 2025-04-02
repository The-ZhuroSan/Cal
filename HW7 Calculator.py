import math_tools as mt

print("Welcome to Simple Calculator!")

while True:
    #Input first number
    a = input("Enter a first number (or q to quit): ")
    if a == 'q':
         break
    try:
        a = float(a)
    except ValueError:          #handling errors
        print("Not a valid number, try again")
        continue


    #Input second number
    b = input("Enter a second number (or q to quit): ")
    if b == 'q':
         break
    try:
        b = float(b)
    except ValueError:
        print("Not a valid number, try again")
        continue


    #input operation
    operation = input("Do you want to +add, -subtract, /divide, or *multiply? ")
    if operation == 'q':
        break


    while True:
        if operation == 'add' or operation == '+':
            print('Result: ', mt.add(a,b))
            break
        elif operation == 'substract' or operation == '-':
            print('Result: ', mt.substract(a,b))
            break
        elif operation == 'multiply' or operation == '*':
            print('Result: ', mt.multiply(a,b))
            break
        elif operation == 'divide' or operation == '/':
            print('Result: ', mt.divide(a,b))
            break
        else:
            operation = input("Try again. Do you want to +add, -subtract, /divide, or *multiply? ")


   