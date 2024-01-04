
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


from sklearn.metrics import precision_score,\ 
recall_score, f1_score, accuracy_score

# PRECISION
print("Precision:", precision_score(y_test, 
                                    y_pred, 
                                    average="weighted")) 
# RECALL 
print('Recall:', recall_score(y_test, 
                              y_pred, 
                              average="weighted")) 

# F1 SCORE
print('F1 score:', f1_score(y_test, y_pred, 
        			average="weighted")) 


# CONFUSION MATRIX
confusion_matrix = metrics.confusion_matrix(y_test, 
					y_pred) 

cm_display = metrics.ConfusionMatrixDisplay( 
	confusion_matrix=confusion_matrix, 
	display_labels=[0, 1, 2]) 

cm_display.plot() 
plt.show() 


# ROC AUC
from sklearn .metrics import roc_auc_score 


