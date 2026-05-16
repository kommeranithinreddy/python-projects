print("Finding Course Fee")
print("1.Python")
print("2.Java")
print("3..Net")
print("4.Exit")
opt = int(input("Enter digit: "))

match(opt):
    case 1:
        print("Python 20000/-")
    case 2:
        print("Java 12000/_")
    case 3:
        print(".Net 10000/-")
    case 4:
        print("Thank you")
    case _:
        print("Invalid input")
