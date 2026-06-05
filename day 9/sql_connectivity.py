# sqlite3 db usage

import sqlite3 as sql

# conn = sql.connect('company.db')

try:
    with sql.connect('company.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS employees(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    salary REAL
                )
            """)
        emp_id = int(input("Enter Employee Id: "))
        name = input("Employee Name: ")
        salary = float(input("Employee Salary: "))

        # employees = [
        #     (102, 'David', 23451.00),
        #     (103, 'Prasad', 53663.00)
        # ]

        cursor.execute("""
                INSERT INTO employees (id, name, salary) VALUES (?, ?, ?)
        """,
        (emp_id, name, salary)
        )

        # cursor.executemany("""
        #          INSERT INTO employees (id, name, salary) VALUES (?, ?, ?)
        #  """, employees)

        conn.commit()

        cursor.execute("""
            SELECT * FROM employees
        """)
        for row in cursor.fetchall():
            print(row)

        
except sql.IntegrityError as ex:
    conn.rollback()
    print(ex)
except sql.Error as ex:
    print(ex)
except Exception as ex:
    print(ex)
finally:
    conn.close()
    print("Database closed")