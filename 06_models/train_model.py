# Points on joblib 

# 1. Joblib is library that is used to run jobs/programs in parallel
# 2. It can be scaled 
# 3. In machine learning - if we want to use pickle files we can use joblib library 
# 4. The machine learning model can be saved as pickle file using the joblib library.(dump & load)

# how to install joblib - pip install joblib 


import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
#from sklearn.linear_model import LogisticRegression
# 1. Load sample data (Iris flowers)
iris = load_iris()
X, y = iris.data, iris.target

# 2. Train a simple Model
model = LogisticRegression()

model.fit(X, y)

# 3. Save the model to a file
joblib.dump(model, 'my_model_logistic.pkl')
print("Model saved as my_model_logistic.pkl")