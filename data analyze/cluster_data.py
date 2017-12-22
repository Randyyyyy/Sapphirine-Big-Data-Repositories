import os
import numpy as np
import pandas as pd
from pandas import DataFrame
import h5py
from scipy.stats import kurtosis
from scipy.stats import skew
#load all the feature information
f_path = []
f_dic = '/Users/zqq/Downloads/MillionSongSubset/data'
for dirpath, dirnames, filenames in os.walk(f_dic):
    for files in filenames:
        if (os.path.splitext(files)[1] == '.h5'):
            f_path.append(os.path.join(dirpath, files)) 

#calcualte all the feature statistics
class s_info:
    def __init__(self, source_data):
        self.mean = np.mean(source_data)
        self.std = np.std(source_data)
        self.median = np.percentile(source_data,50)
        self.skew = skew(source_data)

#Feature extraction construction
details_col = ['f_path',
           'BarCon_mean','BarCon_std',
           'BarCon_median','BarCon_skw',
           
           'BarSta_mean','BarSta_std',
           'BarSta_median','BarSta_skw',
           
           'BeatsC_mean','BeatsC_std',
           'BeatsC_median','BeatsC_skw',
           
           'BeatsS_mean','BeatsS_std',
           'BeatsS_median','BeatsS_skw',
           
           'SC_mean','SC_std',
           'SC_median','SC_skw',
           
           'SS_mean','SS_std',
           'SS_median','SS_skw',
           
           'SLM_mean','SLM_std',
           'SLM_median','SLM_skw',
           
           'SLMT_mean','SLMT_std',
           'SLMT_median','SLMT_skw',
           
           'SLS_mean','SLS_std',
           'SLS_median','SLS_skw',
           
           'TC_mean','TC_std',
           'TC_median','TC_skw',
           
           'TS_mean','TS_std',
           'TS_median','TS_skw']

#Feature extraction construction
pitch_col = [
            'pitch_0_mean','pitch_0_std','pitch_0_median',
            'pitch_0_skw',

            'pitch_1_mean','pitch_1_std','pitch_1_median',
            'pitch_1_skw',

            'pitch_2_mean','pitch_2_std','pitch_2_median',
            'pitch_2_skw',

            'pitch_3_mean','pitch_3_std','pitch_3_median',
            'pitch_3_skw',

            'pitch_4_mean','pitch_4_std','pitch_4_median',
            'pitch_4_skw',

            'pitch_5_mean','pitch_5_std','pitch_5_median',
            'pitch_5_skw',

            'pitch_6_mean','pitch_6_std','pitch_6_median',
            'pitch_6_skw',

            'pitch_7_mean','pitch_7_std','pitch_7_median',
            'pitch_7_skw',

            'pitch_8_mean','pitch_8_std','pitch_8_median',
            'pitch_8_skw',

            'pitch_9_mean','pitch_9_std','pitch_9_median',
            'pitch_9_skw',

            'pitch_10_mean','pitch_10_std','pitch_10_median',
            'pitch_10_skw',

            'pitch_11_mean','pitch_11_std','pitch_11_median',
            'pitch_11_skw']

def get_details(source_file):
    tmp_zeros = np.zeros(details_col.__len__())
    f_df = DataFrame([tmp_zeros],columns=details_col)
    
    f_tmp = h5py.File(source_file,'r')
    bars_confidence = s_info(f_tmp['analysis']['bars_confidence'][()])
    bars_start = s_info(f_tmp['analysis']['bars_start'][()])
    beats_confidence = s_info(f_tmp['analysis']['beats_confidence'][()])
    beats_start = s_info(f_tmp['analysis']['beats_start'][()])
    segments_confidence = s_info(f_tmp['analysis']['segments_confidence'][()])
    segments_loudness_max = s_info(f_tmp['analysis']['segments_loudness_max'][()])
    segments_loudness_max_time = s_info(f_tmp['analysis']['segments_loudness_max_time'][()])
    segments_loudness_start = s_info(f_tmp['analysis']['segments_loudness_start'][()])
    segments_start = s_info(f_tmp['analysis']['segments_start'][()])
    tatums_confidence = s_info(f_tmp['analysis']['tatums_confidence'][()])
    tatums_start = s_info(f_tmp['analysis']['tatums_start'][()])
    
    f_df['f_path'] = source_file

    f_df['BarCon_mean'] = bars_confidence.mean
    f_df['BarCon_std'] = bars_confidence.std
    f_df['BarCon_median'] = bars_confidence.median
    f_df['BarCon_skw'] = bars_confidence.skew

    f_df['BarSta_mean'] = bars_start.mean
    f_df['BarSta_std'] = bars_start.std
    f_df['BarSta_median'] = bars_start.median
    f_df['BarSta_skw'] = bars_start.skew

    f_df['BeatsC_mean'] = beats_confidence.mean
    f_df['BeatsC_std'] = beats_confidence.std
    f_df['BeatsC_median'] = beats_confidence.median
    f_df['BeatsC_skw'] = beats_confidence.skew

    f_df['BeatsS_mean'] = bars_start.mean
    f_df['BeatsS_std'] = bars_start.std
    f_df['BeatsS_median'] = bars_start.median
    f_df['BeatsS_skw'] = bars_start.skew

    f_df['SC_mean'] = segments_confidence.mean
    f_df['SC_std'] = segments_confidence.std
    f_df['SC_median'] = segments_confidence.median
    f_df['SC_skw'] = segments_confidence.skew

    f_df['SS_mean'] = segments_start.mean
    f_df['SS_std'] = segments_start.std
    f_df['SS_median'] = segments_start.median
    f_df['SS_skw'] = segments_start.skew

    f_df['SLM_mean'] = segments_loudness_max.mean
    f_df['SLM_std'] = segments_loudness_max.std
    f_df['SLM_median'] = segments_loudness_max.median
    f_df['SLM_skw'] = segments_loudness_max.skew

    f_df['SLMT_mean'] = segments_loudness_max_time.mean
    f_df['SLMT_std'] = segments_loudness_max_time.std
    f_df['SLMT_median'] = segments_loudness_max_time.median
    f_df['SLMT_skw'] = segments_loudness_max_time.skew

    f_df['SLS_mean'] = segments_loudness_start.mean
    f_df['SLS_std'] = segments_loudness_start.std
    f_df['SLS_median'] = segments_loudness_start.median
    f_df['SLS_skw'] = segments_loudness_start.skew

    f_df['TC_mean'] = tatums_confidence.mean
    f_df['TC_std'] = tatums_confidence.std
    f_df['TC_median'] = tatums_confidence.median
    f_df['TC_skw'] = tatums_confidence.skew

    f_df['TS_mean'] = tatums_start.mean
    f_df['TS_std'] = tatums_start.std
    f_df['TS_median'] = tatums_start.median
    f_df['TS_skw'] = tatums_start.skew

    return f_df

		
