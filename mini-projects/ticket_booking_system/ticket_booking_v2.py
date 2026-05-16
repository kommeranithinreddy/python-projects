#Ticket booking system for a Movie theater


day_type = input("Enter day (weekday/weekend): ")
customer_type = input("Enter customer type for discount (adult/student/senior): ")
show_time = input("Enter Show Time (morning/afternoon/evening/night): ")

rate = None
discount = None
time = None

match day_type:
    case 'weekday':
        rate = 120
    case 'weekend':
        rate = 180
    case _:
        print("invalid Day Type - please try again")
match customer_type:
    case 'adult':
        discount = 1
    case 'student':
        discount= 0.8
    case 'senior':
        discount= 0.7
    case _:
        print("invalid Customer Type - please try again")
match show_time:
    case 'morning':
        time= -20
    case 'afternoon':
        time= 0
    case 'evening':
        time= 30
    case 'night':
        time= 50
    case _:
        print("invalid Show Time - please try again")

if rate is not None and discount is not None and time is not None:
    price = rate * discount + time
    print(f'The price of the ticket is {int(price)}')
else:
    print ("ticket cannot be calculated")
