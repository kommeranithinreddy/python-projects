def computer_input():
    from random import randint
    choice = randint(1, 3)
    match choice:
        case 1:
            return 'rock'
        case 2:
            return 'paper'
        case 3:
            return 'scissors'

def find_winner(user_choice):
    computer_choice = computer_input()
    print(f'user choice : {user_choice}')
    print(f'computer choice : {computer_choice}')
    if user_choice == computer_choice:
        print('Draw')
    else:
        match user_choice:
            case 'rock':
                if computer_choice == 'paper':
                    print('Computer wins')
                else:
                    print('User wins')
            case 'paper':
                if computer_choice == 'rock':
                    print('User wins')
                else:
                    print('Computer wins')
            case 'scissors':
                if computer_choice == 'rock':
                    print('Computer wins')
                else:
                    print('User wins')
            case _ :
                print('invalid input from user')


def play_game():
    user_choice = input('Enter your choice (rock/paper/scissors): ')
    find_winner(user_choice.lower())

play_game()