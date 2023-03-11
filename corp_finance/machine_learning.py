from data_preparation import marketValuesList

df = marketValuesList()
df_bool = df[['Held_Open','Trend_bool','RVOL_bool','Gap_bool','ExCl']]
print(df_bool)