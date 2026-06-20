def retry(parameter):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < parameter:
                try:
                    fun(*args, **kwargs)
                    break
                except ValueError: #added extra by myself
                    attempts += 1
                    if attempts < parameter:
                        print(f'Attempt {attempts} failed')
                    else:
                        print(f'{attempts} Attempts exceeded')
        return wrapper
    return decorator


@retry(3)
def login():
    uname = input("Enter uname: ")
    password = input("Enter password: ")
    if uname == 'nithin' and password == 'reddy123':
        print('Success')
    else:
        raise ValueError()

login()
login()
