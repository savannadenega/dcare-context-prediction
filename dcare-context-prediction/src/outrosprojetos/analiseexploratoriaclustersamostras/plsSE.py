from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_predict
from scipy.signal import savgol_filter
import numpy as np
import matplotlib
import importlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt 

# Values

Y_calib =  np.loadtxt("moSE.txt",  delimiter='\t')

X = np.loadtxt("matrixSE.txt",  delimiter='\t')


# Define PLS object
pls = PLSRegression(n_components=12, scale = False) #False = meancenter  True = autoscale

# Fit
pls.fit(X, Y_calib)


# Prediction   //aqui estou fazendo a predição das amostras de calibração para avaliar o modelo mas poderia ser amostras de fora => X2
X2 = X  
Y_pred = pls.predict(X2)

print("Y_calib")
print(Y_calib)
print("Y_pred")
print(Y_pred)

Y_valid = Y_calib

score = r2_score(Y_valid, Y_pred)

mse = mean_squared_error(Y_valid, Y_pred)

sep = np.std(Y_pred[:,0] - Y_valid)

rpd = np.std(Y_valid)/sep

#bias = np.mean(Y_pred[:,0]-Y_valid)

#print('R2: %5.5f'  % score)
#print('MSE: %5.5f' % mse)
#print('SEP: %5.5f' % sep)
#print('RPD: %5.5f' % rpd)
#print('Bias: %5.5f' %  bias)

cv = cross_val_predict(pls, X, Y_calib, cv=21)
msecv = mean_squared_error(Y_valid, cv)

rangey = max(Y_valid) - min(Y_valid)
rangex = max(Y_pred) - min(Y_pred)

z = np.polyfit(Y_valid, Y_pred, 1)

with plt.style.context(('ggplot')):
    fig, ax = plt.subplots(figsize=(9, 5))
    plt.xlabel('Predicted')
    plt.ylabel('Measured')
    
    
    ax.scatter(Y_pred, Y_valid, c='red', edgecolors='k')
    ax.plot(z[1]+z[0]*Y_valid, Y_valid, c='blue', linewidth=1)
    #ax.plot(Y_valid, Y_valid, color='green', linewidth=1)
    plt.title('O.M. Prediction')

	# Print the scores on the plot
    plt.text(min(Y_pred)+0.05*rangex, max(Y_valid)-0.1*rangey, 'R$^{2}=$ %5.5f'  % score)
    plt.text(min(Y_pred)+0.05*rangex, max(Y_valid)-0.15*rangey, 'MSE: %5.5f' % mse)
    plt.text(min(Y_pred)+0.05*rangex, max(Y_valid)-0.2*rangey, 'SEP: %5.5f' % sep)
    plt.text(min(Y_pred)+0.05*rangex, max(Y_valid)-0.25*rangey, 'RPD: %5.5f' % rpd)
    plt.text(min(Y_pred)+0.05*rangex, max(Y_valid)-0.3*rangey, 'msecv: %5.5f' %  msecv)
    plt.show()

