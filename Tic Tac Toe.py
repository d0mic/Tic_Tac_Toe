#Modules and packages
from IPython.display import clear_output
from modulos import Functions as d

#Defining display_board with player turn decorator
display_dec_board = d.table_dec(d.display_board)

#Welcome message
print('\r\n********** "TIC TAC TOE" **********')
print('PLAY IN THE WINDOWS TERMINAL WITH THE TRACKPAD')

#Game logic
while d.game_on:
    
    while d.playing:

        display_dec_board()
        d.ask_position()
        d.search_result()
        if d.winner == True:
            print("\r\n--------------------")
            print(f"The {d.turn} won this game !!")
            print("--------------------\r\n")
            break
        if d.draw == True:
            print("\r\n-------------------------")
            print("The game ended as draw !!")
            print("-------------------------\r\n")
            break
        d.turn_change()
        clear_output()

    d.replay()