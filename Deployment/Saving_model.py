from sklearn.neighbors import KNeighborsClassifier as KNN 
import numpy as np 

# Load dataset 
from sklearn.datasets import load_iris 
iris = load_iris() 

X = iris.data 
y = iris.target 

# Split dataset into train and test 
X_train, X_test, y_train, y_test = \ 
	train_test_split(X, y, test_size=0.3, 
					random_state=2018) 

# import KNeighborsClassifier model 
knn = KNN(n_neighbors=3) 

# train model 
knn.fit(X_train, y_train) 



#pickle
import pickle 
saved_model = pickle.dumps(knn) 
knn_from_pickle = pickle.loads(saved_model) 
knn_from_pickle.predict(X_test) 


# use joblib

from joblib import Parallel, delayed 
import joblib 
joblib.dump(knn, 'filename.pkl') 
knn_from_joblib = joblib.load('filename.pkl') 
knn_from_joblib.predict(X_test) 
