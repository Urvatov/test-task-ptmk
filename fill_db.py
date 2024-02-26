from employee import Employee

import random
import time
from datetime import date
from database_manager import data

iterations = 1000000

employees = []
letters = "abcdefghijklmnopqrstuvwxyz"


def generate_name() -> str:
    letter = random.choice(letters)
    name = letter.upper() + "_name"

    return name

def generate_date() -> date:
    year = random.randint(1960, 2024)
    #month = random.randint(1, 12)
    month = 1
    #day = random.randint(1, 28)
    day = 1

    return date(year, month, day)

def generate_sex() -> str:
    sex = random.choice(["Male", "Female"])

    return sex

def f_strings():
    for _ in range(100):
        employee = Employee("F_NAME", generate_date(), "Male")
        employees.append(employee)

        Employee.insert_data(data, employees)

        employees.clear()

def fill_db():
    start_time = time.time()

    f_strings()
    print("Начинается вставка сообщений...")

    for _ in range(iterations):
        employee = Employee(generate_name(), generate_date(), generate_sex())
        employees.append(employee)
    
    Employee.insert_data(data, employees)

    end_time = time.time()

    total_time = end_time - start_time

    print(f"Значения вставлены. Время выполнения: {total_time} секунд")
