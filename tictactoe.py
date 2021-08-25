import numpy as np 
import random
import time

main = np.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
empty = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]


def check_match(board, entry):

    check = [board[0], board[1], board[2], [i[0] for i in board], [i[1] for i in board], [i[2] for i in board],
             [board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
    
    for i in check:
        if all(item == entry for item in i):
            return True
        
    return False
                
                
def random_bot():

    time.sleep(1)
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    
    if empty[x][y] == '*':
        empty[x][y] = 'o'
    else:
        random_bot()


def run():

    game_on = True
        
    while game_on:
            
        print('This is your reference board')
        print('\n'.join(' '.join(map(str, sl)) for sl in main))
        print('\n')
        print('This is your playing board')
        print('\n'.join(' '.join(map(str, sl)) for sl in empty))
                
        value = input('What position would you place your "x" mark? ')
                
        position = np.where(main == str(value))
                
        if position and empty[position[0][0]][position[1][0]] == '*':
                    
            empty[position[0][0]][position[1][0]] = 'x'
            print('\n'.join(' '.join(map(str, sl)) for sl in empty))
                
            if check_match(empty, 'x'):
                print('You won!')
                game_on = False
                
            else:
                print('bot is playing')
                random_bot()
                print('\n'.join(' '.join(map(str, sl)) for sl in empty))
                    
            if check_match(empty, 'o'):
                print('The bot won!')
                game_on = False
                
        else:
            print('Wrong selection! Select again!')
            run()


while input('Do you want to play the game? y or n: ') == 'y':
    run()
