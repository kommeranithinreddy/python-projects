#UpperLowerConverter

char = input("Enter  your Alphabet: ")
change = ord(char) + 32
chg = ord(char) - 32

if 64<ord(char)<91:
    print(chr(change))
elif 96<ord(char)<123:
    print(chr(chg))
else:
    print("Please enter only Alphabets")
