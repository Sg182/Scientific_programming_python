import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import r2_score, mean_squared_error , root_mean_squared_error

np.random.seed(42)

n = 100    #Data size

X1 = np.random.uniform(0,10,n)
X2 = np.random.uniform(-5,5,n)
 

noise = np.random.normal(loc=0,scale=2.0,size=n)    

y = 3*X1 - 2*X2**2 + 5 + noise

#X_quadratic = np.column_stack((X1, X2**2))
X = np.column_stack((X1, X2))


#X = X.reshape(-1, 1)
 
##==========================================EXPERIMENT==================================================
train_r2_values = []
test_r2_values = []

test_sizes = [0.1, 0.2, 0.4, 0.5, 0.7, 0.8, 0.9]

for test_size in test_sizes:

#========== NOW LET US SPLIT THE DATA SET INTO TRAINING AND TEST SET (CROSS VALIDATION USES K-FOLD OF SHUFFLING)=====================#
    X_train, X_test, Y_train, Y_test = train_test_split(X,y,random_state=32,test_size=test_size)
    model = LinearRegression()

    model.fit(X_train,Y_train)

#=========================================================================================#

#NOW TEST THE MODEL ON TRAINING AND TEST SET
    Y_train_predict = model.predict(X_train)
    Y_test_predict = model.predict(X_test)

#=========== NOW EVALUATE MSE and R^2 ===================#

    train_mse = mean_squared_error(Y_train, Y_train_predict)
    test_mse = mean_squared_error(Y_test, Y_test_predict)

    train_r2 = r2_score(Y_train, Y_train_predict)
    test_r2 = r2_score(Y_test, Y_test_predict)

#========================================================#
# STORE VALUES
    train_r2_values.append(train_r2)
    test_r2_values.append(test_r2)

    print(f"=======================================")
    print(f"test size = {test_size}")
    print("Fitted parameters:", model.coef_)
    print("Intercept:", model.intercept_)

    print("Train MSE:", train_mse)
    print("Test MSE:", test_mse)

    print("Train R2:", train_r2)
    print("Test R2:", test_r2)        #(R^2 close to 1 is great)

 

#=================PLOT=====================================

plt.figure()

plt.plot(test_sizes, train_r2_values, marker='o',label="Train_R2")
plt.plot(test_sizes, test_r2_values, marker='o',label="Test_R2")

plt.xlabel("Test_size")
plt.ylabel(r"$R^2$")
plt.legend()
plt.show()
