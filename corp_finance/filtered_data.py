import statistics
import pandas as pd

def gaps_outside_st(df):
    standard_deviation = statistics.stdev(df["Chng"])
    average_gap = statistics.mean(df["Chng"])
    df = df.values.tolist()
    df_filltered = []
    for i in range(len(df)):
        if df[i][8] > average_gap + standard_deviation or df[i][8] < average_gap - standard_deviation:
            df_filltered.append(df[i])
    df_filltered = pd.DataFrame(df_filltered)
    df_filltered.columns = ["VIX","VIX_Coded","TLT","Open","High","Low","Close","Volume","Chng","Close_Extreme","Wrong","Rvol","ATR","Rrng"]
    return df_filltered


