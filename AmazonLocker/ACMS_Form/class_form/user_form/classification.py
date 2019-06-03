import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier 
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier as DTC
import seaborn as sns
import numpy as np
import pandas as pd

# --------------Reading CSV---------------- #

orders_data = pd.read_csv('orders.csv', error_bad_lines = False)
#orders_data
#orders_data = orders_data.drop(['Unnamed: 0'],axis =1)
orders_data = orders_data.drop(['address_line1', 'address_line2', 'landmark'], axis = 1)
replace_map_Y = {'isLockerRecommended' : {'Y' : 1, 'N' : 0}}
orders_data.replace(replace_map_Y, inplace = True)
orders_Y = orders_data.iloc[:,21] #isLockerRecommended
orders_X = orders_data.iloc[:, 9:20]
orders_X['TransactionID'] = orders_data['TransactionID']
orders_X.drop(['CountryName'], axis = 1)
column_titles = ['TransactionID','address_type', 'ItemWeight_lbs','ItemLength', 'ItemBreadth', 'ItemHeight', 'Itemprice', 'isHazardous', 'isFullFilledByAmazon', 'isSubscribed', 'isReleaseDate']
orders_X = orders_X.reindex(columns = column_titles)
#-------------------Cleaning ------------------- #

#print(orders_X.isnull().sum()) #No Null Values
#orders_X['address_type'].value_counts() #Frequency Of Each Categorical Value

#Converting Binary Categorial Attributes into Binary Numerical Attributes

# Address_Type attribute has two categorical values office and home
replace_map_X = {'address_type' : {"Home" : 1, "Office" : 0}, 'isHazardous' : {'Y' : 1, 'N': 0}, 'isFullFilledByAmazon' : {'Y' : 1, 'N': 0}, 'isSubscribed' : {'Y' : 1, 'N': 0}, 'isReleaseDate' : {'Y' : 1, 'N': 0}}
orders_X.replace(replace_map_X, inplace = True)
#orders_Y.head()
orders_X_train, orders_X_test, orders_Y_train, orders_Y_test = train_test_split(orders_X, orders_Y, random_state = 0)
#orders_Y_train

#------------------------- Naive Bayes Classifier ------------------------- #
def Gaussian(request):
	gnb = GaussianNB()
	bayes_model = gnb.fit(orders_X_train, orders_Y_train)
	#Prediction

	predictions = bayes_model.predict(orders_X_test)
	bayes_accuracy = accuracy_score(orders_Y_test, predictions)

	#Precision
	bayes_precision = metrics.precision_score(orders_Y_test, predictions, pos_label = 1)

	#Recall
	bayes_recall = metrics.recall_score(orders_Y_test, predictions, pos_label = 1)

	#F-Score
	bayes_fscore = metrics.f1_score(orders_Y_test, predictions, pos_label = 1)

	user_data = []
	user_data.append(int(request.POST.get('Transaction_ID')))
	user_data.append(int(request.POST.get('Address')))
	user_data.append(float(request.POST.get('Item_Weight')))
	user_data.append(float(request.POST.get('Item_Length')))
	user_data.append(float(request.POST.get('Item_Breadth')))
	user_data.append(float(request.POST.get('Item_Height')))
	user_data.append(float(request.POST.get('Item_Price')))
	user_data.append(int(request.POST.get('Hazardous')))
	user_data.append(int(request.POST.get('FulfilledByAmazon')))
	user_data.append(int(request.POST.get('Subscribed')))
	user_data.append(int(request.POST.get('ReleaseDate')))
	user_prediction = bayes_model.predict([user_data])
	return [int(user_prediction), bayes_accuracy*100]
# -------------------------- Logistic Regression --------------------------#

def Logistic_Regression(request):
	lr = LogisticRegression()
	logit_model = lr.fit(orders_X_train, orders_Y_train)


	predictions = logit_model.predict(orders_X_test)

	logit_accuracy = accuracy_score(orders_Y_test, predictions)

	#Precision
	logit_precision = metrics.precision_score(orders_Y_test, predictions, pos_label = 1)

	#Recall
	logit_recall = metrics.recall_score(orders_Y_test, predictions, pos_label = 1)

	#F-Score
	logit_fscore = metrics.f1_score(orders_Y_test, predictions, pos_label = 1)

	user_data = []
	user_data.append(int(request.POST.get('Transaction_ID')))
	user_data.append(int(request.POST.get('Address')))
	user_data.append(float(request.POST.get('Item_Weight')))
	user_data.append(float(request.POST.get('Item_Length')))
	user_data.append(float(request.POST.get('Item_Breadth')))
	user_data.append(float(request.POST.get('Item_Height')))
	user_data.append(float(request.POST.get('Item_Price')))
	user_data.append(int(request.POST.get('Hazardous')))
	user_data.append(int(request.POST.get('FulfilledByAmazon')))
	user_data.append(int(request.POST.get('Subscribed')))
	user_data.append(int(request.POST.get('ReleaseDate')))
	user_prediction = logit_model.predict([user_data])
	return [user_prediction,logit_accuracy*100]

