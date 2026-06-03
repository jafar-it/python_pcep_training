import pandas as pd

# create a dataframe
employees = pd.DataFrame(
    {'name': ['Prithvi', 'Pooja', 'Manish', 'Sneha'],
     'department': ['HR', 'IT', 'IT', 'Sales'],
     'salary': [65000.00, 78090.00, 76000.00, 58000.00],
     'remote': [False, True, True, False]
    }
)

# print the entire dataframe
# print(employees)

# print one row only
# print(employees.loc[0])

# print first 2 records only
# print(employees.head(2))

# count unique values
# print(employees['department'].value_counts())

# retrieve column names
# print(employees.columns)

# print(employees.describe())

# df = employees.copy()

# print(employees[['name', 'salary']])

# print(employees.loc[0, 'name'])

# renaming index (column names)
employees = employees.rename(columns={'remote': 'working_remotely'})
# print(employees)

# sorting
employees.sort_values('salary', ascending=True, inplace=True)
print(employees)