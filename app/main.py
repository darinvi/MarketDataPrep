import data_preparation as dp
import calculations as cl
import filtered_data as fd
import multiple_regression as mr

df = dp.marketValuesDataFrame()
print(df)
print(df.columns)
# df.to_parquet("../market_data.parquet")

# df = df[df['Gap']>0]
# df_std= fd.gapsRelativeToStandardDeviation(df,'out',2)
# print(len(df_std))
# print(len(df))
# print(len(df_std)/len(df))

# df_held = df_std[(df_std['Gap']>0)&(df_std['Held_Open']==1)&(df_std['ExCl']==1)]
# df_second_day = df_held[df_held['D2']==1]
# df_held = df_std[(df_std['Held_Open']==1)]
# print(len(df_second_day))
# print(len(df_held))
# print(len(df_second_day)/len(df_held))
# print(len(df_held))

# df = fd.downTrend(df,100,200)
# df= df[(df['Gap']>0)]

# df_std= df_std[(df_std['Gap']<0) & (df_std['ExCl']==1)]
# df_cont= df_std[df_std['D2']==1]
# df= fd.gapsRelativeToStandardDeviation(df,'out',1)


# df_pull = fd.filterConsecutiveRedDays(df)
# df_pull = df_pull[df_pull['MA100']>df_pull['MA200']]
# df_pull = df_pull[df_pull['VIX']<20]
# cl.gapUpAfterRedDays(df_pull)
# cl.greenDayAfterRedDays(df_pull)
# cl.gapDownCloseUpSecondDay(df_pull)

# print(len(df))
# cl.trueRangeRelativeToAtr(df)

# df = df[df['Gap']>0]
# held_df = fdf[fdf['Held_Open']==1]
# print(len(fdf),len(held_df),len(held_df)/len(fdf))
# cl.extremeCloseContinuation(fdf,1,'hold')

# print(df['VIX'].mean())
# print(df['VIX'].std())

# cl.regression(df,"AR",['VIX'])
# cl.regression(df,"AR",['V_coded'])
# cl.regression(df,"RR",['Gap','Rvol'])
# cl.distributionBasedOnVix(df,'ExCl')
# cl.distributionBasedOnVix(df,'Held_Open')

# print(df[780:782])
# print(df[1780:1782])
# print(df[2780:2782])
# print(df[3780:3782])
# print(df[4780:4782])
# print(df[5780:5782])
# print(df[6780:6782])

# print(df['ExCl'].unique())
# print(df['D2'].unique())
# print(len(df_cont),