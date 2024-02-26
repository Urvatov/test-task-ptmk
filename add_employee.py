from datetime import date
from employee import Employee
from database_manager import data


def add_employee(name : str, date_of_birth : date, sex : str):
    employee = Employee(name, date_of_birth, sex)

    print(f"Имя: {employee.name}")
    print(f"Дата рождения: {employee.date_of_birth}")
    print(f"Пол: {employee.sex}")
    employee.save_to_database(data)

    print(f"Сотрудник {employee} добавлен")