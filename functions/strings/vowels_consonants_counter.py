def vowels(string):
    vowels_count = 0
    for i in string:
        if i.lower() in ['a', 'e', 'i', 'o', 'u']:
           vowels_count += 1
    return vowels_count

#we can write 'aeiouAEIOU' as a string for better use-case.

def consonants(string):
    consonants_count = 0
    for i in string:
        if i.lower() not in ['a', 'e', 'i', 'o', 'u']:
           consonants_count += 1
    return consonants_count


print(vowels("Iithin"))
print(consonants("Nithin"))