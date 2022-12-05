import data_preparation as dp
import calculations as cl
import filtered_data as fd

market_values = dp.marketValuesList()

# extreme_close_vix_counter(market_values)

# print(sum(market_values["Close_Extreme"]))


# arr = gaps_outside_st(market_values)
# simple_regression(arr,"Rrng",[])
# simple_regression(market_values,"Close_Extreme",['Chng','Rrng','Rvol','VIX_Coded'])

# closeExtremeRate(market_values)