import sqlite3

DB_NAME = 'company.db'

def create_table():
    sql_create = "CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY,\
                    name TEXT NOT NULL,\
                    department TEXT NOT NULL,\
                    salary REAL)"
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute(sql_create)

            conn.commit()
    except sqlite3.Error as e:
        print("Database Error: ", e)
    finally:
        conn.close()

create_table()

# CRUD Operations:

def add_employee(emp):
    """
        Adding an employee
    """
    insert_query = "INSERT INTO employees (id, name, department, salary) VALUES (?, ?, ?, ?)"
    try:
         with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute(insert_query,
                           (
                               emp['id'],
                               emp['name'],
                               emp['department'],
                               emp['salary']
                           ))

            conn.commit()
            return{
                'success': True,
                "message": "Employee Added Successfully"
            }
    except sqlite3.IntegrityError as e:
        return {
            'success': False,
            "message": "Employee Id already exists"
        }
    except sqlite3.Error as e:
        print("Database Error: ", e)
    except Exception as e:
        return {
            'success': False,
            "message": str(e)
        }
    finally:
        conn.close()

def get_all_employees():
    """
        Retrieving all employees
    """
    get_query = "SELECT * FROM employees"
    try:
        with sqlite3.connect(DB_NAME) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            cursor.execute(get_query)

            rows = cursor.fetchall()

            return [
                dict(row)
                for row in rows
            ]
            
    except sqlite3.Error as e:
        print(" Error: ", e)
        return []
    finally:
        conn.close()
       

def get_employee_by_id(emp_id):
    get_query = "SELECT * FROM employees WHERE id = ?"
    try:
        with sqlite3.connect(DB_NAME) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            cursor.execute(get_query, (emp_id,))

            row = cursor.fetchone()
            
            if row:
                return dict(row)
            else:
                return {
                    'message': "Employee Not Found"
                }
            
    except sqlite3.Error as e:
        return {'error': str(e)}
    finally:
        conn.close()