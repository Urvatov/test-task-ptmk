from datetime import date
import sqlite3


class Employee:
    def __init__(self, name : str, date_of_birth : date, sex : str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.sex = sex
    
    def __str__(self) -> str:
        return self.name
    
    def get_age(self) -> int:
        return date.today().year - self.date_of_birth.year
    
    def save_to_database(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute("""INSERT INTO employees (name, date_of_birth, sex)
                        VALUES (?, ?, ?)""", (self.name, self.date_of_birth, self.sex))
        
        connection.commit()
        connection.close()

    @staticmethod
    def insert_data(employees : list):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        for employee in employees:
            cursor.execute("""INSERT INTO employees (name, date_of_birth, sex) VALUES (?, ?, ?)""", (employee.name, employee.date_of_birth, employee.sex))
            
        
        connection.commit()
        connection.close()