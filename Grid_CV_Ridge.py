import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import  Ridge
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import sr, train_test_split, KFold,GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_absolute_error, root_mean_squared_error


np.random.seed(42)

n = 100    #Data size

X1 = np.random.uniform(0,10,n)
X2 = np.random.uniform(-5,5,n)
 

noise = np.random.normal(loc=0,scale=2.0,size=n)    

y = 3*X1 - 2*X2**2 + 5 + noise

#X_quadratic = np.column_stack((X1, X2**2))
X = np.column_stack((X1, X2))


#=================================RESERVING TEST SET=================================================
X_train, X_test, y_train, y_test = train_test_split( X,y,test_size=0.2,random_state=42)
print("Training size:", X_train.shape)
print("Final test size:", X_test.shape)

#================================LET US DEFINE 5-FOLD CV==============================================

kf = KFold(n_splits=5,shuffle=True,random_state=42)

# =========================================================
# 3. DEFINE THE ML PIPELINE
# =========================================================

pipeline = Pipeline([
    ("poly", PolynomialFeatures(include_bias=False)),
    ("scale", StandardScaler()),
    ("ridge", Ridge())
])


# =========================================================
# 4. DEFINE HYPERPARAMETER GRID
# =========================================================

param_grid = {

    "poly__degree": [1, 2, 3, 4, 5],
     "ridge__alpha": [0.001, 0.01, 0.1,1.0,10.0,100.0]
}
 
#=============================DO GRID_SEARCH_CV================================
# GRID SEARCH CV EXHAUSTIVELY TESTS EVERY COMBINATION OF THE
# SPECIFIED HYPERPARAMETER VALUES USING CROSS-VALIDATION AND
# SELECTS THE COMBINATION THAT GIVES THE BEST VALIDATION SCORE.
# IN OTHER WORDS, IT EXPLORES ALL PERMUTATIONS/COMBINATIONS
# DEFINED BY THE USER'S HYPERPARAMETER GRID.


grid = GridSearchCV(estimator=pipeline, param_grid=param_grid,cv=kf,scoring="neg_root_mean_squared_error",return_train_score=True)

grid.fit(X_train, y_train)      #PERFORM THE SEARCH USING TRAINING DATA

#=====================PRINT THE BEST HYPERPARAMETERS================================
print("\nGrid Search CV completed.")
print("\nBest hyperparameters: ")
print(grid.best_params_)

print("\nBest mean CV RMSE: ")
print(-grid.best_score_)


#===================================FINAL MODEL===============================

final_model = grid.best_estimator_     #FITS THE MODEL WITH THE BEST HYPERPARAMETERS

y_test_pred = final_model.predict(X_test)

final_rmse = root_mean_squared_error(y_test_pred,y_test)
final_r2 = r2_score(y_test, y_test_pred)

print("\nFINAL TEST RMSE:", final_rmse)
print("\nFINAL TEST R2:", final_r2)