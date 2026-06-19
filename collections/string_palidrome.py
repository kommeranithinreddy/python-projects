#Palidrome
string = input("Enter Your string: ")
temp2 = ''

for i in range(len(string)-1, -1):
    temp2 = temp2+string(i)

if temp2 == string:
    print("String is palidrome")
else:
    print("String is not palidrome")
