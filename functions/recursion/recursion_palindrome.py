def is_palindrome(string): #Most updated form
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])

    return False

print(is_palindrome('i'))