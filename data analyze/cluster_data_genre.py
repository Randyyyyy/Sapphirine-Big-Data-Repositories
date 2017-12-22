import os
import numpy as np
import pandas as pd
from pandas import DataFrame
import h5py

# count the word frequency and weight for each cluster
cluster_data = DataFrame.from_csv("/Users/zqq/Downloads/cluster.csv")

# group number is 0,1,2,3,4,5
def get_word_fre(group):
    artist_0 = np.array([])
    artist_0_freq = np.array([])

    for k in range(cluster_data.shape[0]):
        f_name = cluster_data['f_path'][k]
        f_tmp = h5py.f(f_name,'r')
        artist_terms = f_tmp['metadata']['artist_terms'][()]
        artist_freq = f_tmp['metadata']['artist_freq'][()]
        artist_weight = f_tmp['metadata']['artist_weight'][()]
   
        if cluster_data['cluster'][k] == group:
            for word in artist_terms:
                if not word in artist_0:
                    artist_0 = np.append(word,artist_0)

    artist_0 = np.ndarray.tolist(artist_0)
    artist_0_freq = np.zeros(artist_0.__len__())
    artist_0_weight = np.zeros(artist_0.__len__())
    artist_0_addone = np.zeros(artist_0.__len__())

    for k in range(cluster_data.shape[0]):
        f_name = cluster_data['f_path'][k]
        f_tmp = h5py.f(f_name,'r')
        artist_terms = f_tmp['metadata']['artist_terms'][()]
        artist_freq = f_tmp['metadata']['artist_freq'][()]
        artist_weight = f_tmp['metadata']['artist_weight'][()] 
        if cluster_data['cluster'][k] == group:
            for word in artist_terms:
                index = artist_0.index(word)
                index_in = np.where(artist_terms == word)
                weight = artist_weight[index_in]
                freq = artist_freq[index_in]
                
                artist_0_freq[index] += freq
                artist_0_weight[index] += weight
                artist_0_addone[index] += 1

    fre_table_0 = DataFrame({'artist_terms':artist_0,
                                   'frenquency':artist_0_freq,
                                   'weight':artist_0_weight,
                                   'add_one':artist_0_addone})
    return fre_table_0
# Change the number to get from other group 
# In our case, we change the number from zero to five to get six groups of data.
group_f = get_word_fre(0)	
group_f.to_csv('group0.csv')