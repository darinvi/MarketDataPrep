from data_preparation import marketValuesList

df = marketValuesList()
df_bool = df[['Held_Open','Trend_bool','RVOL_bool','Gap_bool','ExCl','D2']]
print(df_bool['D2'].value_counts())