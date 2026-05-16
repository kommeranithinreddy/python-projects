#Write a program to accept percentage from the user and display the grade according to the crieteria:


per = int(input("Enter your percentage: "))
if per>90:
    print("Grade A")
elif 80<per<=90:
    print("Grade B")
elif 60<=per<=80:
    print("Grade C")
else:
    print("Grade D")
