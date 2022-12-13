import statistics
import pandas as pd

def gapsOutsideStandardDeviation(df):
    df_filtered = df[(df['Gap']>df['Gap_mean']+df['Gap_std']) | (df['Gap']<df['Gap_mean']-df['Gap_std'])]
    return df_filtered

def closeAtExtremeOnly(df):
    df_filtered = df[df['ExCl']!=0]
    return df_filtered