# ------------------ Random Forest Classifier --------------------------- #

def rfc(request):
	rfc_model = RandomForestClassifier()
	rfc_model = rfc_model.fit(orders_X_train, orders_Y_train)

	predictions = rfc_model.predict(orders_X_test)

	rfc_accuracy = accuracy_score(orders_Y_test, predictions)

	#Precision
	rfc_precision = metrics.precision_score(orders_Y_test, predictions, pos_label = 1)

	#Recall
	rfc_recall = metrics.recall_score(orders_Y_test, predictions, pos_label = 1)

	#F-Score
	rfc_fscore = metrics.f1_score(orders_Y_test, predictions, pos_label = 1)

	user_data = []
	user_data.append(int(request.POST.get('Transaction_ID')))
	user_data.append(int(request.POST.get('Address')))
	user_data.append(float(request.POST.get('Item_Weight')))
	user_data.append(float(request.POST.get('Item_Length')))
	user_data.append(float(request.POST.get('Item_Breadth')))
	user_data.append(float(request.POST.get('Item_Height')))
	user_data.append(float(request.POST.get('Item_Price')))
	user_data.append(int(request.POST.get('Hazardous')))
	user_data.append(int(request.POST.get('FulfilledByAmazon')))
	user_data.append(int(request.POST.get('Subscribed')))
	user_data.append(int(request.POST.get('ReleaseDate')))
	user_prediction = rfc_model.predict([user_data])
	return [int(user_prediction), rfc_accuracy*100]


# ------------------------- KNN Classifiers --------------------------- #
def knn(request):
	knn_model = KNeighborsClassifier(n_neighbors=3)
	knn_model = knn_model.fit(orders_X_train, orders_Y_train)

	predictions = knn_model.predict(orders_X_test)

	knn_accuracy = accuracy_score(orders_Y_test, predictions)

	#Precision
	knn_precision = metrics.precision_score(orders_Y_test, predictions, pos_label = 1)

	#Recall
	knn_recall = metrics.recall_score(orders_Y_test, predictions, pos_label = 1)

	#F-Score
	knn_fscore = metrics.f1_score(orders_Y_test, predictions, pos_label = 1)

	user_data = []
	user_data.append(int(request.POST.get('Transaction_ID')))
	user_data.append(int(request.POST.get('Address')))
	user_data.append(float(request.POST.get('Item_Weight')))
	user_data.append(float(request.POST.get('Item_Length')))
	user_data.append(float(request.POST.get('Item_Breadth')))
	user_data.append(float(request.POST.get('Item_Height')))
	user_data.append(float(request.POST.get('Item_Price')))
	user_data.append(int(request.POST.get('Hazardous')))
	user_data.append(int(request.POST.get('FulfilledByAmazon')))
	user_data.append(int(request.POST.get('Subscribed')))
	user_data.append(int(request.POST.get('ReleaseDate')))
	user_prediction = knn_model.predict([user_data])
	return [int(user_prediction), knn_accuracy*100]

# ------------------------- Decision Tree --------------------------- #

#max_depth = 3 - 78.508, 4 - 85.72, 5 - 91.184, 6 - 94.948, 7 - 97.072, 8 - 98.872
def decision_tree(request):
	tree_model = DTC(max_depth = 8)#DTC(DecisionTreeClassifier)
	tree_model = tree_model.fit(orders_X_train, orders_Y_train)

	predictions = tree_model.predict(orders_X_test)

	tree_accuracy = accuracy_score(orders_Y_test, predictions)

	#Precision
	tree_precision = metrics.precision_score(orders_Y_test, predictions, pos_label = 1)

	#Recall
	tree_recall = metrics.recall_score(orders_Y_test, predictions, pos_label = 1)

	#F-Score
	tree_fscore = metrics.f1_score(orders_Y_test, predictions, pos_label = 1)

	user_data = []
	user_data.append(int(request.POST.get('Transaction_ID')))
	user_data.append(int(request.POST.get('Address')))
	user_data.append(float(request.POST.get('Item_Weight')))
	user_data.append(float(request.POST.get('Item_Length')))
	user_data.append(float(request.POST.get('Item_Breadth')))
	user_data.append(float(request.POST.get('Item_Height')))
	user_data.append(float(request.POST.get('Item_Price')))
	user_data.append(int(request.POST.get('Hazardous')))
	user_data.append(int(request.POST.get('FulfilledByAmazon')))
	user_data.append(int(request.POST.get('Subscribed')))
	user_data.append(int(request.POST.get('ReleaseDate')))
	user_prediction = tree_model.predict([user_data])
	return [int(user_prediction), tree_accuracy*100]
