from datetime import date
from application.salary import calculate_salary
from application.db.people import get_employees


date = date.today()

if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(date)
