from random import randint

str_list = 'aK9#mP2xQw7@tY1!L2$zP8nK'
def pass_generator():
    while True:
        password = ''
        for _ in range(8):
            password += str_list[randint(0, len(str_list) - 1)]
        yield password


password1 = pass_generator()

print(next(password1))
print(next(password1))
print(next(password1))
print(next(password1))

