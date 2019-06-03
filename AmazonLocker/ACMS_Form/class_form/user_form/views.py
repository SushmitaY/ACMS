import pandas as pd
from django.shortcuts import render
from user_form import classification

# Create your views here.

def Reccommendation(model, pred_acc):
	feedback_data = pd.read_csv("feedback.csv", error_bad_lines = False)
	unpredected_data = feedback_data.tail(1)
	feedback_data = feedback_data.iloc[:-1, :]
	feedback_data.to_csv('feedback.csv', index=False)
	
	unpredected_data['isLockerRecommended'] = pred_acc[0]
	if pred_acc[0] == 0:
		unpredected_data['isLockerUsed'] = 0
	with open('feedback.csv', 'a') as f:
		unpredected_data.to_csv(f, header=False, index=False)
		
	if pred_acc[0] == 1:
		content = {
			'model': model,
			'prediction': "Locker is Recommended",
			'predictionBool' : pred_acc[0], 
			'accuracy': pred_acc[1]
		}
	else:
		
		content = {
			'model': model,
			'prediction': "Locker is Not Recommended",
			'predictionBool' : pred_acc[0],
			'accuracy': pred_acc[1]
		}

	return content

def Classify(request):
	
	user_data = {}
	user_data['Transaction_ID'] = int(request.POST.get('Transaction_ID'))
	user_data['Address(Home/Office)'] = int(request.POST.get('Address'))
	user_data['Item_Weight'] = float(request.POST.get('Item_Weight'))
	user_data['Item_Length'] = float(request.POST.get('Item_Length'))
	user_data['Item_Breadth'] = float(request.POST.get('Item_Breadth'))
	user_data['Item_Height'] = float(request.POST.get('Item_Height'))
	user_data['Item_Price'] = float(request.POST.get('Item_Price'))
	user_data['Hazardous'] = int(request.POST.get('Hazardous'))
	user_data['FulfilledByAmazon'] = int(request.POST.get('FulfilledByAmazon'))
	user_data['Subscribed'] = int(request.POST.get('Subscribed'))
	user_data['ReleaseDate'] = int(request.POST.get('ReleaseDate'))
	
	with open('feedback.csv', 'a') as feedback_data:
		pd.DataFrame(user_data, index=[0]).to_csv(feedback_data, header=False, index=False)
    
	if request.POST.get('Models') == 'Bayes':
		pred_acc = classification.Gaussian(request)
		content = Reccommendation("Gaussian Naive Bayes Model",pred_acc)
		return render(request, 'hello.html',content)
	elif request.POST.get('Models') == 'Logistic':
		pred_acc = classification.Logistic_Regression(request)
		content = Reccommendation("Logistic Regression Model", pred_acc)
		return render(request, 'hello.html',content)
	elif request.POST.get('Models') == 'Rfc':
		pred_acc = classification.rfc(request)
		content = Reccommendation("Random Forest Classifier Model", pred_acc)
		return render(request, 'hello.html',content)
	elif request.POST.get('Models') == 'Knn':
		pred_acc = classification.knn(request)
		content = Reccommendation("K-Nearest Neighbour Model", pred_acc)
		return render(request, 'hello.html',content)
	elif request.POST.get('Models') == 'Tree':
		pred_acc = classification.decision_tree(request)
		content = Reccommendation("Decision Tree Model", pred_acc)
		return render(request, 'hello.html',content)

def SaveFeedback(request):
	
	feedback_data = pd.read_csv("feedback.csv", error_bad_lines = False)
	unfed_data = feedback_data.tail(n=1)
	unfed_data['isLockerUsed'] = request.POST.get('feedback')
	feedback_data = feedback_data.iloc[:-1]
	feedback_data.to_csv('feedback.csv', index=False)
	
	with open('feedback.csv', 'a') as f:
		unfed_data.to_csv(f, header=False, index=False)
		
	return render(request, 'final.html')
	
def homepage(request):
	return render(request, 'form.html')
