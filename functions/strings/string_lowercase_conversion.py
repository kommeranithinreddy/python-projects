def lowercase_converter(string):
    new_string = ''
    for i in string:
        if 65 <= ord(i) <= 90:
            new_chr = chr(ord(i) + 32)
            new_string += new_chr
        else:
            new_string += i
    return new_string

print(lowercase_converter("Nithin"))