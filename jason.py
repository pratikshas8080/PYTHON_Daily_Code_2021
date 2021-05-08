import json

"""
person = '{"Name": "sud", "Spekon": "English"}'

dict = json.loads(person)

print(dict)"""


# open existing json File
with open("new.json") as f:
    data = json.load(f)

print(json.dumps(data, indent=4, sort_keys=True))  # show the data into readable format


"""
# creating dictionary and save that data into file
person = {"Name": "sud", "Spekon": "English", "Age": 22}

with open("person.txt", "w") as json_file:
    json.dump(person, json_file)"""

"""only this types converted into json that are following 
dict
list
tuple
str
int
float
Boolean
None(Empty)"""
