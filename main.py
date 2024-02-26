import sys

from create_table import create_table

def main(arg : int):
    print(f"Аргумент: {arg}")

    match arg:
        case 1: create_table()

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("Не выбран аргумент!")
    else:
        arg = int(sys.argv[1])
        main(arg)