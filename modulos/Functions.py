from IPython.display import clear_output

#Variables
in_game = True
game_state = 'Playing'
turn = 'Player 1 (X)'

#Functions

def display_board(table_state : dict) -> None:
    """
    Function that shows the current table state.
    """
    
    print(' ___________')
    print('|   |   |   |')
    print(f"| {table_state['7']} | {table_state['8']} | {table_state['9']} |")
    print('|___|___|___|')
    print('|   |   |   |')
    print(f"| {table_state['4']} | {table_state['5']} | {table_state['6']} |")
    print('|___|___|___|')
    print('|   |   |   |')
    print(f"| {table_state['1']} | {table_state['2']} | {table_state['3']} |")
    print('|___|___|___|\r\n')

def turn_change(turn_state : str) -> str:
    """
    Function that changes the turn of players.
    """

    if turn_state == 'Player 1 (X)':
        return 'Player 2 (O)'
    
    else:
        return 'Player 1 (X)'

def check_box(table_state : dict, turn_state : str) -> None:
    """
    Asks for the position selection and verifies that is a valid choice.
    Once the position is valid, asings a 'X' or 'O' to 'table_state'.
    """

    valid_positions = [1,2,3,4,5,6,7,8,9]

    while True:
        
        #Asks the player for the next move
        position = input('Choose your next move (1-9): ') 
        
        try:
            #Verifies data introduced and asings it to table_state if it's valid
            if int(position) in valid_positions:

                if table_state[position] == ' ':

                    if turn_state == 'Player 1 (X)':
                        table_state[position] = 'X'
                        break
                    else:
                        table_state[position] = 'O'
                        break
                else:
                    print('Invalid choice. Select other position!')
            else:
                print('Invalid choice. Choose a number between 1 and 9.')

        except ValueError:
            print('Invalid choice. Choose a number between 1 and 9.')
            
def check_game_state(table_state : dict, turn_state : str) -> str:
    """
    Function that verifies the table, searching the result of the game between this cases: Winner, Draw, continue Playing.
    """

    #Conditions for winning
    if (table_state['1'] == table_state['2'] == table_state['3'] == 'X') or (table_state['1'] == table_state['2'] == table_state['3'] == 'O'):
        return 'Winner'
    if (table_state['4'] == table_state['5'] == table_state['6'] == 'X') or (table_state['4'] == table_state['5'] == table_state['6'] == 'O'):
        return 'Winner'
    if (table_state['7'] == table_state['8'] == table_state['9'] == 'X') or (table_state['7'] == table_state['8'] == table_state['9'] == 'O'):
        return 'Winner'
    if (table_state['1'] == table_state['4'] == table_state['7'] == 'X') or (table_state['1'] == table_state['4'] == table_state['7'] == 'O'):
        return 'Winner'
    if (table_state['2'] == table_state['5'] == table_state['8'] == 'X') or (table_state['2'] == table_state['5'] == table_state['8'] == 'O'):
        return 'Winner'
    if (table_state['3'] == table_state['6'] == table_state['9'] == 'X') or (table_state['3'] == table_state['6'] == table_state['9'] == 'O'):
        return 'Winner'
    if (table_state['1'] == table_state['5'] == table_state['9'] == 'X') or (table_state['1'] == table_state['5'] == table_state['9'] == 'O'):
        return 'Winner'
    if (table_state['3'] == table_state['5'] == table_state['7'] == 'X') or (table_state['3'] == table_state['5'] == table_state['7'] == 'O'):
        return 'Winner'
        
    #Search if there is any movement left, if not the game ends as a draw
    for x in table_state.values():

        if x == ' ': 
            return 'Playing' #If just 1 box is empty, means that are movements left, so returns "Playing"
        else:
            continue

    #Every box is used and nobody won, so returns "Draw"
    return 'Draw'

def check_in_game_state(in_game_state : bool) -> bool:
    """
    Function that asks if players want to replay or end the game.
    """
    answers =['y','n']

    while True:

        answer = input('Do you want to play again? (y/n): ').lower()

        if answer in answers:
            if answer == 'y':
                in_game_state = True
                return in_game_state
                
            if answer == 'n':
                in_game_state = False
                print("Thanks for playing, see you next time")
                return in_game_state
        else:
            print("Please say yes (y) or no (n)")
        
    

#Decorators

#def table_dec(original):
#
#   def wrap_func():
#
#        print(f"*** It's {turn} turn ***")
#        original()
#
#    return wrap_func


if __name__ == "__main__":
    print("File containing all the fucntions to play Tic Tac Toe")