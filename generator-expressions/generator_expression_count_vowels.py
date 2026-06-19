string = 'nithinreddykommera'

vowels = (value for value in string if value in 'AEIOUaeiou')

count = 0
for _ in vowels:
    count += 1

print(count)