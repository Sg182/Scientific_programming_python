import math


def Regula_Falsi(func,a,b,tol=1e-8,maxiter=1000):
    '''Here we will write a code for obtaining roots for a function f(x) = 0.
    
    f(x) is assumed to be continuous in the interval (a,b), and if f(a)f(b)<0,
    then there exist a root k in (a,b), such that f(k)=0.
    
    '''

    if (func(a)*func(b) >= 0):
        raise ValueError("The function interval is not stable! F must have different signs.")
    
    print("=========================================")
    print(" ITER  |      c       |     f(x)      |")
    print("=========================================")

    for i in range(1, maxiter+1):
        c = (a*func(b) - b*func(a))/(func(b)-func(a))
        fun_c = func(c)
        
        print(f"{i:4d}  {c:9.8f}    {fun_c:10.8f}")

        if abs(func(c)) < tol:
            return i-1 , c
        
        if func(c)*func(a) < 0:
            b = c
        else:
            a = c

    raise RuntimeError("Regula-Falsi did not Converge!")

def func(x):
    return math.exp(-x) * math.cos(2 * math.pi * x) - 0.5 * x + math.sin(x**2)



N , root = Regula_Falsi(func, 0,1.5, tol=1e-9)

print(func(2))
print("Regula-Falsi converged in ", N, " iterations.")
print(f"The root is {root:10.8f}")
        
         
    



