even_gen = (num for num in range(1, 21) if num%2 == 0)

print(list(even_gen))

simple_even = (num for num in range(2, 21, 2)) #better and efficient version
print(list(simple_even))