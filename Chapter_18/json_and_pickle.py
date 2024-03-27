"""
JSON e pickle

JSON -> JavaScript Object Notation

API -> Communication between services offered by companies and us


"""
# doing with json
"""
import json

# dumps is necessary because json works wit "" and not '', so dumps format this
ret = json.dumps(['product', {'PlayStation 4': ('3TB', 'New', '220V', 2340)}])
print(type(ret))
print(ret)


class Cat:

    def __init__(self, name, race):
        self._name = name
        self._race = race

    @property
    def name(self):
        return self._name

    @property
    def race(self):
        return self._race


felix = Cat('Felix', 'Vira-Lata')
print(felix.__dict__)
ret = json.dumps(felix.__dict__)
print(ret)
"""

# oding with json pickle




import jsonpickle
class Cat:

    def __init__(self, name, race):
        self._name = name
        self._race = race

    @property
    def name(self):
        return self._name

    @property
    def race(self):
        return self._race


felix = Cat('Felix', 'Vira-Lata')
"""
ret = jsonpickle.encode(felix)
print(ret)
"""

with open('Chapter_18/felix_json_pickle.json', 'w') as file:
    ret = jsonpickle.encode(felix)
    file.write(ret)

# trying to recover the json file to a python object

with open('Chapter_18/felix_json_pickle.json', 'r') as file:
    content = file.read()
    ret = jsonpickle.decode(content)
    print(ret)
    print(type(ret))
    print(ret.name)
    print(ret.race)
