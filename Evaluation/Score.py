
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



# Regression
------------------------------------------------------------------------------

from sklearn.metrics import mean_absolute_error,\ 
    mean_squared_error, mean_absolute_percentage_error 

# MEAN ABSOLUTE ERROR
mae = mean_absolute_error(y_true=Y_test, 
                          y_pred=Y_pred) 


#MEAN SQUARE ERROR
mse = mean_squared_error(y_true=Y_test, 
                         y_pred=Y_pred) 


# ROOT MEAN SQUARE ERROR
Rmse = mean_squared_error(y_true=Y_test, 
                          y_pred=Y_pred, 
                          squared=False) 


# ROOT MEAN ABSOLUTE PERCENTAGE ERROR
mape = mean_absolute_percentage_error(Y_test, 
                                      Y_pred, 
                                      sample_weight=None, 
                                      multioutput='uniform_average')
