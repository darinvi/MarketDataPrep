import statsmodels.formula.api as smf


def regression(df,dep,indep):
    regg = smf.ols(formula=f"{dep} ~ {' + '.join(indep)}", data=df).fit()
    print(regg.summary())

def extremeCloseCounter(df):
    pass

def distributionBasedOnVix(df,col):
    for val in range(1,6):
        ultra_filtered = df[(df[col]!=0) & (df['V_coded']==val)]
        slightly_filtered = df[df['V_coded']==val]
        l1 = len(ultra_filtered)
        l2 = len(slightly_filtered)
        print(l1,l2)
        print(l1/l2)
    return df

def extremeCloseAndFadeContinuation(df,rvol):
    fade_and_extreme = df[(df['Held_Open']==0) & (df['ExCl']==-(df['Gap']/abs(df['Gap']))) & (df['Rvol']>rvol)]
    fade_and_extreme_continuation = df[(df['Held_Open']==0) & (df['ExCl']==-(df['Gap']/abs(df['Gap']))) & (df['D2']==1) & (df['Rvol']>rvol)]
    print(len(fade_and_extreme_continuation),len(fade_and_extreme))
    print(f'{len(fade_and_extreme_continuation)/len(fade_and_extreme)*100:.2f}%')

def extremeCloseAndContinuation(df,rvol):
    pass
