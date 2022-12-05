import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import statsmodels.api as sm

def expected_range(data_frame):

    range_and_volume = []
    
    for i in range(16,len(data_frame)):
        
        average_true_range = 0
        # for j in range(1,15):
        #     true_ranges = max([abs(data_frame['High'][i-j] - data_frame['Low'][i-j]),abs(data_frame['High'][i-j] - data_frame['Close'][i-j-1]),\
        #         abs(data_frame['Low'][i-j] - data_frame['Close'][i-j-1])])
        #     average_true_range += true_ranges
        # average_true_range /= 14
        
        range_compared_to_atr_no_gap = (data_frame['High'][i]-data_frame['Low'][i])/average_true_range
        true_range_today_compared_with_gap = max([data_frame['High'][i]-data_frame['Low'][i],abs(data_frame['High'][i]-data_frame['Close'][i-1]),\
            abs(data_frame['Low'][i]-data_frame['Close'][i-1])])/average_true_range
        range_and_volume.append([range_compared_to_atr_no_gap, true_range_today_compared_with_gap, data_frame['Rvol'][i]])


    range_volume_as_df = pd.DataFrame(range_and_volume, columns=['RANGE/ATR_NO-GAP','RANGE/ATR_GAP','RVOL'])
    print(range_volume_as_df.head())
    dependent_variable = range_volume_as_df.iloc[:,1].values.reshape(-1,1)
    explanatory_variable = range_volume_as_df.iloc[:,2].values.reshape(-1,1)
    plt.figure(figsize=(16, 8))
    plt.scatter(range_volume_as_df['RVOL'],range_volume_as_df['RANGE/ATR_NO-GAP'],c='black')
    plt.xlabel("RVOL")
    plt.ylabel("ATR")
    plt.show()

    constant = sm.add_constant(explanatory_variable)
    estimate = sm.OLS(dependent_variable,constant).fit()
    print(estimate.summary())


