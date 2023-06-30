import pandas as pd
import numpy as np
import math
from data_preparation import marketValuesDataFrame, prepareDataForNaive


# All possible combination of variable value and target value -> 0:0, 0:1, 1:0, 1:1
def calculate_r_values(train_data,feature,features):
    train_data = pd.DataFrame(train_data,columns=[*features,'target'])
    
    #split into two datasets, positive examples and negative examples
    p_exmp, n_exmp = train_data[train_data['target']==1], train_data[train_data['target']==0]
    
    #compute the R values for each combination feature-outcome; Laplace correction
    r11_val = (len(p_exmp[p_exmp[feature]==1])+1)/(len(p_exmp)+2)
    r01_val = 1 - r11_val
    r10_val = (len(n_exmp[n_exmp[feature]==1])+1)/(len(n_exmp)+2)
    r00_val = 1 - r10_val
    
    log_val = list(map(lambda x: math.log(x,10),[r11_val,r01_val,r10_val,r00_val]))
    return {'positive':{1:log_val[0],0:log_val[1]},'negative':{1:log_val[2],0:log_val[3]}}


#The score is calculated using r-values. It is used to make a prediction. 1 if S(1)>S(0) else 0
def handle_score_computations(row,scores,is_positive):
    score = 0
    for i,name in enumerate(list(scores.keys())):
        curr_score = scores[name]['positive'][row[i]] if is_positive else scores[name]['negative'][row[i]]
        score += curr_score
    return score


def cross_valiadtion(scores,test_data):
    right_answers = 0
    print(scores)
    # print(len(test_data))
    for el in test_data:
        score_positive = handle_score_computations(el,scores,True)
        score_negative = handle_score_computations(el,scores,False)
        expected = 1 if score_positive > score_negative else 0
        actual = el[-1]
        if expected == actual:
            right_answers += 1
    right_answers /= len(test_data)
    return right_answers


def run_naive_bayes(df, columns):
    df = prepareDataForNaive(df, columns)
    print(df.columns)
    features = list([e for e in df.columns if e!='D2'])
    print(features)
    df = np.array_split(np.array(df),10)
    correct_predictions = 0

    #using list-comprehensions and numpy.concatenate in order to cross-validate and get an average idea of the error term
    for i in range(len(df)):
        df_train = np.concatenate([el for indx,el in enumerate(df) if indx != i])
        df_test = np.array(*[el for indx,el in enumerate(df) if indx == i])
        scores = {feature:calculate_r_values(df_train,feature,features) for feature in features}
        correct_predictions += cross_valiadtion(scores,df_test)

    correct_predictions /= len(df)
    print(f'Average error = {(1 - correct_predictions)*100:.2f}% => {correct_predictions*100:.2f}% correct predictions')




# The choice of those features is based on my personal view and experience.
# I am trying to predict D2- whether the close tomorrow will be in the same direction as today's close.
columns = ['Held_Open','Trend_bool','RVOL_bool','Gap_bool','ExCl','D2']
df = prepareDataForNaive(marketValuesDataFrame(), columns)


# RUN THE MODEL:

run_naive_bayes(df, columns)
