# https://scikit-learn.org/stable/
# https://nirpyresearch.com/partial-least-squares-regression-python/
# https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html
# https://drive.google.com/file/d/1Y1iG4qDCuMcNp-aZgUFY5LPdVQeM2XiQ/view

from sys import stdout
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import mean_squared_error, r2_score

# Define PLS object
# TODO ver necessidade 2 parametro
pls = PLSRegression(n_components=5)

# Fit
# TODO adicionar dcaredatasetsimulator gerado pelo gerador de dcaredatasetsimulator
data = pd.read_csv('/dcaredatasetsimulator/peach_spectra_brix.csv')

# Get reference values
# TODO mudar nomes das colunas e linhas para leitura
Y = data['Brix'].values
# Get spectra
X = data.drop(['Brix'], axis=1).values

pls.fit(X, Y)

# Cross-validation
y_cv = cross_val_predict(pls, X, Y, cv=10)

# Calculate scores
# TODO mudar score para retorno em binario
score = r2_score(Y, y_cv)
mse = mean_squared_error(Y, y_cv)

