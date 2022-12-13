import statsmodels.formula.api as smf


def regression(df,dep,indep):
    regg = smf.ols(formula=f"{dep} ~ {' + '.join(indep)}", data=df).fit()
    print(regg.summary())

def extremeCloseVixCounter(df):
    pass

def closeHeldGap(df_filltered):
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


