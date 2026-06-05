# extract from csv and load into sqlite
import pandas as pd
import sqlite3 as sql

sql_select = "SELECT * FROM employees"
sql_insert = "INSERT INTO employees (id,name,department, salary) VALUES (?,?,?,?)"
sql_delete = "DELETE FROM employees WHERE id = ?"

# # read csv
# df = pd.read_csv("employees.csv")

# create the connection
try:
    with sql.connect('company.db') as conn:

        # # load data
        # df.to_sql(
        #     "employees",
        #     conn,
        #     if_exists='replace',
        #     index=False
        # )
        # print("Data loaded successfully")

        # retrieve the data
        cursor = conn.cursor()
        cursor.execute(sql_select)

        for row in cursor.fetchall():
            print(row)

        # emp_id = int(input("Employee to Remove: "))
        # cursor.execute(sql_delete, (emp_id,))

        conn.commit()

        if cursor.rowcount == 0:
            print("Employee not found")
        else:
            print("employee removed")

except sql.Error as ex:
    print(ex)
except Exception as ex:
    print(ex)
finally:
    conn.close()
    print("Database closed")