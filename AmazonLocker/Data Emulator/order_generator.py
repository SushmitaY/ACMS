import random
import json
from JSONEncoder import toJSON
from random import choice
from eligibility import isItemEligible, isLockerAvailable


fd_item = open("items.json",'r')
fd_locker = open("lockers.json", 'r') 
fd_user = open("users.json",'r')

item_dict = json.load(fd_item)
locker_dict = json.load(fd_locker)
user_dict = json.load(fd_user)

opt_yes = ['Y'] * 9 + ['N'] * 1
item_count = [1]*30 + [2] + [3]
last_digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class Order:
	def __init__(self, tid, userID, address, item, isDelivered):
		self.TransactionID = tid
		self.userID = userID
		self.address = address
		self.item = item		
		self.isDelivered = isDelivered		
		self.isLockerRecommended = None
		self.whichLockerRecommended = None
		self.isLockerUsed = None
		self.whichLockerUsed = None
    	
def random_order(tid):
	userID = random.choice(list(user_dict.keys()))
	userObj = user_dict[userID]
	address = userObj["address_list"][userObj["default_address"]]
	item_key = random.choice(list(item_dict.keys()))
	item_obj = item_dict[item_key] 
	item_obj["ASIN"] = 'ASIN' + str(item_key)	
	isDelivered = random.choice(opt_yes)
	orderObject = Order(tid, userID, address, item_obj, isDelivered)
		
	eligible = isItemEligible(orderObject.item) 
	if eligible and isLockerAvailable(orderObject.address):
		orderObject.isLockerRecommended = 'Y'
		pin = orderObject.address["pincode"]
		orderObject.whichLockerRecommended = locker_dict[pin]["locker_name"]
		orderObject.isLockerUsed = random.choice(opt_yes)
		if(orderObject.isLockerUsed == 'Y'):
			options = ['Y']*49 + ['N']
			if choice(options) == 'Y':
				orderObject.whichLockerUsed = locker_dict[pin]["locker_name"]
			else:
				print(pin)
				new_pin = pin[0:5] + str(choice(last_digit))
				while new_pin not in locker_dict.keys():
					new_pin = pin[0:5] + str(choice(last_digit))
				print(new_pin)
				orderObject.whichLockerUsed = locker_dict[new_pin]["locker_name"]
		else:
			orderObject.whichLockerUsed = None	
	else:
		orderObject.isLockerRecommended = 'N'
		orderObject.whichLockerRecommended = None
		orderObject.isLockerUsed = 'N'
		orderObject.whichLockerUsed = None
	return orderObject
	
order_dictionary = {}

for i in range(100):
	order_object = random_order(i+1)
	order_json = toJSON(order_object)
	order_dictionary[i+1] = order_json

fd = open("orders.json",'w')
json.dump(order_dictionary,fd,indent=4)
