
from context_prediction import predict
from src.dcaredatasetsimulator.dcare_dataset_simulator import generate_random_scenario_sequence

###############################

'''Generate scenarios'''
# generate_random_scenario_sequence(2)

'''Predict scenarios'''
# predict()

############################### Confusion matrix

# disp = metrics.plot_confusion_matrix(pls_binary, X_binary, y_binary)
# disp.figure_.suptitle("Confusion Matrix")
# print(f"Confusion matrix:\n{disp.confusion_matrix}")
# plt.show()

# Predicted values
# y_pred = ["0", "1", "0", "1", "1"]

# Actual values
# y_act = ["1", "1", "0", "1", "1"]

# Printing the confusion matrix
# The columns will show the instances predicted for each label,
# and the rows will show the actual number of instances for each label.
# print(metrics.confusion_matrix(y_act, y_pred, labels=["0", "1"]))
# print(metrics.confusion_matrix(y_binary, y_pred, labels=["0", "1"]))

# Printing the precision and recall, among other metrics
# print(metrics.classification_report(y_act, y_pred, labels=["0", "1"]))
# print(metrics.classification_report(y_binary, y_pred, labels=["0", "1"]))