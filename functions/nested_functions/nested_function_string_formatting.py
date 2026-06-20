def format_name(name):
    result_name = ''
    def inner():
        nonlocal result_name
        for char in name:
            if 'A' <= char <= 'Z':
                result_name += chr(ord(char) + 32)
            elif char == ' ':
                result_name += '_'
            else:
                result_name += char
    inner()
    return result_name

print(format_name("Nithin Reddy Kommera"))