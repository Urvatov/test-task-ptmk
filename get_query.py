import sqlite3
import time

def get_query() -> list:

    start_time = time.time()

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute(""" SELECT * FROM employees WHERE sex = "Male" AND name LIKE "F%" """)

    employees = cursor.fetchall()

    connection.close()

    end_time = time.time()

    total_time = end_time - start_time


    print (f"Время выполнения запроса: {total_time} секунд")
    return employees

def create_index():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("""CREATE INDEX IF NOT EXISTS name_index ON employees(name, sex)""")

    connection.commit()
    connection.close()