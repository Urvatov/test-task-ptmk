import sqlite3

def display_employees():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT * FROM employees""")

    employees = cursor.fetchall()

    connection.close()


    for employee in employees:
        print(f"{employee[0]} | {employee[1]} | {employee[2]} | {employee[3]}")
    
    

display_employees()