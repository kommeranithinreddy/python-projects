contacts = {}

def add_contact():
    name = input("Enter name of the contact to add")
    number = input("Enter mobile number to link to contact")
    if name in contacts:
        print(f'{name} is already in contacts')
    else:
        contacts[name] = number
        print(f'{name} is added in contacts')

def remove_contact():
    name = input("Enter name of the contact to remove")
    if name in contacts:
        del contacts[name]
        print(f'{name} is removed from contacts')
    else:
        print(f'{name} is not in contacts')

def view_contacts():
    if contacts:
        for i in contacts:
            print(f'{i} -- {contacts[i]}')
    else:
        print('contacts book is empty')

def search_contacts():
    name = input("Enter name to search in contacts")
    if name in contacts:
        print(f'{name} -- {contacts[name]}')
    else:
        print(f'{name} is not in contacts')

def print_menu():
    print('''
1. Add contact
2. Remove contact
3. View contacts
4. Search contact 
5. Exit''')

def contact_book():
    while True:
        print_menu()
        operation = input("Enter operation to continue: ")
        match operation:
            case '1':
                add_contact()
            case '2':
                remove_contact()
            case '3':
                view_contacts()
            case '4':
                search_contacts()
            case '5':
                return
            case _ :
                print("invalid input - please try again")


contact_book()