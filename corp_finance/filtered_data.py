import statistics
import pandas as pd
from data_preparation import addMovingAverages

def gapsRelativeToStandardDeviation(df,position,multiplicator):
    if position.lower() == 'out':
        df_filtered = df[(df['Gap']>df['Gap_mean']+df['Gap_std']*multiplicator) | (df['Gap']<df['Gap_mean']-df['Gap_std']*multiplicator)]
    elif position.lower() == 'in': 
        df_filtered = df[abs(df['Gap']-df['Gap_mean'])<df['Gap_std']/multiplicator]
    return df_filtered

def filterByVixCoded(df,key):
    df_filteed = df[df['V_coded']==key]
    return df_filteed

def filterByVixValue(df,val,relation):
    if relation.lower()=='above':
        df_filteed = df[df['VIX']>val]
    elif relation.lower()=='below':
        df_filteed = df[df['VIX']<val]
    return df_filteed

def filterByTrend(df,ma_short_term,ma_long_term,direction):
    if direction.lower() == 'up':
        df_filteed = df[df[f'MA{ma_short_term}']>df[f'MA{ma_long_term}']]
    elif direction.lower() == 'down':
        df_filteed = df[df[f'MA{ma_short_term}']<df[f'MA{ma_long_term}']]
    return df_filteed

def upTrend(df,ma_short,ma_long):
    df = df[(df['Close'].rolling(ma_short,0).mean()>df['Close'].rolling(ma_long,0).mean())]
    return df

def downTrend(df,ma_short,ma_long):
    df = df[(df['Close'].rolling(ma_short,0).mean()<df['Close'].rolling(ma_long,0).mean())]
    return df
