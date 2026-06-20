def char_frequency(string, char):
    count = 0
    for i in string:
        if i == char:
            count += 1
    return count

print(char_frequency("nithin", "n"))