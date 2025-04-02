"""
math_tools.py

A module for basic math operations

Functions:
add(a,b)
subtract(a,b)
multiply(a,b)
divide(a,b)
"""


def add(a,b):
    """returns the sum of two float numbers a and b"""
    return a+b

def substract(a,b):
    """returns the difference of two float numbers a and b"""
    return a-b

def multiply(a,b):
    """returns the product of two float numbers a and b"""
    return a*b

def divide(a,b):
    """returns the quotient of two float numbers a and b"""
    if b == 0:
        return ZeroDivisionError
    else:
        return a/b
    
