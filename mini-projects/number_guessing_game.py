from random import randint

def guessing_game():
    attempts = 0
    value = randint(1, 100)
    while True:
        number = int(input(f'Enter number between 1 to 100: '))
        attempts += 1
        if number > value:
            print(f'Too High - try again')
        elif number < value:
            print(f'Too Low - try again')
        else:
            print(f"Correct, you have solved it in {attempts} attempt's")
            break

guessing_game()
