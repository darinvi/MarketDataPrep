import pandas as pd 
import datetime as dt
import pandas_datareader as web

def clients()->list:
    start = dt.datetime(1994,1,1)
    end = dt.datetime(2022,10,20)
    vix_close = pd.read_csv('VIX_History.csv')['CLOSE'].values.tolist()
    # funds_rate = pd.read_csv('FEDFUNDS.csv')#.values.tolist()
    spy = pd.DataFrame(web.DataReader('SPY', 'yahoo', start, end)).values.tolist()
    return vix_close,spy
    # tlt_close = pd.DataFrame(web.DataReader('TLT', 'yahoo', start, end)["Close"]).values.tolist()
    # return vix_close,tlt_close,spy
clients()

def getMergedValues()->list:
    vix_close,spy = clients()
    values_merged = []
    for i in range(-len(spy),0,1):
        values_merged.append([vix_close[i],spy[i][2],spy[i][0],spy[i][1],spy[i][3],spy[i][4]])
    values_merged = pd.DataFrame(values_merged)
    values_merged.columns = ['VIX','Open','High','Low','Close','Volume']
    return values_merged
    # vix_close,tlt_close,spy = clients()
    # for i in range(-len(tlt_close),0,1):
    #     values_merged.append([vix_close[i],tlt_close[i][0],spy[i][2],spy[i][0],spy[i][1],spy[i][3],spy[i][4]])
    # values_merged.columns = ['VIX','TLT','Open','High','Low','Close','Volume']

def addLastFedRate():
    pass