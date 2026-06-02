# to read from a txt file
# method 1
# with open('sample.txt', 'r', encoding='utf-8') as f:
#     content = f.read()
#     print(content)

# print()
# print()
# # method 2
# with open('sample.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     # print(lines)
#     for line in lines:
#         print(line)

# method 3 - to work with large files and for filtering the file
# with open('sample.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line)

# lines = ['This is python content\n', 'writing into file now\n', 'complete this\n']

# with open('sample.txt', 'w', encoding='utf-8') as f:
#     for line in lines:
#         f.write(line)

# f = open('sample.txt', 'r', encoding='utf-8')
# content = f.read()
# print(content)
# f.close()

# working with multiple files
# with open('sample.txt', 'r', encoding='utf-8') as src, open('output.txt', 'w', encoding='utf-8') as dest:
#     for line in src:
#         dest.write(line.title())


# with exceptions
# try:
#     with open('sample.txt', 'r', encoding='utf-8') as src, open('output.txt', 'w', encoding='utf-8') as dest:
#         for line in src:
#             dest.write(line.title())
# except FileNotFoundError as ex:
#     print("File not found. Using defaults: ", ex)
# except PermissionError as ex:
#     print("Permission denied to write. ", ex)


# ----------------------------------------------------------------------
# working with csv files
import csv

# with open('employees.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     header = next(reader)  #skip the header row

#     for row in reader:
#         print(row)

# using a DictReader
# with open('employees.csv', 'r', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     employees = list(reader)

#     for emp in employees:
#         print(f"Id: {emp.get('EMPLOYEE_ID')},\
#               First Name: {emp.get('FIRST_NAME')},\
#             Last Name: {emp.get('LAST_NAME')}, \
#                 Email: {emp.get('EMAIL')}")
        
# writing into csv 
#fields - EMPLOYEE_ID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUMBER,HIRE_DATE,JOB_ID,SALARY,COMMISSION_PCT,MANAGER_ID,DEPARTMENT_ID
# sample rec - 198,Donald,OConnell,DOCONNEL,650.507.9833,21-JUN-07,SH_CLERK,2600, - ,124,50

new_employees = [
    {'EMPLOYEE_ID': 342,'FIRST_NAME': 'Alex', 'LAST_NAME': 'Smith', 'EMAIL': 'ASMITH', 'PHONE_NUMBER': '659.001.993','HIRE_DATE':'23-FEB-10','JOB_ID':'SH_CLERK','SALARY':2800, 'COMMISSION_PCT': '-','MANAGER_ID':124,'DEPARTMENT_ID': 10 },
    {'EMPLOYEE_ID': 362,'FIRST_NAME': 'Jane', 'LAST_NAME': 'Doe', 'EMAIL': 'JDOE', 'PHONE_NUMBER': '650.001.994','HIRE_DATE':'23-FEB-10','JOB_ID':'SH_CLERK','SALARY':2800, 'COMMISSION_PCT': '-','MANAGER_ID':124,'DEPARTMENT_ID': 10 }
]

with open('employees.csv', 'a', encoding='utf-8', newline='') as f:
    fieldnames = ['EMPLOYEE_ID','FIRST_NAME','LAST_NAME','EMAIL','PHONE_NUMBER','HIRE_DATE','JOB_ID','SALARY','COMMISSION_PCT','MANAGER_ID','DEPARTMENT_ID']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    for e in new_employees:
        writer.writerow(e)

    print("Written successfully")
