
from IPython.display import clear_output

#Variables

#Global variables
global game_on
global playing
global winner
global draw
global position
global turn
global table

#Game variables
game_on = True
playing = True
winner = False
draw = False
    
#Players variables
position = ''
turn = 'Player 1 (X)'
    
#Table variable. Stablishes a dictionary with table values.
table = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' ',}

#Functions

def display_board():
    """
    Function that shows the current table state.
    """
    global table

    print(' ___________')
    print('|   |   |   |')
    print(f"| {table['7']} | {table['8']} | {table['9']} |")
    print('|___|___|___|')
    print('|   |   |   |')
    print(f"| {table['4']} | {table['5']} | {table['6']} |")
    print('|___|___|___|')
    print('|   |   |   |')
    print(f"| {table['1']} | {table['2']} | {table['3']} |")
    print('|___|___|___|\r\n')

def turn_change():
    """
    Function that changes the turn of players.
    """
    global turn

    if turn == 'Player 1 (X)':
        turn = 'Player 2 (O)'
    
    else:
        turn = 'Player 1 (X)'

def ask_position():
    """
    Asks for the position selection and verifies that is a valid choice.
    Once the position is valid, asings it to 'table'.
        """
    while True:
        
        global position
        global table
        global turn

        #Asks the player for the next move
        position = input('Choose your next move (1-9): ') 
        
        #Verifies that the data introduced is an int, not str
        if position.isdigit() == False:
            #clear_output()
            print('Invalid choice. Choose a number between 1 and 9.')
            
        else:
            if int(position) in range(1,10):
                #clear_output()

                #Verifies that selected position is not ocuppied
                if table[position] != ' ':
                    print('Invalid choice. Select other position!')
                    continue
                else:
                    if turn == 'Player 1 (X)':
                        table[position] = 'X'
                        break
                    else:
                        table[position] = 'O'
                        break
            else:
                #clear_output()
                print('Invalid choice. Choose a number between 1 and 9.')

def search_result():
    """
    Function that verifies the table, searching the result of the game between this cases: Winner, Draw, Continue Game.
    """
    global winner
    global draw
    global table

    #Conditions for winning
    if (table['1'] == table['2'] == table['3'] == 'X') or (table['1'] == table['2'] == table['3'] == 'O'):
        winner = True
    if (table['4'] == table['5'] == table['6'] == 'X') or (table['4'] == table['5'] == table['6'] == 'O'):
        winner = True
    if (table['7'] == table['8'] == table['9'] == 'X') or (table['7'] == table['8'] == table['9'] == 'O'):
        winner = True
    if (table['1'] == table['4'] == table['7'] == 'X') or (table['1'] == table['4'] == table['7'] == 'O'):
        winner = True
    if (table['2'] == table['5'] == table['8'] == 'X') or (table['2'] == table['5'] == table['8'] == 'O'):
        winner = True
    if (table['3'] == table['6'] == table['9'] == 'X') or (table['3'] == table['6'] == table['9'] == 'O'):
        winner = True
    if (table['1'] == table['5'] == table['9'] == 'X') or (table['1'] == table['5'] == table['9'] == 'O'):
        winner = True
    if (table['3'] == table['5'] == table['7'] == 'X') or (table['3'] == table['5'] == table['7'] == 'O'):
        winner = True
    
    else:
        #Search if there is any movement left, if not the game ends as a draw
        for x in table.values():
            if x == ' ':
                draw = False
                break
            else:
                draw = True

def replay():
    """
    Function that asks if players want to replay or end the game.
    """
    
    global game_on
    global playing
    global winner
    global draw
    global position
    global table
    global turn
    
    answer = input('Do you want to play again? (y/n): ')
        
    if (answer == 'y') == True:
            
        #Game variables
        game_on = True
        playing = True
        winner = False
        draw = False
            
        #Players variables
        position = ''
        turn_change()
            
        #Table variable. Stablishes a dictionary with table values.
        table = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
        
    if (answer == 'n') == True:
            
        clear_output()
        print('Good Bye !!')
        game_on = False

#Decorators

def table_dec(original):

    def wrap_func():

        print(f"*** It's {turn} turn ***")
        original()

    return wrap_func