#Symmetric

string = input("Enter Your string: ")

temp = ''
if len(string)%2 != 0:
    print("String is not symmetric")
else:
    for i in range(len(string)//2):
        temp = temp + string[i]
    if temp*2 == string:
        print("String is  symmetric")
    else:
        print("String is not a symmetric")


