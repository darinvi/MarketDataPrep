import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import numpy as np
from init_data import getFinalMergedValues


def marketValuesList()->dict:
    all_val = getFinalMergedValues()
    all_val = addRangeToday(all_val)
    all_val = addTrueRange(all_val)
    all_val = recodeVolatility(all_val)
    all_val = addGap(all_val)
    all_val = addRvol(all_val)
    all_val = addATR(all_val)
    all_val = addYesterdayClose(all_val)
    all_val = addAR(all_val)
    # all_val = addRTR(all_val)
    all_val = addRR(all_val)
    all_val = addMovingAverages(all_val)
    all_val = addNextDayContinuation(all_val)
    all_val = addCloseAtExtreme(all_val)
    all_val = addCloseHeldOpen(all_val)
    all_val = addStandardDeviation(all_val,'Gap')
    all_val = addMean(all_val,'Gap')
    # all_val = addCloseExtremeRate(all_val)
    # all_val = addOpenHeldRate(all_val)
    print(all_val.columns)
    return(all_val[200:])

def addRangeToday(df):
    df['Range'] = df['High'] - df['Low']
    return df

def recodeVolatility(df):
    conditions = [(df['VIX'] < 10),(df['VIX']//10==1),(df['VIX']//10==2),(df['VIX']//10==3),(df['VIX']//10>3)]
    values = [1,2,3,4,5]
    df['V_coded'] = np.select(conditions,values)
    return df

def addGap(df)->dict:
    df['Gap'] = (df['Open'] - df['Close'].shift(1))/df['Close'].shift(1)*100
    return df

def addStandardDeviation(df,col):
    df[f'{col}_std'] = df[col].shift(1).rolling(200,0).std()
    return df

def addMean(df,col):
    df[f'{col}_mean'] = df[col].shift(1).rolling(200,0).mean()
    return df

def addRvol(df):
    df['Rvol'] = df['Volume']/df['Volume'].shift(1).rolling(window=20,min_periods=0).mean()
    return df

def addTrueRange(df):
    # add True range for the day
    true_range = pd.DataFrame([])
    true_range['m1'] = df['High']-df['Low']
    true_range ['m2'] = abs(df['High']-df['Close'].shift(1))
    true_range['m3'] = abs(df['Low']-df['Close'].shift(1))
    df['TR'] = true_range[['m1', 'm2', 'm3']].max(axis=1)
    return df
    
def addATR(df):
    # Average True Range takes into account the gap
    df['ATR'] = df['TR'].shift(1).rolling(20,0).mean()
    return df

def addAR(df):
    # I want to compute Average Range without gap aswell
    df['AR'] = (df['High'] - df['Low']).shift(1).rolling(20,0).mean()
    return df

def addRTR(df):
    # I want to compare true range to average true range - Relative True Range
    df['RTR'] = df['TR']/df['ATR']
    return df

def addRR(df):
    # I want to compare range to average range - Relative Range
    df['RR'] = df['Range']/df['AR']
    return df

def addMovingAverages(df):
    df['MA50'] = df['Close'].rolling(50,0).mean()
    df['MA100'] = df['Close'].rolling(100,0).mean()
    df['MA200'] = df['Close'].rolling(200,0).mean()
    return df

def checkCloseAtExtreme(row):
    if (row['High']-row['Close']) / (row['High']-row['Low']) <= 0.2:
        return 1
    elif (row['Close']-row['Low']) / (row['High']-row['Low']) <= 0.2:
        return -1
    else:
        return 0

def addCloseAtExtreme(df):
    df['ExCl'] = df.apply(checkCloseAtExtreme, axis=1)
    return df    

# def addCloseExtremeRate(df):
#     df['ExCl_Rate'] = abs(df['ExCl']).rolling(100,0).mean()
#     return df

def checkCloseHeldOpen(row):
    close_upper = bool(row['Close']>row['Open'] and row['Gap'] > 0)
    close_lower = bool(row['Close']<row['Open'] and row['Gap'] < 0)
    if close_upper or close_lower:
        return 1
    else:
        return 0 

def addCloseHeldOpen(df):
    df['Held_Open'] = df.apply(checkCloseHeldOpen,axis=1)
    return df

# def addOpenHeldRate(df):
#     df['Held_Rate'] = abs(df['Held_Open']).rolling(100,0).mean()
#     return df

def addNextDayContinuation(df):
    df['Close_tomorrow'] = df['Close'].shift(-1)
    df['D2'] = df.apply(checkContinuation,axis=1)
    del df['Close_tomorrow']
    return df

def checkContinuation(row):
    if (row['Close']-row['Open'])*(row['Close_tomorrow']-row['Close'])>0:
        return 1
    else:
        return 0 

def addYesterdayClose(df):
    df['YCl'] = df['Close'].shift(1)
    return df