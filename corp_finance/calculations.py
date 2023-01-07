import statsmodels.formula.api as smf

def regression(df,dep,indep):
    regg = smf.ols(formula=f"{dep} ~ {' + '.join(indep)}", data=df).fit()
    print(regg.summary())

def distributionBasedOnVix(df,col):
    for val in range(1,6):
        ultra_filtered = df[(df[col]!=0) & (df['V_coded']==val)]
        slightly_filtered = df[df['V_coded']==val]
        l1 = len(ultra_filtered)
        l2 = len(slightly_filtered)
        print(l1,l2)
        print(l1/l2)

def extremeCloseContinuation(df,rvol,direction):
    if direction.lower() == 'fade':
        multiplier = -1
    elif direction.lower() == 'hold':
        multiplier = 1
    fade_and_extreme = df[(df['ExCl']==multiplier*(df['Gap']/abs(df['Gap']))) & (df['Rvol']>rvol)]
    fade_and_extreme_continuation = df[(df['ExCl']==multiplier*(df['Gap']/abs(df['Gap']))) & (df['D2']==1) & (df['Rvol']>rvol)]
    print(len(fade_and_extreme_continuation),len(fade_and_extreme))
    print(f'{len(fade_and_extreme_continuation)/len(fade_and_extreme)*100:.2f}%')

def gapDownCloseUp(df):
    # df_gap = df[(df['Gap']<0) & (df['Low']<df['MA50']) & (df['Close']>df['YCl'])]
    df_gap = df[(df['Open']>df['MA50']) & (df['Low']<df['MA50']) & (df['Close']>df['Open'])]
    engulf = df_gap[df_gap['D2']==1]
    print(len(df_gap))
    print(len(engulf))
    print(len(engulf)/len(df_gap))

def filterConsecutiveRedDays(df):
    for i in range(1,5):
        df[f'yd{i}'] = df['Close'].shift(i)
    df = df[(df['yd1']<df['yd2'])&(df['yd2']<df['yd3'])]
    # df = df[(df['yd1']<df['yd2'])&(df['yd2']<df['yd3'])&(df['yd3']<df['yd4'])]
    return df

def gapUpAfterRedDays(df):
    gap_up = df[df['Gap']>0]
    # gap_held = gap_up[(gap_up['Close']>gap_up['Open'])&(gap_up['ExCl']==1)]
    gap_held = gap_up[(gap_up['Close']>gap_up['Open'])]
    df = df.drop(['yd1','yd2','yd3','yd4'],axis=1)
    print(len(gap_held))
    print(len(gap_up))
    print(f'{len(gap_held)/len(gap_up):.2f}%')

def greenDayAfterRedDays(df):
    # gap_up = df[(df['Close']>df['Open'])&(df['Gap']>0)&(df['D2']==1)&(df['ExCl']==1)]
    # green_day = df[(df['Close']>df['Open'])&(df['Gap']>0)&(df['ExCl']==1)]
    gap_up = df[(df['Close']>df['Open'])&(df['Gap']>0)&(df['D2']==1)]
    green_day = df[(df['Close']>df['Open'])&(df['Gap']>0)]
    df = df.drop(['yd1','yd2','yd3','yd4'],axis=1)
    print(len(gap_up))
    print(len(green_day))
    print(f'{len(gap_up)/len(green_day):.2f}%')

def breakFakeAtMa(df):
    pass

def trueRangeRelativeToAtr(df):
    # larger_range = df[df['TR']>df['ATR']]
    larger_range = df[df['Range']>df['AR']]
    print(len(larger_range))
    print(len(df))
    print(len(larger_range)/len(df))

# def invasionBackTest(df):
#     down_days = df[
#         (df['Close'].shift(1)<df['Close'].shift(2)) &
#         (df['Close'].shift(2)<df['Close'].shift(3)) &
#         (df['Close'].shift(3)<df['Close'].shift(4)) &
#         (df['Close'].shift(4)<df['Close'].shift(5)) &
#         (((df['Close'].shift(5)-df['Open'])/df['Close'].shift(5))<0.1) &
#         (((df['Close'].shift(5)-df['Open'])/df['Close'].shift(5))>0.05) &
#         (df['Gap']<(df['Gap_mean']-df['Gap_std']))
#     ]
#     close_up = down_days[
#         down_days['Close']>down_days['Close']
#     ]
#     print(close_up)

def invasionBackTest(df):
    down_days = df[
        (df['Close'].shift(1)<df['Close'].shift(2)) &
        (df['Close'].shift(2)<df['Close'].shift(3)) &
        (df['Close'].shift(3)<df['Close'].shift(4)) &
        (df['Close'].shift(4)<df['Close'].shift(5)) &
        (((df['Close'].shift(5)-df['Open'])/df['Close'].shift(5))<0.1) &
        (((df['Close'].shift(5)-df['Open'])/df['Close'].shift(5))>0.05) &
        (df['Gap']<(df['Gap_mean']-df['Gap_std']))
    ]
    close_up = down_days[
        down_days['Close']>down_days['Close']
    ]
    print(close_up)
    print(down_days)

def averageHigh(df):
    df['High_distance'] = (df['High'] - df['Open'])/df['AR']
    df['Low_distance'] = (df['Open'] - df['Low'])/df['AR']
    print(f'Avg.High: {df["High_distance"].mean()}*AR')
    print(f'Avg.Low: {df["Low_distance"].mean()}*AR')