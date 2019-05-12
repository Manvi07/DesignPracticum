from sklearn import datasets 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
from GenerateDataset  import load_dataset

# loading dataset 
energy = load_dataset()
  
# X -> features
# Y -> label 
X = energy.data
Y = energy.target 
  
# dividing X, Y into train and test data 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.33, random_state = 42, shuffle = True) 
  
# training a DescisionTreeClassifier 
from sklearn.tree import DecisionTreeClassifier 
dtree_model = DecisionTreeClassifier(max_depth = 2).fit(X_train, Y_train) 

accuracy = dtree_model.score(X_test, Y_test) 
print 'Accuracy: ', accuracy

print(X_test)
dtree_predictions = dtree_model.predict(X_test) 
  
print(dtree_predictions)

# creating a confusion matrix 
# cm = confusion_matrix(Y_test, dtree_predictions) 

print(X_train)
print(dtree_model.predict(X_train))