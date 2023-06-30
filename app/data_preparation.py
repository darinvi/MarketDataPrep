import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import numpy as np
from init_data import getFinalMergedValues

# TO DO: apply all the function in a prettier and shorter way
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
    all_val = addRTR(all_val)
    all_val = addRR(all_val)
    all_val = addMovingAverages(all_val)
    all_val = addNextDayContinuation(all_val)
    all_val = addCloseAtExtreme(all_val)
    all_val = addCloseHeldOpen(all_val)
    all_val = addStandardDeviation(all_val,'Gap', 200)
    all_val = addMean(all_val,'Gap', 200)
    all_val = addTrendBool(all_val)
    all_val = addRvolBool(all_val, 1.25)
    all_val = addGapStandardDeviation(all_val)
    # all_val[200:].to_parquet('market_data.parquet')
    return all_val[200:]


def addYesterdayClose(df):
    df['YCl'] = df['Close'].shift(1)
    return df


def addRangeToday(df):
    df['Range'] = df['High'] - df['Low']
    return df

def recodeVolatility(df):
    conditions = [(df['VIX'] < 10),(df['VIX']//10==1),(df['VIX']//10==2),(df['VIX']//10==3),(df['VIX']//10>3)]
    values = [1,2,3,4,5]
    df['V_coded'] = np.select(conditions,values)
    return df

def addGap(df):
    df['Gap'] = (df['Open'] - df['Close'].shift(1))/df['Close'].shift(1)*100
    return df


# add the standard deviation of a chosen column for the past N days (rows).
def addStandardDeviation(df, col, range):
    df[f'{col}_std'] = df[col].shift(1).rolling(range,0).std()
    return df


# add the mean value of a chosen column for the past N days (rows).
def addMean(df,col, range):
    df[f'{col}_mean'] = df[col].shift(1).rolling(range,0).mean()
    return df


# Relative Volume (RVOL) is a measure of how much volume is being realized today relative to the volume done in an average day.
# It is a coefficient and the higher it is, the more in play the stock is. A reading of 1 means it is an average day. 
def addRvol(df):
    df['Rvol'] = df['Volume']/df['Volume'].shift(1).rolling(window=20,min_periods=0).mean()
    return df


# The True range of the day is similar to the "range" reading, but it takes into account the gap for the day.
# If today's range is completely outside yesterday's range, then the true range will be higher than the range for sure.
def addTrueRange(df):
    true_range = pd.DataFrame([])
    true_range['m1'] = df['High']-df['Low']
    true_range ['m2'] = abs(df['High']-df['Close'].shift(1))
    true_range['m3'] = abs(df['Low']-df['Close'].shift(1))
    df['TR'] = true_range[['m1', 'm2', 'm3']].max(axis=1)
    return df


# the average true range (ATR) is the average of the true range reading. This is a good measure for how much a stock might move on an given day
def addATR(df):
    df['ATR'] = df['TR'].shift(1).rolling(20,0).mean()
    return df


# Average range ignoring the gap
def addAR(df):
    df['AR'] = (df['High'] - df['Low']).shift(1).rolling(20,0).mean()
    return df


# Compare true range to average true range - Relative True Range
def addRTR(df):
    df['RTR'] = df['TR']/df['ATR']
    return df


# Compare range to average range - Relative Range
def addRR(df):
    df['RR'] = df['Range']/df['AR']
    return df


# Some arbitrary moving averages. There is nothing special to the 50,100,200 values.
def addMovingAverages(df):
    df['MA50'] = df['Close'].rolling(50,0).mean()
    df['MA100'] = df['Close'].rolling(100,0).mean()
    df['MA200'] = df['Close'].rolling(200,0).mean()
    return df


# 1 if the stock closed in the upper 80% of it's range.
# -1 if the stock closedin the lower 80% of it's range.
# 0 if it closed far from either extreme.
def checkCloseAtExtreme(row):
    #FIX VAL
    if (row['High']-row['Close']) / (row['High']-row['Low']) <= 0.2:
        return 1
    elif (row['Close']-row['Low']) / (row['High']-row['Low']) <= 0.2:
        return -1
    else:
        return 0

def addCloseAtExtreme(df):
    df['ExCl'] = df.apply(checkCloseAtExtreme, axis=1)
    return df    


# 1 if the stock gapped higher and held the gap (held defined by closing higher than the opening print)
# -1 if the stock held a gap lower
# 0 in any other scenario
def checkCloseHeldOpen(row):
    close_upper = bool(row['Close']>row['Open'] and row['Gap'] > 0)
    close_lower = bool(row['Close']<row['Open'] and row['Gap'] < 0)
    if close_upper:
        return 1
    elif close_lower:
        return -1
    else:
        return 0 

def addCloseHeldOpen(df):
    df['Held_Open'] = df.apply(checkCloseHeldOpen,axis=1)
    return df



# shift(-1) means we take tommorow's value.
# 1 if today's candle is green (relative to today's open) and the next day saw continuation (closed higher than today's close)
# -1 if today's candle is red and the next day closed lower again.
# 0 if no continuation
def addNextDayContinuation(df):
    cond = [
        ((df['Close']>df['Open']) & (df['Close'].shift(-1)>df['Close'])),
        ((df['Close']<df['Open']) & (df['Close'].shift(-1)<df['Close']))
    ]
    val = [1,-1]
    df['D2'] = np.select(cond,val,0)
    return df


# Arbitrary criteria for stock being in a trend based on moving averages (ma). 
# 1: if 50ma > 100ma > 200ma, -1: if 50ma < 100ma < 200ma, 0 otherwise.
def addTrendBool(df):
    #Change val
    conditions = [
        ((df['MA50']>df['MA100']) & (df['MA100']>df['MA200'])),
        (df['MA50']<df['MA100']) & (df['MA100']<df['MA200'])
    ]
    values = [1,-1]
    df['Trend_bool'] = np.select(conditions,values,0)
    return df


# Boolean for whether the RVOL was above a certain value. Used for binary domain models.
def addRvolBool(df, val):
    cond,val = [
        df['Rvol'] > val
    ],[
        1
    ]
    df['RVOL_bool'] = np.select(cond,val)
    return df


# 1 if the gap higher of a stock is more than the average gap plus the standard deviation of the gaps.
# -1 if the gap lower is more than the average gap minus the std. 
# 0 in any other case 
def addGapStandardDeviation(df):
    cond = [
        df['Gap']>df['Gap_mean']+df['Gap_std'],
        df['Gap']<df['Gap_mean']-df['Gap_std']
    ]
    val = [1,-1]
    df['Gap_bool'] = np.select(cond,val,0)
    return df
