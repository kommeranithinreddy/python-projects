def temp_converter(converter):
    def cel_to_far(degrees):
        return (degrees * 1.8) + 32
    def far_to_cel(degrees):
        return (degrees - 32) * 5/9

    match converter.lower():
        case 'to_fahrenheit':    #names should be understandable
            return cel_to_far
        case 'to_celsius':      #names should be understandable
            return far_to_cel
        case _ :
            print('invalid syntax')

to_fahrenheit = temp_converter('to_fahrenheit')     #names should be understandable
to_celsius = temp_converter('to_celsius')       #names should be understandable

print(to_celsius(100))
print(to_fahrenheit(36))

