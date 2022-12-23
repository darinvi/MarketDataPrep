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

# def gapDownCloseUp(df):
#     # df_gap = df[(df['Gap']<0) & (df['Open']<df['MA50']) & (df['Close']>df['Open']) & (df['RR']>1) & (df['Rvol']>1)]
#     df_gap = df[(df['Gap']<0) & (df['Open']<df['MA50']) & (df['Close']>df['Open'])]
#     engulf = df_gap[df_gap['D2']==1]
#     print(len(df_gap))
#     print(len(engulf))
#     print(len(engulf)/len(df_gap))

def greenDayAfterRedDays(df):
    pass

def breakFakeAtMa(df):
    pass