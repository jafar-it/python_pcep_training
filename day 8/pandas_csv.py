import pandas as pd

# employees = pd.read_csv('employees.csv')
# # print(employees)

# employees.sort_values('SALARY', ascending=False, inplace=True)

# first_ten = employees.head(10)

# first_ten.to_csv('top_10.csv', index=False)
# print(type(employees['EMPLOYEE_ID'][0]))

# processing large csv files in chunks
chunk_size = 20
result = [] 
for chunk in pd.read_csv('employees.csv', chunksize=chunk_size):
    filtered_data = chunk[chunk['EMPLOYEE_ID'] < 200]
    result.append(filtered_data)

final_output = pd.concat(result, ignore_index=True)
print(final_output)


