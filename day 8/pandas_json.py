import pandas as pd

# employees = pd.read_json('employeeData.json')
# print(employees.loc[0])

employees = pd.read_excel("employees.xlsx")
# print(employees)

top_10 = employees.head(10)
# print(top_10)

top_10.to_excel('top_ten.xlsx', sheet_name='Employee Data', index=False)
