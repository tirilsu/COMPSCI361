import matplotlib.pyplot as plt  
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA

from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import Birch

data = pd.read_csv('BanknoteData.csv')

features = ['V1','V2','V3','V4']

# Separating out the features
x = data.loc[:, features].values
# Standardizing the features
x = StandardScaler().fit_transform(x)

#pca = PCA(n_components=2)
pca = KernelPCA(n_components=2,kernel='rbf',gamma=0.9)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['pca1', 'pca2'])

"""cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')  
labels = cluster.fit_predict(principalDf)
labels = 1-labels"""

# cluster the data into five clusters
"""dbscan = DBSCAN(eps=0.15, min_samples = 25, metric='euclidean')
labels = dbscan.fit_predict(principalDf)
"""
clustering = Birch(branching_factor=100, n_clusters = 2, threshold = 0.1)
pred = clustering.fit_predict(principalDf)
for i in range(len(pred)):
	if pred[i] == -1:
		pred[i] = 1


output = pd.DataFrame()
output['ID'] = data.loc[:,'ID']
output['Class'] = pred


output.to_csv('A5_kaggle_submission.csv',index=False, encoding='utf-8')
