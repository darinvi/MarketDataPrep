import datetime as dt
import pandas as pd
import pandas_datareader.data as web

def market_values_list():
    
    start = dt.datetime(2006,1,1)
    end = dt.datetime(2022,10,20)

    vix_close = pd.read_csv('VIX_History.csv')['CLOSE'].values.tolist()
    tlt_close = pd.DataFrame(web.DataReader('TLT', 'yahoo', start, end)["Close"]).values.tolist()
    spy = pd.DataFrame(web.DataReader('SPY', 'yahoo', start, end)).values.tolist()

    values_merged = []
    # TLT has the least amount of data so I can't zip them and have to loop for the length of tlt.
    for i in range(-len(tlt_close),0,1):
        values_merged.append([vix_close[i],tlt_close[i][0],spy[i][2],spy[i][0],spy[i][1],spy[i][3],spy[i][4]])
    
    #working with list
    values_merged = recode_volatility(values_merged)
    values_merged = add_gap_main_list(values_merged)
    values_merged = close_extreme_boolean(values_merged)
    values_merged = close_held_open_rate(values_merged)

    #list to data frame
    values_merged = pd.DataFrame(values_merged)
    values_merged.columns = ["VIX","VIX_Coded","TLT","Open","High","Low","Close","Volume","Chng","Cl_Ex","Wrong"]

    #working with data frame 
    values_merged = calculate_rvol(values_merged)
    values_merged = calculate_atr(values_merged)
    values_merged = compare_range_to_atr(values_merged)
    values_merged.columns = ["VIX","VIX_Coded","TLT","Open","High","Low","Close","Volume","Chng","Cl_Ex","Wrong","Rvol","ATR","Rrng"]
    values_merged = values_merged[19:len(values_merged)]
    return(values_merged)

def recode_volatility(lst:list):
    vix_states_counter = []
    vix_codes = {1:range(0,10),2:range(10,20),3:range(20,30),4:range(30,40),5:range(40,50),6:range(50,200)}
    
    for i in range(len(lst)):
        vix_now = int(lst[i][0])
        for j in range(len(vix_codes)):
            if vix_now in vix_codes[j+1]:
                vix_coded = int(list(vix_codes.keys())[j])
                vix_states_counter.append(vix_coded)
                lst[i].insert(1,vix_coded)
    # print(vix_states_counter.count(1),vix_states_counter.count(2),vix_states_counter.count(3),vix_states_counter.count(4),vix_states_counter.count(5),vix_states_counter.count(6))
    return lst


def add_gap_main_list(lst:list):
    
    for i in range(len(lst)):
        try:
            open_today = lst[i][3]
            close_yday = lst[i-1][6]
            gap_percentage = float(f"{(open_today*100/close_yday)-100:.2f}")
            lst[i].append(gap_percentage)
        except IndexError:
            lst[i].append(0)
    return lst


def close_extreme_boolean(lst:list):
    for i in range(len(lst)):
        high, low, close = lst[i][4], lst[i][5], lst[i][6]
        daily_range = high-low
        if (high-close)/daily_range<=0.2:
            lst[i].append(1)
        elif (close-low)/daily_range<=0.2:
            lst[i].append(1)
        else:
            lst[i].append(0)
        # print(lst[i])
    return lst    
        

def close_held_open_rate(lst:list):
    for i in range(len(lst)):
        close_held_open = 0
        if i >= 100:
            for j in range(1,101):
                gap, close, open = lst[i-j][7], lst[i-j][6], lst[i-j][3]
                if (gap > 0 and close >= open) or (gap < 0 and close <= open):
                    close_held_open += 1
        lst[i].append(close_held_open)
    return lst



def calculate_rvol(df):
    df['Rvol'] = df['Volume']/df['Volume'].shift(1).rolling(window=20,min_periods=0).mean()
    return df

def calculate_atr(df): 
    
    aux = pd.DataFrame([])
    aux['m1'] = df['High']-df['Low']
    aux ['m2'] = abs(df['High']-df['Close'].shift(1))
    aux['m3'] = abs(df['Low']-df['Close'].shift(1))
    aux['TR'] = aux[['m1', 'm2', 'm3']].max(axis=1)
    df['ATR'] = aux['TR'].rolling(20,0).mean()
    del aux
    return df


def compare_range_to_atr(df):
    df = df.values.tolist()
    for i in range(len(df)):
        high = df[i][4]
        low = df[i][5]
        atr = df[i][12]
        range_compared_atr = 0
        try:
            range_compared_atr = (high-low)/atr
        except ZeroDivisionError:
            pass
        df[i].append(range_compared_atr)
    df = pd.DataFrame(df)
    return df

# def close_at_extreme_quantitative(df):
#     df["Close_extreme_q"] = df[]
#     print(df)

def closeExtremeRate(df):
    df["cl_ex_rate"] = df['Cl_Ex'].shift(1).rolling(3,3).sum()
    df = df[100:]
    print(df)