def get_pitch(source_file):
    tmp_zeros = np.zeros(pitch_col.__len__())
    f_df = DataFrame([tmp_zeros],columns = pitch_col)
    
    f_tmp = h5py.File(source_file,'r')
    pitch_matrix = np.asmatrix(f_tmp['analysis']['segments_pitches'][()])

    pitch_0 = s_info(pitch_matrix[:,0])
    pitch_1 = s_info(pitch_matrix[:,1])
    pitch_2 = s_info(pitch_matrix[:,2])
    pitch_3 = s_info(pitch_matrix[:,3])
    pitch_4 = s_info(pitch_matrix[:,4])
    pitch_5 = s_info(pitch_matrix[:,5])
    pitch_6 = s_info(pitch_matrix[:,6])
    pitch_7 = s_info(pitch_matrix[:,7])
    pitch_8 = s_info(pitch_matrix[:,8])
    pitch_9 = s_info(pitch_matrix[:,9])
    pitch_10 = s_info(pitch_matrix[:,10])
    pitch_11 = s_info(pitch_matrix[:,11])

    f_df['pitch_0_mean'] = pitch_0.mean
    f_df['pitch_0_median'] = pitch_0.median
    f_df['pitch_0_std'] = pitch_0.std
    f_df['pitch_0_skw'] = pitch_0.skew

    f_df['pitch_1_mean'] = pitch_1.mean
    f_df['pitch_1_median'] = pitch_1.median
    f_df['pitch_1_std'] = pitch_1.std
    f_df['pitch_1_skw'] = pitch_1.skew

    f_df['pitch_2_mean'] = pitch_2.mean
    f_df['pitch_2_median'] = pitch_2.median
    f_df['pitch_2_std'] = pitch_2.std
    f_df['pitch_2_skw'] = pitch_2.skew

    f_df['pitch_3_mean'] = pitch_3.mean
    f_df['pitch_3_median'] = pitch_3.median
    f_df['pitch_3_std'] = pitch_3.std
    f_df['pitch_3_skw'] = pitch_3.skew

    f_df['pitch_4_mean'] = pitch_4.mean
    f_df['pitch_4_median'] = pitch_4.median
    f_df['pitch_4_std'] = pitch_4.std
    f_df['pitch_4_skw'] = pitch_4.skew

    f_df['pitch_5_mean'] = pitch_5.mean
    f_df['pitch_5_median'] = pitch_5.median
    f_df['pitch_5_std'] = pitch_5.std
    f_df['pitch_5_skw'] = pitch_5.skew

    f_df['pitch_6_mean'] = pitch_6.mean
    f_df['pitch_6_median'] = pitch_6.median
    f_df['pitch_6_std'] = pitch_6.std
    f_df['pitch_6_skw'] = pitch_6.skew

    f_df['pitch_7_mean'] = pitch_7.mean
    f_df['pitch_7_median'] = pitch_7.median
    f_df['pitch_7_std'] = pitch_7.std
    f_df['pitch_7_skw'] = pitch_7.skew

    f_df['pitch_8_mean'] = pitch_8.mean
    f_df['pitch_8_median'] = pitch_8.median
    f_df['pitch_8_std'] = pitch_8.std
    f_df['pitch_8_skw'] = pitch_8.skew

    f_df['pitch_9_mean'] = pitch_9.mean
    f_df['pitch_9_median'] = pitch_9.median
    f_df['pitch_9_std'] = pitch_9.std
    f_df['pitch_9_skw'] = pitch_9.skew

    f_df['pitch_10_mean'] = pitch_10.mean
    f_df['pitch_10_median'] = pitch_10.median
    f_df['pitch_10_std'] = pitch_10.std
    f_df['pitch_10_skw'] = pitch_10.skew

    f_df['pitch_11_mean'] = pitch_11.mean
    f_df['pitch_11_median'] = pitch_11.median
    f_df['pitch_11_std'] = pitch_11.std
    f_df['pitch_11_skw'] = pitch_11.skew

    return f_df

cluster_data = DataFrame()  
wrong_file = []

for k in range(f_path.__len__()):
    try:
        details = get_details(f_path[k])
        pitches = get_pitch(f_path[k])
        df_tmp = pd.concat([details,pitches],axis = 1)
        cluster_data = cluster_data.append(df_tmp)
        print k
    except:
        wrong_file.append(f_path[k])
        print "wrong file is:",k

cluster_data.index = range(cluster_data.shape[0])
        
cluster_data.to_csv('cluster_data.csv')