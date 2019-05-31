import random, json, math
from random import choice, random

def random_values(min, max):
	'''
	This function returns a random value biased towards lower end of given range.
	'''
	return round((abs(random() - random()) * (1 + max - min) + min), 2)
        
opt_no = ['Y'] * 1 + ['N'] * 9
opt_yes = ['Y'] * 9 + ['N'] * 1

class Item:
	def __init__(self):
		self.ItemWeight_lbs = random_values(2, 23)                 #weight in lbs
		self.ItemLength = random_values(2, 22)                     #length of item in inches
		self.ItemBreadth = random_values(2, 15)                    #breath of item in inches
		self.ItemHeight = random_values(2, 17)                     #height of item in inches
		self.Itemprice = 0
		if( choice(opt_yes) == 'Y' ):
			self.Itemprice = random_values(100, 5000);
		else:	
			self.ItemPrice = random_values(100, 5000 * 70)         #price in rupess max limit is 350000 but item price should be less than 300000
		self.isHazardous = choice(opt_no)
		self.isFullFilledByAmazon = choice(opt_yes)
		self.isSubscribed = choice(opt_no)
		self.CountryName = 'India'
		self.isReleaseDate = choice(opt_no)

item_dictionary = {}
id_prim = 1
for i in range(100000):
	box = Item()
	box_json = json.dumps(box.__dict__)
	item_dictionary[id_prim] = json.loads(box_json)
	id_prim = id_prim + 1

fd = open("items.json", 'w')
json.dump(item_dictionary, fd, indent=4)
