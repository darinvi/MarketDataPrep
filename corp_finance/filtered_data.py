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

def filterByTrend(df,ma_short_term,ma_long_term,direction):
    if direction.lower() == 'up':
        df_filteed = df[df[f'MA{ma_short_term}']>df[f'MA{ma_long_term}']]
    elif direction.lower() == 'down':
        df_filteed = df[df[f'MA{ma_short_term}']<df[f'MA{ma_long_term}']]
    return df_filteed

def upTrend(df):
    # df = df[(df['Close'].rolling(20,0).mean()>df['Close'].rolling(50,0).mean()) & (df['Close'].rolling(50,0).mean()>df['Close'].rolling(100,0).mean())]
    df = df[(df['Close'].rolling(100,0).mean()>df['Close'].rolling(200,0).mean())]
    return df