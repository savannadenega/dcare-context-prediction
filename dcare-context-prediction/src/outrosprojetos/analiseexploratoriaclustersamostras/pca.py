import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.signal import savgol_filter
from sklearn.decomposition import PCA as sk_pca
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.cluster import KMeans

# Values
wave = np.loadtxt("waveSE.txt",  delimiter='\t')

Y_calib = np.loadtxt("moSE.txt",  delimiter='\t')

X_calib = np.loadtxt("matrixSE.txt",  delimiter='\t')

skpca2 = sk_pca(n_components=20)

#dfeat = savgol_filter(X_calib.T, 15, polyorder = 2, deriv=1)
#
with plt.style.context(('ggplot')):
    plt.plot(wave,X_calib)
    plt.xlabel('Wavenumber (1/cm)')
    plt.ylabel('Absorbance')
    plt.show()

print(len(wave))
print(len(Y_calib))

# Transform on the scaled features
Xt2 = skpca2.fit_transform(X_calib)

# Define the labels for the plot legend
labplot = Y_calib #["0/8 Milk","1/8 Milk","2/8 Milk", "3/8 Milk", "4/8 Milk", "5/8 Milk","6/8 Milk","7/8 Milk", "8/8 Milk"]

# Scatter plot
unique = list(set(wave))
colors = [plt.cm.jet(float(i)/max(unique)) for i in unique]
with plt.style.context(('ggplot')):
    for i, u in enumerate(unique):
        xi = [Xt2[j,0] for j  in range(len(Xt2[:,0])) if wave[j] == u]
        yi = [Xt2[j,1] for j  in range(len(Xt2[:,1])) if wave[j] == u]
        plt.scatter(xi, yi, c=colors[i], s=60, edgecolors='k',label=str(u))

    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.legend(labplot,loc='lower right')
    plt.title('Principal Component Analysis')
plt.show()
