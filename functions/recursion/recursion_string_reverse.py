def reverse(string): #updated version
    if string != '':
        return reverse(string[1:]) + string[0]
    else:
        return ''


print(reverse('reddy'))

