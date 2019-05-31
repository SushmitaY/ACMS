import json
import random
from json import JSONEncoder

class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

def toJSON(obj):
    a = MyEncoder().encode(obj)
    return json.loads(a)

