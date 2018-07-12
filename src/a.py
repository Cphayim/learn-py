
from camel_and_snake import Converter
import json

# dict_obj = {
#     'org_id': 123,
#     'org_name': 'ShadowCoder',
#     'member_list': [
#         {'member_id': 1, 'member_name': 'Cphayim'},
#         {'member_id': 2, 'member_name': 'Hoyoe'}
#     ]
# }

# print(json.dumps(Converter.camelify(dict_obj), indent=2))
# # {"orgId": 123, "orgName": "ShadowCoder", "memberList": [{"memberId": 1, "memberName": "Cphayim"}, {"memberId": 2, "memberName": "Hoyoe"}]}

json_str = '{"orgId": 123, "orgName": "ShadowCoder", "memberList": [{"memberId": 1, "memberName": "Cphayim"}, {"memberId": 2, "memberName": "Hoyoe"}]}'
dict_obj = Converter.snakeify(json.loads(json_str))
print(dict_obj)
