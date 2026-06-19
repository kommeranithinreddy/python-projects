def words_counter(sentence):
    count = 1
    string = ''
    for i in sentence:
        if i == ' ' and string != '':
            count += 1
            string = ''
        elif i != ' ':
            string += i

    return count

print(words_counter("Shubham is a python developer"))
