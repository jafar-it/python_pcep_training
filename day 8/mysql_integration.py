import sqlite3 as sql3

try:
    conn = sql3.connect('employees.db')
    print("Connection successful")
except Exception as ex:
    print(ex)
finally:
    conn.close()