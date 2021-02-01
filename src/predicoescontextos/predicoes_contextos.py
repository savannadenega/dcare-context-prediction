# https://scikit-learn.org/stable/
# https://nirpyresearch.com/partial-least-squares-regression-python/
# https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html
# https://nirpyresearch.com/pls-discriminant-analysis-binary-classification-python/

import numpy as np
import pandas as pd

from scipy.signal import savgol_filter
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import KFold, cross_val_predict, train_test_split
from sklearn.metrics import accuracy_score
from sklearn import metrics
import os
from pathlib import Path
import matplotlib.pyplot as plt

from src.dcaredatasetsimulator.dcare_dataset_simulator_csv import generate_scenarios_to_csv

global pls_binary


def train():
    # Next, we load the data, extract the first and the last label, and do some cleaning and preprocessing steps
    # Load data into a Pandas dataframe
    dirname = Path(__file__).parent.parent
    filepath = os.path.join(dirname, 'db/milk-powder.csv')
    # filepath = os.path.join(dirname, 'db/dataset.csv')
    data = pd.read_csv(filepath)
    # Extract first and last label in a new dataframe
    binary_data = data[(data['labels'] == 5) | (data['labels'] == 6)]
    # Read data into a numpy array and apply simple smoothing
    X_binary = savgol_filter(binary_data.values[:, 2:], 15, polyorder=3, deriv=0)
    # Read categorical variables
    y_binary = binary_data["labels"].values
    # Map variables to 0 and 1
    y_binary = (y_binary == 6).astype('uint8')

    # Now it’s time for the actual PLS decomposition, which is as simple as
    # Define the PLS regression object
    # pls_binary = PLSRegression(n_components=2)
    # Fit and transform the data
    X_pls = pls_binary.fit_transform(X_binary, y_binary)[0]
    return X_binary, y_binary


def pls_da(X_train, y_train, X_test):
    # Define the PLS object for binary classification
    plsda = PLSRegression(n_components=2)

    # Fit the training set
    plsda.fit(X_train, y_train)

    # Binary prediction on the test set, done with thresholding
    binary_prediction = (pls_binary.predict(X_test)[:, 0] > 0.5).astype('uint8')

    return binary_prediction


# Execucao
# generate_scenarios_to_csv(1000)
pls_binary = PLSRegression(n_components=2)
X_binary, y_binary = train()
accuracy = []
cval = KFold(n_splits=10, shuffle=True, random_state=19)
pls_binary.fit(X_binary, y_binary)
y_pred = []
for train, test in cval.split(X_binary):
    y_pred = pls_da(X_binary[train, :], y_binary[train], X_binary[test, :])

    accuracy.append(accuracy_score(y_binary[test], y_pred))
print("Average accuracy on 10 splits: ", np.array(accuracy).mean())

# disp = metrics.plot_confusion_matrix(pls_binary, X_binary, y_binary)
# disp.figure_.suptitle("Confusion Matrix")
# print(f"Confusion matrix:\n{disp.confusion_matrix}")
# plt.show()

# Predicted values
y_pred = ["0", "1", "0", "1", "1"]
# Actual values
y_act = ["1", "1", "0", "1", "1"]
# Printing the confusion matrix
# The columns will show the instances predicted for each label,
# and the rows will show the actual number of instances for each label.
print(metrics.confusion_matrix(y_act, y_pred, labels=["0", "1"]))
# print(metrics.confusion_matrix(y_binary, y_pred, labels=["0", "1"]))
# Printing the precision and recall, among other metrics
print(metrics.classification_report(y_act, y_pred, labels=["0", "1"]))
# print(metrics.classification_report(y_binary, y_pred, labels=["0", "1"]))
