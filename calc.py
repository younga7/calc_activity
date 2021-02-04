# CS362 In-Class activity
# Alex Young
# 2/4/2021
# Run this file using python3 calc.py
# This program holds funtions for addition, subtraction, multiplication, and division

def add(x, y):
    try:
        n = x + y
    except TypeError:
        return("Type Error")
    return n

def sub(x, y):
    try:
        n = x - y
    except TypeError:
        return("Type Error")
    return n

def mul(x, y):
    try:
        n = x * y
    except TypeError:
        return("Type Error")
    return n
    
def div(x, y):
    try:
        n = x / y
    except TypeError:
        return("Type Error")
    except ZeroDivisionError:
        return("Zero Division")
    return n