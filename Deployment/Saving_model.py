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




import pickle 
saved_model = pickle.dumps(knn) 
