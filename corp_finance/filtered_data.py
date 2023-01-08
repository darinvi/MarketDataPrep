import statistics
import pandas as pd
from data_preparation import addMovingAverages

def gapsRelativeToStandardDeviation(df,position,multiplicator):
    if position.lower() == 'out':
        df_filtered = df[(df['Gap']>df['Gap_mean']+df['Gap_std']*multiplicator) | (df['Gap']<df['Gap_mean']-df['Gap_std']*multiplicator)]
    elif position.lower() == 'in': 
        df_filtered = df[abs(df['Gap']-df['Gap_mean'])<df['Gap_std']/multiplicator]
    return df_filtered

def filterByVixValue(df,key):
    df_filteed = df[df['V_coded']==key]
    return df_filteed

def filterConsecutiveRedDays(df):
    for i in range(1,5):
        df[f'yd{i}'] = df['Close'].shift(i)
    df = df[(df['yd1']<df['yd2'])&(df['yd2']<df['yd3'])]
    # df = df[(df['yd1']<df['yd2'])&(df['yd2']<df['yd3'])&(df['yd3']<df['yd4'])]
    return df
