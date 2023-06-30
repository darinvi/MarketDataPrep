from data_preparation import marketValuesDataFrame
import statsmodels.formula.api as smf


def regression(df,dep,indep):
    regg = smf.ols(formula=f"{dep} ~ {' + '.join(indep)}", data=df).fit()
    print(regg.summary())


# takes user input for the variables to be used for fitting
def choosingVariablesForRegression(df):
    all_variables = mapColNameToExplanatoryList(df)
    for inx,val in enumerate(df.columns):
        print(inx+1,val)
    dependent_variable = input('\nPlease choose the index of the dependent variables to fit a regression.\n')
    explanatory_variables = list(map(int,input('\nPlease choose the indexes of the explanatory variables split by space!\n').split()))
    dependent_variable = all_variables[int(dependent_variable)]
    explanatory_variables = list(map(lambda x: all_variables[x],explanatory_variables))
    return dependent_variable,explanatory_variables


# required for easier UI when choosing variables
def mapColNameToExplanatoryList(df):
    colnames = {key:val for (key,val) in zip(range(1,len(df.columns)+1),df.columns)}
    return colnames


def run_multiple_regression():
    df = marketValuesDataFrame()
    dependent, independent = choosingVariablesForRegression(df)
    regression(df, dependent, independent)


run_multiple_regression()