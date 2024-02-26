import sqlite3

from database_manager import data

def create_table():
    data.cursor.execute("""CREATE TABLE IF NOT EXISTS employees 
                   (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    date_of_birth DATE NOT NULL,
                    sex TEXT NOT NULL
                   )""")
    
    print("Таблица создана")
    