def username_check(username):
    username_result = True
    if len(username) == 0:
        username_result = False
    else:
        for char in username:
            if not ('A'<= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9'):
                username_result = False
                break

    return username_result

def domain_check(domain_name):
    if domain_name == 'gmail.com':
        return True
    else:
        return False


def check_at_symbol(email):
    if email.count('@') == 1:
        return True
    else:
        return False

def result_print(value):
    if value:
        print("Email address is valid")
    else:
        print("Email address is not valid")

def email_validator():
    main_email = input('Enter any email address to check: ')
    flag = check_at_symbol(main_email)
    if flag:

        split_email = main_email.rsplit('@', 1)
        username = split_email[0]
        domain_name = split_email[1]
        username_result = username_check(username)
        domain_result = domain_check(domain_name)

        if username_result and domain_result:
            result_print(True)
        else:
            result_print(False)
    else:
        result_print(False)


email_validator()
