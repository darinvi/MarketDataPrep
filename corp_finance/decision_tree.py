import numpy as np
import pandas as pd
import time 
from data_preparation import marketValuesList
import math

class InternalNode:
    def __init__(self,feature,df):
        self.df = df
        self.feature = feature
        self.left_child = 0
        self.right_child = 0

    def create_left_child():
        pass

def pick_best_feature(df):
    def calculate_entropy(test_df):
        p = len(test_df[test_df['D2']==1])/len(test_df)
        entropy = - p*math.log(p,2) - (1-p)*math.log((1-p),2)
        return entropy
    
    entropyes = {}
    
    for el in list(df.columns)[:-1]:
        p_exmp = df[df[el]==1]
        n_exmp = df[df[el]==0]
        p_entropy = calculate_entropy(p_exmp)
        n_entropy = calculate_entropy(n_exmp)
        avg_entropy = len(p_exmp)/len(df)*p_entropy + len(n_exmp)/len(df)*n_entropy
        entropyes[el] = avg_entropy

    return sorted(entropyes.items(),key=lambda x: x[1])[0][0]

def buld_tree(df):
    if len(df[' D2'].unique()==1):
        pass
    else:
        best_feature = pick_best_feature(df)



df = marketValuesList()[-200:]
df_train = df[['Held_Open','Trend_bool','RVOL_bool','Gap_bool','ExCl','D2']][:int(len(df)*0.8)]
df_test = df[['Held_Open','Trend_bool','RVOL_bool','Gap_bool','ExCl','D2']][int(len(df)*0.8):].values.tolist()
print(np.array(df_test))
