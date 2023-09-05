import json

data = [{"name": "老王", "age": "16"}, {"name": "老李", "age": "20"}]
json_str = json.dumps(data)
print(json_str)
