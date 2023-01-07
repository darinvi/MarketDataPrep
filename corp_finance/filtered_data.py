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

def upTrend(df,ma_short,ma_long):
    df = df[(df['Close'].rolling(ma_short,0).mean()>df['Close'].rolling(ma_long,0).mean())]
    return df

def downTrend(df,ma_short,ma_long):
    df = df[(df['Close'].rolling(ma_short,0).mean()<df['Close'].rolling(ma_long,0).mean())]
    return df
