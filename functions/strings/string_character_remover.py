def space_remover(string, char = ' '):
    new_string = ''
    for i in string:
        if i != char:
            new_string += i
    return new_string

print(space_remover('nith in'))