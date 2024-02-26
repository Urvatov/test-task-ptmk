import sqlite3
import time
from database_manager import data

def get_query() -> list:

    start_time = time.time()

    data.cursor.execute(""" SELECT * FROM employees WHERE sex = "Male" AND name LIKE "F%" """)

    employees = data.cursor.fetchall()

    data.connection.close()

    end_time = time.time()

    total_time = end_time - start_time


    print (f"Время выполнения запроса: {total_time} секунд")
    return employees

def create_index():
    data.cursor.execute("""CREATE INDEX IF NOT EXISTS name_index ON employees(name, sex)""")

    data.connection.commit()
    data.connection.close()

    print("Индекс создан")