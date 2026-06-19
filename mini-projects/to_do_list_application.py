def add_task(name):
    if name in to_do_list:
        print(f'{name} is already in to-do list')
    else:
        to_do_list.append(name)
        print(f'{name} is added in to-do List')

def remove_task(name):
    if name in to_do_list:
        to_do_list.remove(name)
        print(f'{name} is removed from to-do list')
    else:
        print(f'{name} is not in to-do list')

def view_tasks():
    if len(to_do_list):
        for i in to_do_list:
            print(i)
    else:
        print('No tasks are added in to-do list')

def print_menu():
    print('''
    1.Add Task
2.Remove Task
3.View Tasks
4.Exit''')

def to_do():
    while True:
        print_menu()
        result = input('Select any task: ')
        match result:
            case '1':
                task_name = input('enter task name to add: ')
                add_task(task_name)
            case '2':
                task_name = input('enter task name to remove: ')
                remove_task(task_name)
            case '3':
                view_tasks()
            case '4':
                return
            case _ :
                print('invalid input - please try again')
to_do_list = []
to_do()