def countdown(number):
    for num in range(number,0, -1):
        yield num


nums = countdown(10)

for i in nums:
    print(i)