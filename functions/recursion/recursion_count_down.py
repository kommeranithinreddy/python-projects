def countdown(parameter):
    if parameter == 0:
        return
    elif parameter > 0:
        print(parameter)
        return countdown(parameter - 1)
    else:
        print(f'parameter should be positive')



countdown(10)