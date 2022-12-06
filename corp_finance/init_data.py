import pandas as pd 
import datetime as dt
import pandas_datareader as web

def stringToTimeStamp(row):
    row[0] = pd.to_datetime(row[0],format='%m/%d/%Y')
    return row

def mergeRateAndSpy(spy_lst,rates_lst):
    rates_lst = list(map(stringToTimeStamp,rates_lst))
    merged = [[*merged,rate[1]] for merged in spy_lst for rate in rates_lst if merged[0].year == rate[0].year and merged[0].month == rate[0].month]
    return merged

def getRatesAndSpyAsList():
    start = dt.datetime(1994,1,1)
    end = dt.datetime(2022,10,19)
    spy = pd.DataFrame(web.DataReader('SPY','yahoo', start, end))
    spy.reset_index(inplace=True)
    spy = spy.values.tolist()
    funds_rate = pd.read_csv('FEDFUNDS.csv').values.tolist()
    merged = mergeRateAndSpy(spy,funds_rate)
    return merged

def clients()->list:
    vix_close = pd.read_csv('VIX_History.csv')['CLOSE'].values.tolist()
    spy_and_funds = getRatesAndSpyAsList()
    return vix_close,spy_and_funds

def getFinalMergedValues()->list:
    vix_close,spy_and_funds = clients()
    values_merged = []
    for i in range(-len(spy_and_funds),0,1):
        values_merged.append([vix_close[i],spy_and_funds[i][3],spy_and_funds[i][1],spy_and_funds[i][2],spy_and_funds[i][4],spy_and_funds[i][5],spy_and_funds[i][7]])
    values_merged = pd.DataFrame(values_merged)
    values_merged.columns = ['VIX','Open','High','Low','Close','Volume','Rate']
    return values_merged


