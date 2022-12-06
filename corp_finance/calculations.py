import statsmodels.formula.api as smf


def simpleRegression(df,dep,indep):
    regg = smf.ols(formula=f"{dep} ~ {' + '.join(indep)}", data=df).fit()
    print(regg.summary())

def extremeCloseVixCounter(df):
    pass

def closeHeldGap(df_filltered):
    pass