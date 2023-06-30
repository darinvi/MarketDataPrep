# Allows for filtering gaps based on the standard deviation.
# Multiplicator is used to filter at how many standard deviations away the gap should be. 
# e.g. multiplicator = 2 will result in a dataframe that contains all rows where the gap was more than 2 standard deviations away from mean
def gapsRelativeToStandardDeviation(df,multiplicator):
    return df[(df['Gap']>df['Gap_mean']+df['Gap_std']*multiplicator) | (df['Gap']<df['Gap_mean']-df['Gap_std']*multiplicator)]


# Filter the dataframe by VIX (volatility indicator) encoded value. (1-5)
def filterByVixValue(df,value):
    df_filteed = df[df['V_coded']==value]
    return df_filteed


# Get a dataframe containing the rows that were preceeded by at least two red or green days.
# Can be used for testing mean reversion strategies.
def filterConsecutiveRedDays(df, direction):
    for i in range(1,4):
        df[f'yd{i}'] = df['Close'].shift(i)
    if direction == 'down':
        return df[(df['yd1']<df['yd2'])&(df['yd2']<df['yd3'])]
    elif direction == 'up':
        return df[(df['yd1']>df['yd2'])&(df['yd2']>df['yd3'])]
