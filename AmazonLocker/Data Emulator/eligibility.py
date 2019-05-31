import json
from datetime import datetime, timedelta
import time
import random

def isItemEligible(item):
	if item['ItemWeight_lbs'] < 20 and item['ItemLength'] < 19 and item['ItemBreadth'] < 12 and item['ItemHeight'] < 14 and item['isFullFilledByAmazon'] == 'Y' and item['Itemprice'] < 5000 * 65 and item['isHazardous'] == 'N' and item['isSubscribed'] == 'N' and item['CountryName'] == 'India' and item['isReleaseDate'] == 'N':
		return True
	else:
		return False		

f_locker = open("lockers.json", 'r')
locker_dict = json.load(f_locker)

def isLockerAvailable(address):
	pin = address["pincode"]
	return pin in locker_dict.keys() and locker_dict[pin]["locker_availability"] == 'Y'
