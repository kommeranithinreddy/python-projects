book_store = {}

def add_book():
    book_name = input("Enter book name to add: ")
    book_count = int(input(f'Enter number of copies for adding {book_name} in store: '))
    if book_name in book_store:
        print(f'{book_name} is already in store - added copies to the existing book')
        book_store[book_name] += book_count
    else:
        book_store[book_name] = book_count
        print(f'{book_name} copies are added in the store')
        print(f'{book_name} available copies -- {book_store[book_name]}')

def view_books():
    if book_store:
        for i in book_store:
            print(f'Book - {i} , number of copies {book_store[i]} ')
    else:
        print('No books are available in store')


def borrow_book():
    book_name = input("Enter book name to borrow: ")
    if book_name in book_store:
        if book_store[book_name] >= 1:
            book_store[book_name] -= 1
            print(f'{book_name} is borrowed successfully')
        else:
            print(f'All {book_name} copies are borrowed from the store - please try again')
    else:
        print(f'{book_name} is not in book store - please try another book to borrow')


def return_book():
    book_name = input("Enter book name to return: ")
    if book_name in book_store:
        book_store[book_name] += 1
        print(f'{book_name} copy is returned')
    else:
        print(f'{book_name} is not from the store. Would you like to add it in the store?')

def search_book():
    book_name = input("Enter book name to search: ")
    if book_name in book_store:
        print(f'{book_name} is available in the store')
        print(f'No of copies of {book_name} -- {book_store[book_name]}' )
    else:
        print(f'{book_name} is not available in the store - please check for other book')


def print_menu():
    print('''
1. Add book
2. View Books
3. Borrow Book
4. Return Book
5. Search Book
6. Exit
''')

def library_management():
    while True:
        print_menu()
        operation = input('Enter the prompt to continue: ')
        match operation:
            case '1':
                add_book()
            case '2':
                view_books()
            case '3':
                borrow_book()
            case '4':
                return_book()
            case '5':
                search_book()
            case '6':
                return
            case _ :
                print("invalid input - please try again")

library_management()