# json file io in python

import json
from datetime import datetime

# json_string = '''
#     {
#         "name": "Alice",
#         "total_score": 97.3,
#         "subjects": ["Science", "Maths"],
#         "email": null,
#         "address": {"street#": 23, "house#": 34, "area": "area12"}
#     }
# '''

# student = json.loads(json_string)

# print(student)
# print('Class: ', type(student))
# print('Name: ', student['name'])
# print("Address Type: ", type(student['address']))


# read from json file
# try:
#     json_data = "{'name': 'Prithvi'}"  # invalid json. use double quotes for key and value

#     data = json.loads(json_data)
#     print(data)
#     # with open('employeeData.json', 'r') as f:
#     #     employees = json.load(f)
#     #     print(employees)
# except json.JSONDecodeError as e:
#     print(f"Invalid JSON: {e}")

# serialize a python object into a json object
# person = {
#     'name': 'Prithvi',
#     'age': 27,
#     'hobbies': ['hiking', 'travelling'],
#     'education': 'MBA'
# }

# with open('personal_details.json', 'a', encoding='utf-8') as f:
#     json.dump(person, f, indent=2)

# print('written to file')

# compact = json.dumps(person)
# print(compact)

# print()

# pretty_print = json.dumps(person, indent=2)
# print(pretty_print)

# json.dumps({"ts": datetime.now()})  # cannot be serialized by default
# data = {'ts': datetime.now().isoformat()}
# print(json.dumps(data))

# class DateEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime):
#             return obj.isoformat()
#         return super().default(obj)
    

# data = json.dumps({'ts': datetime.now()}, cls=DateEncoder)
# print(data)

api_response = '''
    {
        "status": "success",
        "data": {
            "user": {
                "id": 42,
                "name": "Prithvi",
                "contact": {
                    "email": "prithvi@example.com",
                    "phone": "92882810"
                },
                "orders":[
                    {"ord_id": "ORD-001", "total": "60.00", "items": ["book", "pen"]},
                    {"ord_id": "ORD-004", "total": "90.00", "items": ["headphones"]}
                ]
            }
        },
        "errors": []
    }
'''

data = json.loads(api_response)

# working with the nested parts of json
user = data["data"]["user"]
# orders = data["data"]["user"]["orders"]
# print(orders)

orders = user.get('orders')
print(orders)

