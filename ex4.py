
import json
from collections import namedtuple


data = '{"name" : "Arjun", "id" : 101, "location" : "Chennai"}'


x = json.loads(data, object_hook =
			lambda d : namedtuple('X', d.keys())
			(*d.values()))


print(x.name, x.id, x.location)