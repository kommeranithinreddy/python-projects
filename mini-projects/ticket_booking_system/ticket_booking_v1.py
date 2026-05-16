#Ticket booking system for a Movie theater

day_type = int(input("Enter day (Weekday = 1, Weekend = 0): "))
customer_type = int(input("Enter customer Type (adult = 1, student = 2, senior = 3): "))
show_time = int(input("Enter show Time (Morning = 1, Afternoon = 2, Evening = 3, Night = 4): "))

wd_price = 120
we_price = 180
match (day_type, customer_type, show_time):
    case (1,1,1):
        print(f'Final ticket price: {wd_price-20}')
    case (1,1,2):
        print(f'Final ticket price: {wd_price}')
    case (1,1,3):
        print(f'Final ticket price: {wd_price+30}')
    case(1,1,4):
        print(f'Final ticket price: {wd_price+50}')
    case(1,2,1):
        print(f'Final ticket price: {(wd_price*0.8)-20}')
    case(1,2,2):
        print(f'Final ticket price: {wd_price*0.8}')
    case(1,2,3):
        print(f'Final ticket price: {(wd_price*0.8)+30}')
    case(1,2,4):
        print(f'Final ticket price: {(wd_price*0.8)+50}')
    case(1,3,1):
        print(f'Final ticket price: {(wd_price*0.7)-20}')
    case(1,3,2):
        print(f'Final ticket price: {wd_price*0.7}')
    case (1,3,3):
        print(f'Final ticket price: {(wd_price*0.7)+30}')
    case(1,3,4):
        print(f'Final ticket price: {(wd_price*0.7)+50}')
    case(0,1,1):
        print(f'Final ticket price: {we_price-20}')
    case(0,1,2):
        print(f'Final ticket price: {we_price}')
    case(0,1,3):
        print(f'Final ticket price: {we_price+30}')
    case(0,1,4):
        print(f'Final ticket price: {we_price+50}')
    case(0,2,1):
        print(f'Final ticket price: {(we_price*0.8)-20}')
    case(0,2,2):
        print(f'Final ticket price: {we_price*0.8}')
    case(0,2,3):
        print(f'Final ticket price: {(we_price*0.8)+30}')
    case(0,2,4):
        print(f'Final ticket price: {(we_price*0.8)+50}')
    case(0,3,1):
        print(f'Final ticket price: {(we_price*0.7)-20}')
    case(0,3,2):
        print(f'Final ticket price: {we_price*0.7}')
    case(0,3,3):
        print(f'Final ticket price: {(we_price*0.7)+30}')
    case(0,3,4):
        print(f'Final ticket price: {(we_price*0.7)+50}')
    case _:
        print("Invalid Input")
