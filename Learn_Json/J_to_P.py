import json

# Loads: Covert json file to Python format
pythonObj = json.loads('{"name":"GN", "active": false, "value":null}')
print(pythonObj)

# Load:
with open('p_to_j.json', 'r') as file:
    data = json.load(file)
    fo = json.loads(data)
print(fo)