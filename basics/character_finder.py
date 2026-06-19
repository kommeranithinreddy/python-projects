#Character or digit or special character finder

take = input("Enter you charcacter: ")
inp = ord(take)

if 64<inp<91 or 96<inp<123:
    print(f"{take} is a character")
elif 47<inp<58:
    print(f'{take} is a digit')
else:
    print(f'{take} is a Special Character')
