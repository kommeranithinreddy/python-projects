def cust_message(message):
    def inner(name):
        print(f'{message} {name}')
    return inner

hey = cust_message('Hey')
hey('Nithin')
morning = cust_message('Good Morning')
morning('Nithin')
morning('Nandini')
morning('Shubham')