import data_preparation as dp
import calculations as cl
import filtered_data as fd

market_values = dp.marketValuesList()

# extreme_close_vix_counter(market_values)

# print(sum(market_values["Close_Extreme"]))


# cl.simple_regression(market_values,"RR",['Gap','ATR','AR','V_coded','Rvol'])
# simple_regression(market_values,"Close_Extreme",['Chng','Rrng','Rvol','VIX_Coded'])

# closeExtremeRate(market_values)
# close_rate = market_values['ExCl_Rate'].values.tolist()
# for i in range(len(market_values['High'])):
#     print(market_values['ExCl_Rate'][i:i+1])

print(market_values)