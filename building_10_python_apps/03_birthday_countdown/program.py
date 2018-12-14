import datetime


def main():
    header()
    bday = user_bday()
    today = datetime.date.today()
    number_of_days = countdown(bday, today)
    print_birthday_information(number_of_days)


def header():
    print('-------------------------------')
    print('           BIRTHDAY APP')
    print('-------------------------------')


def user_bday():
    year = int(input("What year were you born [YYYY]? "))
    month = int(input("What month were you born [MM]? "))
    day = int(input("What day were you born [DD]? "))

    birthday = datetime.date(year, month, day)
    return birthday


def countdown(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)

    dt = this_year - target_date
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print("You had your birthday {} days ago this year.".format(-days))
    elif days > 0:
        print("Your birthday is in {} days!".format(days))
    else:
        print("Happy birthday!!!")

main()

