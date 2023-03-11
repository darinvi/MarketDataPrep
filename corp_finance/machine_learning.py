from data_preparation import marketValuesList
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import graphviz

df = marketValuesList()
df_bool = df[['Held_Open','Trend_bool','RVOL_bool','Gap_bool','ExCl','D2']]
# print(df_bool.head(30))

X_train, X_test, y_train, y_test = train_test_split(df_bool.iloc[:, :-1], df_bool.iloc[:, -1], test_size=0.2, random_state=42)
# print(y_train)

# # Create a decision tree classifier with max_depth of 3
# tree = DecisionTreeClassifier(max_depth=3, random_state=42)
# tree.fit(X_train, y_train)

# # Make predictions on the test set
# y_pred = tree.predict(X_test)

# # Calculate the accuracy of the classifier
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy)

# # Generate a Graphviz representation of the tree
# dot_data = export_graphviz(tree, out_file=None, 
#                            feature_names=X_train.columns.tolist(),
#                            class_names=['0', '1'], 
#                            filled=True, rounded=True,  
#                            special_characters=True)
# graph = graphviz.Source(dot_data)

# # Show the graph
# print(graph)