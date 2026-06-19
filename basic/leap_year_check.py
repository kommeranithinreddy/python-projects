def leap_year_check(year):
    if year%400 == 0:
        print_result(year, True)
    elif year%4 == 0 and year%100 != 0:
        print_result(year, True)
    else:
        print_result(year, False)

def print_result(year, value):
    if value:
        print(f'{year} is a leap year')
    else:
        print(f'{year} is not a leap year')

leap_year_check(2028)