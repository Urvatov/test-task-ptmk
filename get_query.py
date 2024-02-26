import time
from database_manager import data

def get_query() -> tuple:

    start_time = time.time()

    data.cursor.execute(""" SELECT * FROM employees WHERE sex = "Male" AND name LIKE "F%" """)
    #data.cursor.execute(""" SELECT * FROM employees WHERE name LIKE "F%" AND sex = "Male" """)
    employees = data.cursor.fetchall()

    data.connection.close()

    end_time = time.time()

    total_time = end_time - start_time


    print (f"Время выполнения запроса: {total_time} секунд")
    return employees

def create_index():
    print("Создание индекса...")
    data.cursor.execute("""CREATE INDEX IF NOT EXISTS name_index ON employees(sex, name)""")
    
    data.connection.commit()
    data.connection.close()

    print("Индекс создан")