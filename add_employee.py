from datetime import date
from employee import Employee

def add_employee(name : str, date_of_birth : date, sex : str):
    employee = Employee(name, date_of_birth, sex)
    employee.save_to_database()

    print(f"Сотрудник {employee} добавлен")