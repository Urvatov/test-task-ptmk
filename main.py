import sys
import sqlite3

from datetime import date

from create_table import create_table
from add_employee import add_employee
from display_employees import display_employees
from fill_db import fill_db


def main(arg : int):
    print(f"Аргумент: {arg}")

      
    match arg:
        case 1: create_table()
        case 2: add_employee(sys.argv[2], sys.argv[3], sys.argv[4])
        case 3: display_employees()
        case 4: fill_db()

    connect_db() 

def connect_db():
    global connection
    connection = sqlite3.connect("database.db")

    global cursor
    cursor = connection.cursor()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Не выбран аргумент!")
    else:
        arg = int(sys.argv[1])
        main(arg)