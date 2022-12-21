import data_preparation as dp
import calculations as cl
import filtered_data as fd
import main_menu_functions as mm

df = dp.marketValuesList()

cl.regression(df,"RR",['Gap','ATR','AR','Rvol'])
# filtered_std = fd.gapsRelativeToStandardDeviation(df,'out',1)

# # print(df['V_coded'].unique())

# cl.openHeldBasedOnVix(df)

# cl.regression(df,"Held_Open",['Held_Rate'])
# cl.distributionBasedOnVix(df,'ExCl')
# cl.distributionBasedOnVix(df,'Held_Open')

# print(len(filtered_std))
# print(filtered_std['ExCl'].sum()/len(filtered_std))
# for i in range(len(filtered_std)):
#     print(filtered_std['Gap'][i:i+1])
#     print(filtered_std['Gap_mean'][i:i+1])
#     print(filtered_std['Gap_std'][i:i+1])

# cl.distributionBasedOnVix(filtered_std,'Held_Open')
# print(filtered_std)
# print(filtered_std['Gap'])

# mm.choosingVariablesForRegression(df)
# for i in range(len(df)):
#     print(df['ExCl_Rate'][i:i+1])

# print(df[df['Gap']<0])

# print(filtered_std[filtered_std['Gap'].rolling(200,0).mean()>0])



# print(df[780:782])
# print(df[1780:1782])
# print(df[2780:2782])
# print(df[3780:3782])
# print(df[4780:4782])
# print(df[5780:5782])
# print(df[6780:6782])