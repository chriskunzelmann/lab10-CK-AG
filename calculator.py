import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a,b)

def add(a,b): return a+b

def subtract(a,b): return a-b

def mul(a,b): return a*b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError
        print("Cannot divide a zero")
    else:
        return b/a

def logarithm(a,b):
    if a<=0 or b<= 0 or a==1 :
        raise ValueError
        print("ValueError")
    else:
        return math.log(a,b)

def exp(a,b): return pow(a,b)