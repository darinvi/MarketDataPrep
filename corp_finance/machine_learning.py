from data_preparation import marketValuesList
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


df = marketValuesList()
df_bool = df[['Held_Open','Trend_bool','RVOL_bool','Gap_bool','ExCl','D2']]
# print(df_bool.head(30))

x = df_bool.iloc[:, :-1]
y = df_bool.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Create the decision tree model
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predict the values for the test set
y_pred = clf.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)