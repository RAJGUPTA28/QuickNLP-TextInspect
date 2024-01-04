
from sklearn.metrics import accuracy_score
# Make predictions on the test set
y_pred = model.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)



from sklearn.model_selection import cross_val_score
# Perform cross-validation
scores = cross_val_score(model, X, y, cv=5)
# Calculate the average performance across all folds
mean_accuracy = scores.mean()
print("Mean Accuracy:", mean_accuracy)
