import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import vincent as vin
import seaborn as sb
import time
from patsy import dmatrix
%matplotlib inline

# Recommendation_data1 and recommendation_data2 are derived from recommendation_data

# Style hip-hop
df = pd.read_csv('recommendation_data1.csv', sep=',')
# For style rock
# df = pd.read_csv('recommendation_data2.csv', sep=',')

song_names = df.groupby('song_id').song_titles.first()
M = df.groupby('song_id').rating.mean()

%%time
n_ratings = df.groupby(['song_id', 'user_id']).size()
n_ratings[n_ratings  > 1] = 1  
# Replace empty cells with zero
n_ratings = n_ratings.unstack().fillna(0) 
n_ratings = n_ratings.dot(n_ratings.T)  

# Get score to show two songs' commonness
# note that if we have no common ratings, we get a NaN now
sim = M.dot(M.T)  
sim = sim / n_ratings 

# Get the user reviews and recommend three songs for a certain user
my_reviews = df[df.user_id == user].groupby('song_id').rating.mean()\
    .sort_values(ascending=False, inplace=False)
    
top = 3
favorite_songs = list(my_reviews.index)
pred = sim[favorite_songs].mean(axis=1).dropna().sort_index(ascending=False, inplace=False)
pred_name = pd.Series(song_names[pred.index], name=pred.name)
print "Top recommendations: " 
print pred_name.head(3)