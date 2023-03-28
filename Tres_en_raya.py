#VARIBALES DEL JUEGO

from IPython.display import clear_output
from modulos import definiciones as df

    #generales
game_on = True
comienzo_juego = True
ganador = False
    #jugadores
posicion = ''
turno = 'Jugador 1 (X)'
jugador1 = 'X'
jugador2 = 'O'
    #posiciones del tablero
tablero = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' ',}

while game_on:
    df.display()
    posicion = df.pos_validar()
    df.pos_tablero()
    df.verificacion_final()