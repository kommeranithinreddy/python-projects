def login_attempt():
    count = 0
    def counter():
        nonlocal count
        count += 1
        if count<=3:
            print(f'login attempted {count}')
        else:
            print('Login attempt exceeded, account locked')
    return counter

login = login_attempt()
login()
login()
login()
login()