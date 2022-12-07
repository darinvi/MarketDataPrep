import statsmodels.formula.api as smf


def regression(df,dep,indep):
    regg = smf.ols(formula=f"{dep} ~ {' + '.join(indep)}", data=df).fit()
    print(regg.summary())

def extremeCloseVixCounter(df):
    pass

def closeHeldGap(df_filltered):
    pass

def openHeldBasedOnVix(df):
    filtered = {1:0/len(df[df['V_coded']==1]),\
        2:0/len(df[df['V_coded']==2]),\
            3:0/len(df[df['V_coded']==3]),\
                4:0/len(df[df['V_coded']==4]),\
                    5:0/len(df[df['V_coded']==5]),\
                        6:0/len(df[df['V_coded']==6])}

    for val in range(1,7):
        # I am in a hurry to finish my presentation, should rename those variables
        ultra_filtered = df[(df['Held_Open']!=0) & (df['V_coded']==val)]
        slightly_filtered = df[df['V_coded']==val]
        l1 = len(ultra_filtered)
        l2 = len(slightly_filtered)
        print(l1,l2)
        print(l1/l2)


