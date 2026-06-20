def outer():
    logs = []
    def inner():
        logs.append(input('Enter logs: '))
        print(logs)
    return inner

logger = outer()
logger()
logger()
logger()
logger()