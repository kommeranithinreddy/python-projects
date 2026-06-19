take = eval(input("Enter you charcacter: "))
Typ = type(take)
if isinstance(take, str):
    print(f"{take} is character")
elif isinstance(take, int):
    print(f"{take} is Int")
else:
    print('not a type')
