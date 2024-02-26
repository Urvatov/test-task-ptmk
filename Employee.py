from datetime import date
import sqlite3

from database_manager import data


class Employee:
    def __init__(self, name : str, date_of_birth : date, sex : str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.sex = sex
    
    def __str__(self) -> str:
        return self.name
    
    def get_age(self) -> int:
        today = date.today()
        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return age
    
    def save_to_database(self, data):
        data.cursor.execute("""INSERT INTO employees (name, date_of_birth, sex)
                        VALUES (?, ?, ?)""", (self.name, self.date_of_birth, self.sex))
        
        data.connection.commit()
        data.connection.close()

    @staticmethod
    def insert_data(data, employees : list):
        for employee in employees:
            data.cursor.execute("""INSERT INTO employees (name, date_of_birth, sex) VALUES (?, ?, ?)""", (employee.name, employee.date_of_birth, employee.sex))
            
        data.connection.commit()
        #data.connection.close()