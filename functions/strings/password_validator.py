def password_validator(password):
    upper_check = False
    lower_check = False
    number_check = False
    if len(password)>=8:
        for char in password:
            if 'A' <= char <= 'Z':
                upper_check = True
            if 'a' <= char <= 'z':
                lower_check = True
            if '0' <= char <= '9':
                number_check = True
        if upper_check and lower_check and number_check:
            return f'{password} is valid'
        else:
            return f'{password} is invalid'
    else:
        return f'{password} is invalid'



print(password_validator(input('Enter Your Password: ')))