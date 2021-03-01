# Python to Json

data = {
    'name': 'Gopinath Jayakumar',
    'Exp': '10+',
    'value': None,
    'is_nothing': True,
    'hobbies': ('always sleeping....', 'always sleeping....')
}

import json

# dumps: Convert python data to json
print(type(data))
data = json.dumps(data, indent=4)
print(data)

# dump: write the json file
with open('p_to_j.json', 'w') as file:
    json.dump(data, file, indent=4)