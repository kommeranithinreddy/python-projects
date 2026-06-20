def countup(parameter): # unwinding the call stack.
    if parameter <= 0 :
        return
    else:
        countup(parameter-1)
        print(parameter)


countup(10)
