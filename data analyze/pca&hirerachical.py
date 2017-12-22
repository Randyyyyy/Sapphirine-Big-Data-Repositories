import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import metrics
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from scipy.cluster import hierarchy
import pandas as pd
from pandas import DataFrame

scale_data = DataFrame.from_csv('/Users/zqq/Downloads/million-song-recommendation-master/data.csv')
scale_data = DataFrame.as_matrix(scale_data)
#Use PCA
pca = PCA(n_components=20)
pca.fit(scale_data)


for k in range(pca.explained_variance_ratio_.shape[0]):
    print k,'_', sum(pca.explained_variance_ratio_[0:k])

t_data = pca.transform(scale_data)


DataFrame(t_data).to_csv('transform_data.csv')

# Hierarchy Clustering
A = hierarchy.linkage(transform_data, method='ward', metric='euclidean')
plt.figure()
dn = hierarchy.dendrogram(A)
plt.show()