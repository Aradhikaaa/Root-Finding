import numpy as np

class methods:
    def __init__(self):
        pass

    def bisection(self,f,x1,x2,tol):

        c = (x1+x2)/2

        n=0
        
        if f(x1)*f(x2) > 0:
           
            print("You have not chosen a valid interval")

        else:
            a = x1
            b = x2
            while abs((b-a)/c) > tol:
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


    def newton(self,f,df,x0,tol):
        delta_x = f(x0)/df(x0)
        n=0
        while abs((delta_x)/x0) > tol:
            n +=1
            x1 = x0 - delta_x
            print("The root is: ", x1)
            delta_x = f(x1)/df(x1)
            x0 = x1
        return n,x0

