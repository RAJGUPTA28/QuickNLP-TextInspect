

from sklearn.metrics import  accuracy_score, precision_score,\ 
recall_score, f1_score, accuracy_score

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

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


# CROSS VALIDATION SCORE
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)
mean_accuracy = scores.mean()
print("Mean Accuracy:", mean_accuracy)




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
auc = np.round(roc_auc_score(y_true, 
                             y_pred), 3) 



from sklearn.metrics import mean_absolute_error,\ 
    mean_squared_error, mean_absolute_percentage_error 

