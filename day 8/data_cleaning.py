import pandas as pd
import numpy as np

df = pd.DataFrame(
    {'name': ['Alice', 'Bob',None, 'Dave', 'Ethan'],
    'age': [29, np.nan,34, np.nan, 38],
    'salary': [85000, 68000, 45000, np.nan, np.nan]
    }
)

# print(df)

# print("Null values: ", df.isnull())
# print("Null count: ", df.isnull().sum())

# cleaned_df = df.dropna()
# print("Cleaned data: ", cleaned_df)

# df['name'] = df['name'].fillna('Unknown')
# df['age'] = df['age'].fillna(0)
# df['salary'] = df['salary'].fillna(0)
# print(df)

# filtering and selecting data
employees = pd.DataFrame(
    {'name': ['Prithvi', 'Pooja', 'Manish', 'Sneha'],
     'department': ['HR', 'IT', 'IT', 'Sales'],
     'salary': [65000.00, 78090.00, 76000.00, 58000.00],
     'remote': [True, False, True, False]
    }
)

# boolean indexing - use &, |, ~
# print(employees[(employees['salary']>75000) & (employees['remote'] == True)])

# query()
# print(employees.query("salary > 75000 and remote == True"))

# min_salary = 55000
# print(employees.query("remote==True and salary > @min_salary and department=='IT'"))

employees['salary_band'] = np.where(employees['salary']>=75000, 'High', 'Standard')
print(employees)

# try apply(), groupby()
