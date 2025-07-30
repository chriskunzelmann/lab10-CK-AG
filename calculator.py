import math
def add(a, b): 
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b/a

def log(a,b):
    if a==1 or a<=0 or b<=0:
        raise ValueError("Inputs must be positive and base cannot be 1")
    return math.log(b,a)

def exp(a,b):
    return a**b