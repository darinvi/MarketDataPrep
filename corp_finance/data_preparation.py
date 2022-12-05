import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import numpy as np

def clients()->list:
    start = dt.datetime(2006,1,1)
    end = dt.datetime(2022,10,20)
    vix_close = pd.read_csv('VIX_History.csv')['CLOSE'].values.tolist()
    tlt_close = pd.DataFrame(web.DataReader('TLT', 'yahoo', start, end)["Close"]).values.tolist()
    spy = pd.DataFrame(web.DataReader('SPY', 'yahoo', start, end)).values.tolist()
    return vix_close,tlt_close,spy

def getMergedValues()->list:
    vix_close,tlt_close,spy = clients()
    values_merged = []
    for i in range(-len(tlt_close),0,1):
        values_merged.append([vix_close[i],tlt_close[i][0],spy[i][2],spy[i][0],spy[i][1],spy[i][3],spy[i][4]])
    values_merged = pd.DataFrame(values_merged)
    values_merged.columns = ['VIX','TLT','Open','High','Low','Close','Volume']
    return values_merged

def marketValuesList()->dict:
    all_val = getMergedValues()
    all_val = addRangeToday(all_val)
    all_val = addTrueRange(all_val)
    all_val = recodeVolatility(all_val)
    all_val = addGap(all_val)
    all_val = addRvol(all_val)
    all_val = addATR(all_val)
    all_val = addAR(all_val)
    all_val = addRTR(all_val)
    all_val = addRR(all_val)
    print(all_val[1:])
    # all_val = close_extreme_boolean(all_val)
    # all_val = close_held_open_rate(all_val)
    # all_val.columns = ["VIX","VIX_Coded","TLT","Open","High","Low","Close","Volume","Chng","Cl_Ex","Wrong","Rvol","ATR","Rrng"]
    # all_val = all_val[19:len(all_val)]
    return(all_val[1:])

def addRangeToday(df):
    df['Range'] = df['High'] - df['Low']
    return df

def recodeVolatility(df):
    conditions = [(df['VIX'] < 10),(df['VIX']//10==1),(df['VIX']//10==2),(df['VIX']//10==3),(df['VIX']//10==4),(df['VIX']//10>4)]
    values = [1,2,3,4,5,6]
    df['V_coded'] = np.select(conditions,values)
    return df

def addGap(df)->dict:
    df['Gap'] = (df['Open'] - df['Close'].shift(1))/df['Close'].shift(1)*100
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


# def close_extreme_boolean(lst:list):
#     for i in range(len(lst)):
#         high, low, close = lst[i][4], lst[i][5], lst[i][6]
#         daily_range = high-low
#         if (high-close)/daily_range<=0.2:
#             lst[i].append(1)
#         elif (close-low)/daily_range<=0.2:
#             lst[i].append(1)
#         else:
#             lst[i].append(0)
#         # print(lst[i])
#     return lst    
        

# def close_held_open_rate(lst:list):
#     for i in range(len(lst)):
#         close_held_open = 0
#         if i >= 100:
#             for j in range(1,101):
#                 gap, close, open = lst[i-j][7], lst[i-j][6], lst[i-j][3]
#                 if (gap > 0 and close >= open) or (gap < 0 and close <= open):
#                     close_held_open += 1
#         lst[i].append(close_held_open)
#     return lst


# # def close_at_extreme_quantitative(df):
# #     df["Close_extreme_q"] = df[]
# #     print(df)

# def closeExtremeRate(df):
#     df["cl_ex_rate"] = df['Cl_Ex'].shift(1).rolling(3,3).sum()
#     df = df[100:]
#     print(df)