import data_preparation as dp
import calculations as cl
import filtered_data as fd
import main_menu_functions as mm


df = dp.marketValuesList()
# df = fd.upTrend(df)
# df= fd.gapsRelativeToStandardDeviation(df,'out',1)

df = cl.filterConsecutiveRedDays(df)
df = df[df['V_coded']==2]
# for i in range(1,6):
#     print(f'\n {i}')
#     df1 = df[(df['V_coded']==i)]
#     cl.gapUpAfterRedDays(df1)
#     cl.greenDayAfterRedDays(df1)

print(len(df))
cl.gapDownCloseUp(df)
# cl.trueRangeRelativeToAtr(df)

# df = df[df['Gap']>0]
# held_df = fdf[fdf['Held_Open']==1]
# print(len(fdf),len(held_df),len(held_df)/len(fdf))
# cl.extremeCloseContinuation(fdf,1,'hold')

# print(filtered_std)

# print(df['VIX'].mean())
# print(df['VIX'].std())

# cl.regression(df,"RR",['Gap','ATR','AR','Rvol'])
# cl.distributionBasedOnVix(df,'ExCl')
# cl.distributionBasedOnVix(df,'Held_Open')

# print(df[780:782])
# print(df[1780:1782])
# print(df[2780:2782])
# print(df[3780:3782])
# print(df[4780:4782])
# print(df[5780:5782])
# print(df[6780:6782])