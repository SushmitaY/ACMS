import json
from random_features import randomDate, randomCountry, randomGender, randomPincode, randomPhone, getCity, \
    getState, randomAddType, generatePassword, generateEmail, randomOccupation, randomName, randomDefault, \
    randomAddressCount, toJSON


class Address:
    def __init__(self, full_name, mobile_number, pincode, address_line1, address_line2, landmark, city, state, country,
                 address_type):
        self.full_name = full_name
        self.mobile_number = mobile_number
        self.pincode = pincode
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.landmark = landmark
        self.city = city
        self.state = state
        self.country = country
        self.address_type = address_type

class User:
    def __init__(self, name, gender, date_of_birth, country, contact_number, email, password, occupation):
        self.name = name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.country = country
        self.contact_number = contact_number
        self.email = email
        self.password = password
        self.occupation = occupation
        self.address_list = []
        self.default_address = -1

    def add_address(self, new_address, is_default=False):
        self.address_list.append(new_address)
        if (is_default):
            self.default_address = len(User.address_list) - 1

    def set_default_address(self, addr_index):
        self.default_address = addr_index

def randomAddress(country="India"):
    pincode = randomPincode(country)
    city = getCity(pincode)
    state = getState(pincode)
    mobile_number = randomPhone()
    full_name = name = randomName(country)
    address_type = randomAddType()
    return Address(full_name, mobile_number, pincode, "", "", "", city, state, country, address_type)


def randomUser():
    dob = randomDate("1/1/1970", "1/1/2009")
    gender = randomGender()
    country = randomCountry()
    country = "India"
    name = randomName(country, gender)
    phone = randomPhone()
    email = generateEmail(name)
    occupation = randomOccupation()
    password = generatePassword()
    no_of_addresses = randomAddressCount()
    userObject = User(name, gender, dob, country, phone, email, password, occupation)
    for i in range(no_of_addresses):
        address = randomAddress("India")
        userObject.add_address(address)
    userObject.default_address = randomDefault(len(userObject.address_list))
    return userObject


users = {}
id_prim=1

for i in range(80000):
    user_object = randomUser()
    user_json = toJSON(user_object)
    users[id_prim] = user_json
    id_prim = id_prim+1

f = open("users.json", 'w')
json.dump(users, f, indent = 4)
