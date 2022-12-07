import data_preparation as dp
import calculations as cl
import filtered_data as fd

df = dp.marketValuesList()

# extreme_close_vix_counter(df)

# print(sum(df["Close_Extreme"]))

# cl.regression(df,"RR",['Gap','ATR','AR','V_coded','Rvol'])

# closeExtremeRate(df)
# close_rate = df['ExCl_Rate'].values.tolist()
# for i in range(len(df['High'])):
#     print(df['ExCl_Rate'][i:i+1])


# # print(df['V_coded'].unique())

cl.openHeldBasedOnVix(df)