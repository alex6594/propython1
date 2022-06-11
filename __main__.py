from application.people import get_employees
from application.salary import calculate_salary
from datetime import datetime


def main():
    print('Good morning, master!  ')
    while True:
        command = input('Enter command: ')
        if command == 's':
            print(datetime.now())
            calculate_salary()
        elif command == 'p':
            print(datetime.now())
            get_employees()
        elif command == 'e':
            break
    print('application off, thanks for working!')


if __name__ == '__main__':
    main()
