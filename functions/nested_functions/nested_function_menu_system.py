task_list = []
def menu(tasks):
    def add_task():
        tasks.append(input('Enter the task name to add: '))
        print('Task is added')
    def remove_task():
        task_name = input('Enter task name to remove: ')
        if task_name in tasks:
            tasks.remove(task_name)
            print('Task is removed')
        else:
            print(f'{task_name} is not in the tasks')
    def view_tasks():
        if len(tasks):
            for task in tasks:
                print(task, end = ' ')
            print()
        else:
            print('No tasks are added')
    while True:
        print(''' 
        1. To add a task
        2. To remove a task
        3. To view all tasks
        4. Exit
        ''')
        user_input = input('Enter your prompt: ')
        match user_input:
            case '1':
                add_task()
            case '2':
                remove_task()
            case'3':
                view_tasks()
            case '4':
                return
            case _:
                print('input is not valid')

menu(task_list)



