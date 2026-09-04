import numpy as np
import matplotlib.pyplot as plt

 
def lagrange_inter(x, X_in, Y_in):


    P = 0.0   #POLYNOMIAL --> P_n(x) = \sum y_i*L_i

    for i in range(len(X_in)):

        L_i = 1        # LAGRANGE BASIS POLY--> L_i = \prod_j!=i (x - x_j)/(x_i - x_j)

        for j in range(len(X_in)):
            if j != i:
                L_i *= (x - X_in[j])/(X_in[i] - X_in[j])     

        P += Y_in[i]*L_i

    return P


if __name__ == "__main__":

    #DEFINE THE INPUTS

    X_in = np.array([1, 3.8, 2, 1.02, 3.1])
    Y_in = np.array([3,1,0,4.2,3.12])


    x_new = 1.5
    y_new = lagrange_inter(x_new, X_in, Y_in)

    print(f"x = {x_new}")
    print(f"Interpolated y = {y_new}")
