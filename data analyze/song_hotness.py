import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import vincent as vin
import seaborn as sb
import os
import sys
import time
import glob
import datetime
import sqlite3
import numpy as nm
import hdf5_getters as g
%matplotlib inline

# Do cross validation
# Split the dataset into training set and test set in order to calculate the cross validation score
from sklearn.cross_validation import cross_val_score, train_test_split 
from sklearn.metrics import mean_absolute_error, mean_squared_error
from patsy import dmatrices 

# Select features
import statsmodels.formula.api as sm
from sklearn.feature_selection import RFE
from sklearn.ensemble import ExtraTreesClassifier

# Split the dataset into training set and test set and to calculate the cross validation score
X = data[['play_count_sum','user_id_count','artist_familiarty','artist_hotness','song_durations','song_release_years',\
        'song_keys','song_modes','song_tempo','song_time_signatures','beats_number','bars_number','tatum_number','log_play_count_sum','log_user_id_count']]
y = np.asarray(data['song_hotness'], dtype="|S6")

#  Use Recursive Feature Elimination 
X_train, X_test, y_train, y_test = train_test_split (X,y,train_size=.7,random_state=42)
log_reg_model = LogisticRegression()
rfe = RFE(log_reg_model, 5)
rfe = rfe.fit(X_train, y_train)
rfe_ranking=pd.DataFrame(rfe.ranking_, index = X_train.columns.values, 
                         columns =['ranking']).sort_values('ranking',ascending=[True])
rfe_ranking