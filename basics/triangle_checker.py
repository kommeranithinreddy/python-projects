#Check for a Valid Triangle
#Input three sides and determine if they can form a triangle (triangle inequality rule).


a = float(input("Enter your 1st side length: "))
b = float(input("Enter your 2nd side length: "))
c = float(input("Enter your 3rd side length: "))

print('This is a Triangle')if a+b > c and b+c > a and c+a > b else print('This is not a triangle')
