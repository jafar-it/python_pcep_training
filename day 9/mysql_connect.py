# install the connector
# pip install mysql-connector-python
# NOTE: Create database in the mysql server before running the below code

# CRUD with MySQL DB
import mysql.connector

# ==========================================
# DATABASE CONFIGURATION
# ==========================================

HOST = "localhost"
USER = "root"
PASSWORD = "password"     # Change to your password
DATABASE = "company_db"

# ==========================================
# DATABASE CONNECTION
# ==========================================
def get_connection():

    try:
        conn = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Connection Error: {e}")
        return None

# ==========================================
# CREATE TABLE
# ==========================================
def create_table():
    conn = None

    try:
        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees(
            id INT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            department VARCHAR(100) NOT NULL,
            salary DECIMAL(10,2) NOT NULL
        )
        """)

        conn.commit()

        print("Employee table ready.")
    except mysql.connector.Error as e:
        print("Database Error:", e)
    finally:
        if conn and conn.is_connected():
            conn.close()

# ==========================================
# CREATE EMPLOYEE
# ==========================================
def add_employee():

    conn = None

    try:

        emp_id = int(input("Employee ID: "))
        name = input("Name: ").strip()
        department = input("Department: ").strip()
        salary = float(input("Salary: "))

        conn = get_connection()

        if conn is None:
            return

        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO employees
        (id, name, department, salary)
        VALUES (%s, %s, %s, %s)
        """,
        (
            emp_id,
            name,
            department,
            salary
        ))

        conn.commit()

        print("Employee added successfully.")

    except ValueError:

        print("Invalid numeric input.")

    except mysql.connector.IntegrityError:

        print("Employee ID already exists.")

    except mysql.connector.Error as e:

        print("Database Error:", e)

    finally:

        if conn and conn.is_connected():
            conn.close()


# ==========================================
# VIEW ALL EMPLOYEES
# ==========================================

def view_employees():

    conn = None

    try:

        conn = get_connection()

        if conn is None:
            return

        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM employees
        ORDER BY id
        """)

        rows = cursor.fetchall()

        if not rows:

            print("No employees found.")
            return

        print("\n")
        print("-" * 70)
        print(
            f"{'ID':<10}"
            f"{'NAME':<20}"
            f"{'DEPARTMENT':<20}"
            f"{'SALARY':<15}"
        )
        print("-" * 70)

        for row in rows:

            print(
                f"{row[0]:<10}"
                f"{row[1]:<20}"
                f"{row[2]:<20}"
                f"{row[3]:<15}"
            )

    except mysql.connector.Error as e:

        print("Database Error:", e)

    finally:

        if conn and conn.is_connected():
            conn.close()


# ==========================================
# SEARCH EMPLOYEE
# ==========================================

def search_employee():

    conn = None

    try:

        emp_id = int(input("Enter Employee ID: "))

        conn = get_connection()

        if conn is None:
            return

        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM employees
        WHERE id = %s
        """,
        (emp_id,))

        row = cursor.fetchone()

        if row:

            print("\nEmployee Found")
            print("-" * 30)

            print(f"ID         : {row[0]}")
            print(f"Name       : {row[1]}")
            print(f"Department : {row[2]}")
            print(f"Salary     : {row[3]}")

        else:

            print("Employee not found.")

    except ValueError:

        print("Employee ID must be numeric.")

    except mysql.connector.Error as e:

        print("Database Error:", e)

    finally:

        if conn and conn.is_connected():
            conn.close()


# ==========================================
# UPDATE EMPLOYEE
# ==========================================

def update_employee():

    conn = None

    try:

        emp_id = int(input("Employee ID: "))

        new_name = input("New Name: ")
        new_department = input("New Department: ")
        new_salary = float(input("New Salary: "))

        conn = get_connection()

        if conn is None:
            return

        cursor = conn.cursor()

        cursor.execute("""
        UPDATE employees
        SET
            name=%s,
            department=%s,
            salary=%s
        WHERE id=%s
        """,
        (
            new_name,
            new_department,
            new_salary,
            emp_id
        ))

        conn.commit()

        if cursor.rowcount == 0:

            print("Employee not found.")

        else:

            print("Employee updated successfully.")

    except ValueError:

        print("Invalid input.")

    except mysql.connector.Error as e:

        print("Database Error:", e)

    finally:

        if conn and conn.is_connected():
            conn.close()


# ==========================================
# DELETE EMPLOYEE
# ==========================================

def delete_employee():

    conn = None

    try:

        emp_id = int(input("Employee ID: "))

        conn = get_connection()

        if conn is None:
            return

        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM employees
        WHERE id=%s
        """,
        (emp_id,))

        conn.commit()

        if cursor.rowcount == 0:

            print("Employee not found.")

        else:

            print("Employee deleted successfully.")

    except ValueError:

        print("Employee ID must be numeric.")

    except mysql.connector.Error as e:

        print("Database Error:", e)

    finally:

        if conn and conn.is_connected():
            conn.close()


# ==========================================
# EMPLOYEE STATISTICS
# ==========================================

def employee_statistics():

    conn = None

    try:

        conn = get_connection()

        if conn is None:
            return

        cursor = conn.cursor()

        cursor.execute("""
        SELECT
            COUNT(*),
            AVG(salary),
            MAX(salary),
            MIN(salary)
        FROM employees
        """)

        result = cursor.fetchone()

        print("\nEmployee Statistics")
        print("-" * 30)

        print("Total Employees :", result[0])
        print("Average Salary  :", round(float(result[1]), 2) if result[1] else 0)
        print("Highest Salary  :", result[2] if result[2] else 0)
        print("Lowest Salary   :", result[3] if result[3] else 0)

    except mysql.connector.Error as e:

        print("Database Error:", e)

    finally:

        if conn and conn.is_connected():
            conn.close()


# ==========================================
# MAIN MENU
# ==========================================

def main():

    create_table()

    while True:

        print("\n")
        print("=" * 50)
        print("EMPLOYEE MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Employee Statistics")
        print("7. Exit")

        choice = input("\nEnter Choice: ")

        match choice:

            case "1":
                add_employee()

            case "2":
                view_employees()

            case "3":
                search_employee()

            case "4":
                update_employee()

            case "5":
                delete_employee()

            case "6":
                employee_statistics()

            case "7":
                print("Application Closed.")
                break

            case _:
                print("Invalid Choice")


# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":
    main()