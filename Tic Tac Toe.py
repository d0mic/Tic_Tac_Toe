#Modules and packages
from IPython.display import clear_output
from modulos import Functions as d

#Defining display_board with player turn decorator
#display_dec_board = d.table_dec(d.display_board)

while d.in_game:

    #Welcome message
    print('\r\n********** "TIC TAC TOE" **********')
    print('PLAY IN THE WINDOWS TERMINAL WITH THE TRACKPAD')

    #Table variable. Initializes the table with all empty values.
    table = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}

    #Game logic
    while d.game_state == 'Playing':

        d.display_board(table)
        d.check_box(table,d.turn)
        d.game_state = d.check_game_state(table,d.turn)

        if d.game_state == 'Winner':
            d.display_board(table)
            print("\r\n--------------------")
            print(f"The {d.turn} won this game !!")
            print("--------------------\r\n")

        if d.game_state == 'Draw':
            d.display_board(table)
            print("\r\n-------------------------")
            print("The game ended as draw !!")
            print("-------------------------\r\n")

        d.turn = d.turn_change(d.turn)
        clear_output()

    d.game_state = 'Playing'
    d.in_game = d.check_in_game_state(d.in_game)