import pandas as pd
# import numpy as np

# print("Pandas Version: ", pd.__version__)
# print("Numpy Version: ", np.__version__)

series1 = pd.Series([10, 20, 30, 40])
# print("Series 1: From List:\n", series1)

series2 = pd.Series([86, 78, 90, 65],
                    index=['Prithvi', 'Prasad', 'Pavan', 'Pooja'],
                    name='Marks')
# print("Custom Index: Series 2:\n", series2)

# person ={
#     'name': 'Alice',
#     'email': 'alice@example.com',
#     'age': 45,
#     'contact': '83892992'
# }

# s3 = pd.Series(person)
# print("From Dict:\n", s3 )

# print(series2.loc['Prithvi'])
# print(series2[series2 > 75])
# print(series1.loc[:2])
# print(series1.iloc[:2])

# attributes and operations for series
# print(series1.dtype)
# print(series1.size)

print(series2.describe())