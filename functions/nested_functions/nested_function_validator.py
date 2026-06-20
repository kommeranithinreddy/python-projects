def outer_validator(password):
    def inner_validator():
        len_check = False
        upper_check = False
        lower_check = False
        num_check = False
        char_check = False
        if len(password) >= 8:
            len_check = True
            for string in password:
                if 'A' <= string <= 'Z':
                    upper_check = True
                elif 'a' <= string <= 'z':
                    lower_check = True
                elif '0' <= string <= '9':
                    num_check = True
                else:
                    char_check = True
        if len_check and upper_check and  lower_check and num_check and char_check:
            return True
        else:
            return False
    result = inner_validator()
    if result:
        print(f'{password} is valid')
    else:
        print(f'{password} is invalid')

outer_validator("Nithin@1234")
