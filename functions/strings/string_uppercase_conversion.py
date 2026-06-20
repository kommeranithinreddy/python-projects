def uppercase_converter(string):
    new_string = ''
    for i in string:
        if 97 <= ord(i) <= 122:
            new_chr = chr(ord(i) - 32)
            new_string += new_chr
        else:
            new_string += i
    return new_string

print(uppercase_converter("nithin"))