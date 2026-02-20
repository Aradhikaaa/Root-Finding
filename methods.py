import numpy as np

class methods:
    def __init__(self):
        pass

    def bisection(self,f,x1,x2,tol):

        c = (x1+x2)/2

        n=0
        
        if f(x1)*f(x2) > 0:
           
            print("You have not chosen a valid interval")
            return None, None

        else:
            a = x1
            b = x2
            while abs((b-a)/max(abs(c),1e-16)) > tol:
                n += 1
                c = (a + b)/2

                error = abs((b-a)/max(abs(c),1e-16))

                print("Iter", n, ": interval = [", a, ",", b, "]", ", c =", c,", f(c) =", f(c),", error =", error)

                if f(c) == 0:
                    break
                if f(a)*f(c) < 0:
                    b = c
                else:
                    a = c

        return n,c


    def newton(self,f,df,x0,tol):
        delta_x = f(x0)/df(x0)
        n=0
        while abs((delta_x)/max(abs(x0), 1e-16)) > tol:
            n +=1
            x1 = x0 - delta_x
            error = abs((delta_x)/max(abs(x1), 1e-16))
            print("Iter", n, ": x =", x1, ", f(x) =", f(x1), ", f'(x) =", df(x1),", error =", error)
            delta_x = f(x1)/df(x1)
            x0 = x1
        return n,x0

