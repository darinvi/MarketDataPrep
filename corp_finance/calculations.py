import statsmodels.formula.api as smf


def simple_regression(df,dep,indep):
    
    regg = smf.ols(formula=f"{dep} ~ {' + '.join(indep)}", data=df).fit()
    print(regg.summary())

# def simple_regression(df,dep_var:str,indep_var:str):
    
#     dependent_variable = df[dep_var]
#     independent_variable = df[indep_var]
    
#     sm.add_constant(independent_variable)
#     est = sm.OLS(dependent_variable, independent_variable).fit()
#     print(est.summary())


def extreme_close_vix_counter(df):
    df = df.values.tolist()
    df_as_list = [int(df_as_list[1]) for df_as_list in df if df_as_list[9]>0]
    print(df_as_list.count(1),df_as_list.count(2),df_as_list.count(3),df_as_list.count(4),df_as_list.count(5),df_as_list.count(6))
    

def close_held_gap(df_filltered):
    df_filltered = df_filltered.values.tolist()
    gap_held_counter = 0
    for i in range(len(df_filltered)):
        gap = df_filltered[i][8]
        close_extreme = df_filltered[i][9]
        gap_held = bool((gap < 0 and close_extreme == 2) or (gap > 0 and close_extreme == 1))
        print(gap,close_extreme,gap_held)
        if gap_held:
            gap_held_counter += 1
    print(gap_held_counter,len(df_filltered),f"{gap_held_counter/len(df_filltered)*100:.2f}%")
