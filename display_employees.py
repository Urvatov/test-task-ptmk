import sqlite3
from employee import Employee
from datetime import date

def display_employees():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT * FROM employees
                    WHERE id IN (
                    SELECT MIN(id)
                    FROM employees
                    GROUP BY name, date_of_birth) ORDER BY name""")

    employees = cursor.fetchall()

    connection.close()

    for employee in employees:
        employee_instance = Employee(employee[1], date.fromisoformat(employee[2]), employee[3])
        age = employee_instance.get_age()
        print(f"{employee[0]} | {employee[1]} | {employee[2]} | {employee[3]} | {age}")
    


#display_employees()