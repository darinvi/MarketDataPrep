from data_preparation import marketValuesList
import math

def calculate_r_values(df,feature):
    #split into two datasets, positive examples and negative examples
    p_exmp, n_exmp = df[df['D2']==1], df[df['D2']==0]
    #compute the R values for each combination feature-outcome; Laplace correction
    r11_val = (len(p_exmp[p_exmp[feature]==1])+1)/(len(p_exmp)+2)
    r01_val = 1 - r11_val
    r10_val = (len(n_exmp[n_exmp[feature]==1])+1)/(len(n_exmp)+2)
    r00_val = 1 - r10_val
    log_val = list(map(lambda x: math.log(x,10),[r11_val,r01_val,r10_val,r00_val]))
    return {'positive':{1:log_val[0],0:log_val[1]},'negative':{1:log_val[2],0:log_val[3]}}

def handle_score_computations(row,scores,is_positive):
    score = 1
    for i in range(len(row)):
        curr_score = scores['positive'][row[i]] if is_positive else scores['negative'][row[i]]
        score *= curr_score
    return score

df = marketValuesList()

df_train = df[['Held_Open','Trend_bool','RVOL_bool','Gap_bool','ExCl','D2']][-1000:-200]
df_test = df[['Held_Open','Trend_bool','RVOL_bool','Gap_bool','ExCl','D2']][-200:].values.tolist()

features = list(df_train.columns)[:-1]

scores = {feature:calculate_r_values(df_train,feature) for feature in features}
print(scores)

answer_matches = 0

# for el in df_test:
#     score_positive = 1
#     score_negative = 1
#     inputs = el[:-1]
#     for ft in scores.items():
#         print(ft)