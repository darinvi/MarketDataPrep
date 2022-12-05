from data_preparation import market_values_list,closeExtremeRate
from calculations import simple_regression,extreme_close_vix_counter,close_held_gap
import pandas as pd
from stuff import expected_range
from filtered_data import gaps_outside_st

market_values = market_values_list()

# extreme_close_vix_counter(market_values)

# print(sum(market_values["Close_Extreme"]))


# arr = gaps_outside_st(market_values)
# simple_regression(arr,"Rrng",[])
# simple_regression(market_values,"Close_Extreme",['Chng','Rrng','Rvol','VIX_Coded'])

closeExtremeRate(market_values)