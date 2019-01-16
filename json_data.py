import json
data = '{"name":"John Doe", "job":"web designer","city":"New York"}'
person_info = {"name":"John doe", "job":"web designer","city":"New York"}
info = json.loads(data)
print(info["name"])
print(json.dumps(data))
print(person_info["name"])
print(json.dumps(person_info))