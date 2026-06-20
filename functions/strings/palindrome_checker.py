def palindrome_checker(string):
    new_string = string[-1::-1]
    if string == new_string:
        print(f'{string} is Palindrome')
    else:
        print(f'{string} is not a Palindrome')

str1 = "nithin"
palindrome_checker(str1)