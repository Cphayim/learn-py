import json
json_str = '[{"name": "qiyue", "age": false}, {"name": "qiyue", "age": false}]'

# 反序列化
student = json.loads(json_str)
print(type(student))
print(student)

# 序列化
str = json.dumps(student)
print(type(str))
print(str)
