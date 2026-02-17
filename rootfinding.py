import numpy as np
import matplotlib.pyplot as plt

# Defining the function
def func(x):
    return (x**3 - 7* x**2 + 14*x -5)

def dfunc(x):
    return (3*x**2 - 14*x + 14)


# Bisection Method
def bisection(f,x1,x2,tol):

    n=0

    if f(x1)*f(x2) > 0:
        print("You have not chosen a valid interval")

    else:
        a = x1
        b = x2
        while abs(b-a) > tol:
            n += 1
            c = (a + b)/2
            if f(c) == 0:
                print("The root of the function is: ", c)
            if f(a)*f(c) < 0:
                print("The root lies between: ", a, "and", c , "so we continue the search")
                b = c
            else:
                print("The root lies between: ", c, "and", b , "so we continue the search")
                a = c

    return n,c

# Newton Raphson Method
def newton(f,df,x0,tol):
    delta_x = f(x0)/df(x0)
    n=0
    while abs(delta_x) > tol:
        n +=1
        x1 = x0 - delta_x
        print("The root is: ", x1)
        delta_x = f(x1)/df(x1)
        x0 = x1
    return n,x0



def main():
    print("\n Root finding using Bisection Method\n")
    print("Enter you initial guesses for the interval: ")
    x1 = float(input("x1: "))
    x2 = float(input("x2: "))
    tol =10e-8
    n1,r1 = bisection(func,x1,x2,tol)
    print("The root is: ", r1)
    print("Number of iterations: ", n1)

    print("\n Root finding using Newton Raphson Method\n")
    print("Enter you initial guess: ")
    x0 = float(input("x0: "))
    tol =10e-8
    n2,r2 = newton(func,dfunc,x0,tol)
    print("The root is: ", r2)
    print("Number of iterations: ", n2)


main()