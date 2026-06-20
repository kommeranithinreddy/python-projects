def simple_interest(amount, time, interest_rate):
    interest_amount = (amount*time*interest_rate)/100
    print(f'Interest amount is {interest_amount}')
    print(f'Total amount is {amount + interest_amount}')


simple_interest(5000, 15, 1.5)