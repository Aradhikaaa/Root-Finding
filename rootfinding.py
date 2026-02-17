import numpy as np
import matplotlib.pyplot as plt

# Defining the function

def func(x):
    return (x**3 - 7* x**2 + 14*x -5)

def dfunc(x):
    return (3*x**2 - 14*x + 14)


# Bisection Method

def bisection(f,x1,x2,tol):

    if f(x1)*f(x2) > 0:
        print("You have not chosen a valid interval")

    else:
        a = x1
        b = x2
        while abs(b-a) > tol:
            c = (a + b)/2
            if f(c) == 0:
                print("The root of the function is: ", c)
            if f(a)*f(c) < 0:
                print("The root lies between: ", a, "and", c , "so we continue the search")
                b = c
            else:
                print("The root lies between: ", c, "and", b , "so we continue the search")
                a = c

    return c

def main():
    print("Enter you initial guesses for the interval: ")
    x1 = float(input("x1: "))
    x2 = float(input("x2: "))
    #tol = float(input("Enter the tolerance: "))
    tol =10e-8
    print("The root is: ", bisection(func,x1,x2,tol))


main()