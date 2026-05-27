from collections import namedtuple, defaultdict, Counter

#list methods
# sort, sorted, reverse

# fruits = ["apple", "banana", "grapes"]

# fruits.append("orange")
# fruits.extend(['dates', 'figs'])

# # fruits.remove('apple')
# # print(fruits)

# # fruits.pop(1)
# # print(fruits)

# # print(fruits.count('banana'))

# #slicing lists

# print(fruits[1:4])
# print(fruits[-2:])


# raw_data = [("Alice", "HR", 56000), ("Bob", "IT", 65000), ("Charles", "IT",67500), ("Dan", "Development", 78000), ("Ethan", "IT", 55000), ("Greg", "IT", 65700)]

# it_team = []

# for e in raw_data:
#     if e[1] == 'IT':
#         it_team.append(e)

# print(it_team)

# it_team = sorted([e for e in raw_data if e[1] == 'IT'],
#                  key=lambda x:x[2], reverse=False)

# print(it_team)

# for ind, emp in enumerate(raw_data):
#     for i, e in enumerate(emp[0]):
#         print(i, e)

#tuples - immutable

# employee = ("Alice", "HR", 56000)

# for i, e in enumerate(employee):
#     print(i, e)

# dungeon_map = {
#     (0,0): {"type": "entrance", "lit": True},
#     (0,1): {"type": "corridor", "lit": False},
#     (1,1): {"type": "room", "lit": True}
# }

# player_pos = (0,0)
# cell = dungeon_map.get(player_pos, {"type": "void"})
# print(f"You are in: {cell['type']} ")

# Employee = namedtuple('Employee', ['name', 'dept', 'salary'])
# emp = Employee("Alice", "HR", 45000)

# employees = []
# employees.append(emp)

# print(emp)
# print(employees[0].dept)

#Dictionary - key - value pairs
# customer = {
#     "id": 1001,
#     "name": "John Doe",
#     "email": "john.doe@example.com",
#     "active": True,
#     "balance": 25000.0,
#     "accounts": ["ABC1234", "SB2782"]
# }
# print("Before: ", customer)

# print(customer['email'])
# print(customer.get('name'))
# # print(customer['aadhar'])
# print(customer.get('aadhar', '0000-0000-0000'))

# customer['aadhar'] = '9282-8888-0021'
# print(customer)

# student = dict(name='Seema', marks=89, grade='A')
# print(student)

# initial_sales = dict.fromkeys(["q1", 'q2', 'q3', 'q4'], 0)
# print(initial_sales)

# areas = ['Nagarbhavi', 'Jayanagar', 'Basaveshwarnagar']
# zipcodes = ['560091', '560011', '560079']

# area_codes = dict(zip(areas, zipcodes))
# print(area_codes)

# # for only keys
# for key in area_codes:
#     print(key)

# # for only values
# for val in area_codes.values():
#     print(val)

# # for key and value
# for key,val in area_codes.items():
#     print(f"Key: {key}, Value: {val}")

# config = {"host": "localhost", 'port': 8080, 'db': 'prod', 'pool': 10}

# # for key, val in config.items():
# #     if isinstance(val, int):
# #         print(key, val)

# numeric_vals = {k: v for k,v in config.items() if isinstance(v, int)}
# print(numeric_vals)


# threat_events = [
#     {'ip': '172.1.1.0', 'type': 'brute_force', 'severity': 'high'},
#     {'ip': '10.168.0.0', 'type': 'port_scan', 'severity': 'medium'},
#     {'ip': '172.1.1.0', 'type': 'sql_inject', 'severity': 'critical'},
#     {'ip': '192.16.0.0', 'type': 'brute_force', 'severity': 'high'},
#     {'ip': '10.0.0.3', 'type': 'brute_force', 'severity': 'high'},
#     {'ip': '172.1.1.0', 'type': 'port_scan', 'severity': 'low'}
# ]

# severity_rank = {'low': 1, 'medium': 2, 'high': 3, 'critical': 4}

# intel = defaultdict(lambda: {'events': [], "max_sev": 'low'})  #{ip: [events], max_sev: 'low'}

# for e in threat_events:
#     ip = e['ip']
#     intel[ip]["events"].append(e['type'])
#     if severity_rank[e['severity']] > severity_rank[intel[ip]["max_sev"]]:
#         intel[ip]["max_sev"] = e["severity"]

# print("Intelligence report")
# for ip, data in sorted(intel.items()):
#     freq = Counter(data['events'])
#     print(f"IP: {ip:18} | Max: {data['max_sev']:8} | Events: {dict(freq)}")


# Sets - only unique values
skills_a = {'Python', 'C', 'Java'}
skills_b = {'Java', 'C#', 'Python', 'R'}

common_skills = skills_a & skills_b   # intersection
either_skills = skills_a | skills_b   # union
only_in_a = skills_a - skills_b  # difference
unique_skills = skills_a ^ skills_b  # symmetric diff

print(f"Common Skills: {common_skills}")
print(f"Either Skills: {either_skills}")
print(f"Unique Skills: {unique_skills}")

emp_ids = [101, 102, 102, 104, 109, 101, 301]
unique_ids = list(set(emp_ids))

duplicate_ids = [x for x in emp_ids if emp_ids.count(x) > 1]

print(f"Unique Ids: {unique_ids}, Duplicates: {duplicate_ids}")

# duplicate_ids = []
# for x in emp_ids:
#     if emp_ids.count(x) > 1:
#         duplicate_ids.append(x)

fruits = ["apple", "banana", "grapes", 'apple', 'orange', 'CHERRY', 'banana']

unique_fruits = {fruit.title() for fruit in fruits} # set comprehension
print(f"Unique Fruits in Title case: {unique_fruits}")


# set, functions, modules, classes => tomorrow