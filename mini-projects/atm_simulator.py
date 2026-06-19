total_amount = 10000
def deposit(amount):
    global total_amount
    total_amount += amount
    return total_amount

def withdraw(amount):
    global total_amount
    total_amount -= amount
    return total_amount

def check_balance():
    return total_amount

def atm(amount, operation = 'deposit'):
    match operation:
        case 'deposit':
            return deposit(amount)
        case 'withdraw':
            return withdraw(amount)
        case _:
            return 'invalid type'

print(atm(2000, 'deposit'))
print(atm(2000, 'withdraw'))
print(check_balance())