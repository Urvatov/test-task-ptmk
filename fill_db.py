from employee import Employee
from progress.bar import IncrementalBar

import random
from datetime import date

iterations = 1000000

employees = []
letters = "abcdefghijklmnopqrstuvwxyz"

progress_bar = IncrementalBar("Вставляем значения: ", max=iterations)

def generate_name() -> str:
    letter = random.choice(letters)
    name = letter.upper() + "_name"

    return name

def generate_date() -> date:
    year = random.randint(1960, 2024)
    month = random.randint(1, 12)
    day = random.randint(1, 28)

    return date(year, month, day)

def generate_sex() -> str:
    sex = random.choice(["Male", "Female"])

    return sex

def f_strings():
    for _ in range(100):
        employee = Employee("F_NAME", generate_date(), "MALE")
        employees.append(employee)

        Employee.insert_data(employees)

        employees.clear()

def fill_db():
    f_strings()

    for _ in range(iterations):
        employee = Employee(generate_name(), generate_date(), generate_sex())
        employees.append(employee)
        #progress_bar.next()

    Employee.insert_data(employees)
    print("Значения вставлены")

fill_db()