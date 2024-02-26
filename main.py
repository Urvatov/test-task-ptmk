import sys

from database_manager import DatabaseManager

from create_table import create_table
from add_employee import add_employee
from display_employees import display_employees
from fill_db import fill_db
from get_query import get_query, create_index

DATABASE = "database.db"
def main(arg : int):
    print(f"Аргумент: {arg}")

    match arg:
        case 1: create_table()
        case 2: add_employee(sys.argv[2], sys.argv[3], sys.argv[4])
        case 3: display_employees()
        case 4: fill_db()
        case 5: get_query()
        case 6: create_index()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Не выбран аргумент!")
    else:
        arg = int(sys.argv[1])
        main(arg)