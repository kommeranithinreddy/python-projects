def celsius(f_temp):
    temp = (f_temp-32)/1.8
    print(f'{temp} * Celsius')

def fahrenheit(c_temp):
    temp = (c_temp*1.8) + 32
    print(f'{temp} * Fahrenheit')


celsius(100)
fahrenheit(37)
