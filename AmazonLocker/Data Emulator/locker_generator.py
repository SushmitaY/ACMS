from JSONEncoder import *

class Locker:
    def __init__(self, locker_name, locker_pincode, locker_taluk, locker_district, locker_state, locker_availability):
    	self.locker_name = locker_name
    	self.locker_pincode = locker_pincode
    	self.locker_taluk = locker_taluk
    	self.locker_district = locker_district
    	self.locker_state = locker_state
    	self.locker_availability = locker_availability
    	#self.locker_slots = locker_slots # Max no of slots let 10

pincode_dict = None
f = open('india_pincode.json', 'r')
pincode_dict = json.load(f)

lockers = {}

def get_locker_information():
	id_prim = 1
	availability = ['Y']*49 + ['N']
	for keys in pincode_dict.keys():
		locker_pincode = keys
		locker_taluk = pincode_dict[keys]['taluk']
		locker_district = pincode_dict[keys]['district']
		locker_state = pincode_dict[keys]['state']
		locker_availability = random.choice(availability)
		locker_name = locker_pincode + " " + locker_taluk + " " + locker_district + " " + locker_state
		locker_object = Locker(locker_name, locker_pincode, locker_taluk, locker_district, locker_state, locker_availability)
		locker_json = toJSON(locker_object)
		lockers[locker_pincode] = locker_json
		id_prim = id_prim + 1
	return lockers
	
lockers = get_locker_information()
f =open("lockers.json", 'w')
json.dump(lockers, f, indent=4)
