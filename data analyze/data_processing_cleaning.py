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

# File path should be changed
sys.path.append('/Users/zqq/Downloads/MSongsDB-master/PythonSrc')
# Use filter(lambda x: x[:3] == 'get',HDF5.__dict__.keys()) we can find all the methods to get song metadata

# We should do: !pip install h5py
# The feasures we are going to use is as follows:
% time
artist_names = []
artist_familiarty = []
artist_hotness = []
artist_id = []
artist_latitude = []
artist_longitude = []
artist_location = []
file_path = []
song_id = []
song_titles = []
song_durations = []
song_release_year = []
song_hotness = []
track_id = []
song_tempo = []
song_bars = []
song_beats = []
song_time_signatures =[]
song_tatum = []
song_modes = []
song_keys = []

for f in files:
    h5 = tables.open_file(f)
    filepath = f
    artist_name = g.get_artist_name(h5)
    artist_familar = g.get_artist_familiarity(h5)
    artist_hot = g.get_artist_hotttnesss(h5)
    artist_ids = g.get_artist_id(h5)
    artist_lat = g.get_artist_latitude(h5)
    artist_long = g.get_artist_longitude(h5)
    artist_loc = g.get_artist_location(h5)
    song_idss = g.get_song_id(h5)
    song_speed = g.get_tempo(h5)
    song_bar = g.get_bars_start(h5)
    song_beat = g.get_beats_start(h5)
    song_time_signature = g.get_time_signature(h5)
    song_tat = g.get_tatums_start(h5)
    song_mode = g.get_mode(h5)
    song_key = g.get_key(h5)
    song_idss = g.get_song_id(h5)
    song_title = g.get_title(h5)
    song_duration = g.get_duration(h5)
    song_release_years = g.get_year(h5)
    song_hot = g.get_song_hotttnesss (h5)
    track_idss = g.get_track_id(h5)
    
    file_path.append(filepath)
    artist_names.append(artist_name)
    artist_familiarty.append(artist_familar)
    artist_hotness.append(artist_hot)
    artist_id.append(artist_ids)
    artist_latitude.append(artist_lat)
    artist_longitude.append(artist_long)
    artist_location.append(artist_loc)
    song_id.append(song_idss)  
    song_tempo.append(song_speed)
    song_bars.append(song_bar)
    song_beats.append(song_beat)
    song_time_signatures.append(song_time_signature)
    song_tatum.append(song_tat)
    song_modes.append(song_mode)
    song_keys.append(song_key)
    song_id.append(song_idss)
    song_titles.append(song_title)
    song_durations.append(song_duration)
    song_release_year.append(song_release_years)
    song_hotness.append(song_hot)
    track_id.append(track_idss) 
    h5.close()
    
data = {'artist_names':artist_names
        ,'artist_familiarty':artist_familiarty
        ,'artist_hotness':artist_hotness
        ,'artist_latitude':artist_latitude
        ,'artist_longitude':artist_longitude
        ,'artist_location':artist_location
        ,'artist_id':artist_id
        ,'file_path':file_path
        ,'song_id':song_id
        ,'track_id':track_id
        ,'song_titles':song_titles
        ,'song_durations':song_durations
        ,'song_release_years':song_release_year
        ,'song_hotness':song_hotness
        ,'song_tempo':song_tempo
        ,'song_bars':song_bars
        ,'song_beats':song_beats
        ,'song_time_signatures':song_time_signatures
        ,'song_tatum':song_tatum
        ,'song_modes':song_modes
        ,'song_keys':song_keys
       }

data.to_csv('basic_data.csv', sep=',')

# In order to add rating information to every song, we need other feasures
user_behavior = pd.read_table('/Users/zqq/Downloads/train_triplets.txt', sep='\t', names =['user_id','song_ids','play_count'])

# Count every song's playing times and listeners
functions = {'play_count':['sum'], 'user_id':['count']}
behavior = user_behavior.groupby('song_ids').agg(functions)
data_with_behavior = data.merge(behavior,on='song_id')

# Delete unecessary columns in data_with_behavior
data = data_with_behavior.drop('Unnamed: 0',1)
data = data.drop('song_id_y',1)
data = data.rename(columns = {'song_id_x':'song_id'})

# Change vector columns such as song_bars, song beats and song_tatum
data['beats_number'] = [len(x) for x in data.song_beats]
data['bars_number'] = [len(x) for x in data.song_bars]
data['tatum_number'] = [len(x) for x in data.song_tatum]
data = data.drop(['Unnamed: 0','artist_latitude','artist_location','artist_longitude','song_bars','song_beats','song_tatum'],1)
# The user_id_count and play_count_sum vary a lot, we need to centralize the data
data['log_user_id_count'] = np.log(data[['user_id_count']])
data['log_play_count_sum'] = np.log(data[['play_count_sum']])
# Set threshold and get rating information
bins = [1,2,10,20,40, np.inf]
data['rating']= pd.cut(data['play_count'], bins=bins, include_lowest=True, labels=[1,2,3,4,5]).astype(int)

