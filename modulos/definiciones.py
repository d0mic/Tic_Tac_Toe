
from IPython.display import clear_output

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

def board():
    """
    Función que muestra el tablero de juego
    """
    
    print(' ___________')
    print('|   |   |   |')
    print(f"| {tablero['7']} | {tablero['8']} | {tablero['9']} |")
    print('|___|___|___|')
    print('|   |   |   |')
    print(f"| {tablero['4']} | {tablero['5']} | {tablero['6']} |")
    print('|___|___|___|')
    print('|   |   |   |')
    print(f"| {tablero['1']} | {tablero['2']} | {tablero['3']} |")
    print('|___|___|___|')

def cambio_turno():
    """
    Función que cambia el turno de un jugador al otro
    """
    
    global turno
    
    if turno == 'Jugador 1 (X)':
                
        turno = 'Jugador 2 (O)'
    
    else:
        
        turno = 'Jugador 1 (X)'

def validar_tablero():
    """
    Función que verifica el tablero, buscando el estado de la partida:
        - No hay ganador
        - Hay ganador
    """
    
    global ganador
    
    if (tablero['1'] == 'X' and tablero['2'] == 'X' and tablero['3'] == 'X') == True:
        ganador = True
    if (tablero['4'] == 'X' and tablero['5'] == 'X' and tablero['6'] == 'X') == True:
        ganador = True
    if (tablero['7'] == 'X' and tablero['8'] == 'X' and tablero['9'] == 'X') == True:
        ganador = True
    if (tablero['1'] == 'X' and tablero['4'] == 'X' and tablero['7'] == 'X') == True:
        ganador = True
    if (tablero['2'] == 'X' and tablero['5'] == 'X' and tablero['8'] == 'X') == True:
        ganador = True
    if (tablero['3'] == 'X' and tablero['6'] == 'X' and tablero['9'] == 'X') == True:
        ganador = True
    if (tablero['1'] == 'X' and tablero['5'] == 'X' and tablero['9'] == 'X') == True:
        ganador = True
    if (tablero['3'] == 'X' and tablero['5'] == 'X' and tablero['7'] == 'X') == True:
        ganador = True
        
    if (tablero['1'] == 'O' and tablero['2'] == 'O' and tablero['3'] == 'O') == True:
        ganador = True
    if (tablero['4'] == 'O' and tablero['5'] == 'O' and tablero['6'] == 'O') == True:
        ganador = True
    if (tablero['7'] == 'O' and tablero['8'] == 'O' and tablero['9'] == 'O') == True:
        ganador = True
    if (tablero['1'] == 'O' and tablero['4'] == 'O' and tablero['7'] == 'O') == True:
        ganador = True
    if (tablero['2'] == 'O' and tablero['5'] == 'O' and tablero['8'] == 'O') == True:
        ganador = True
    if (tablero['3'] == 'O' and tablero['6'] == 'O' and tablero['9'] == 'O') == True:
        ganador = True
    if (tablero['1'] == 'O' and tablero['5'] == 'O' and tablero['9'] == 'O') == True:
        ganador = True
    if (tablero['3'] == 'O' and tablero['5'] == 'O' and tablero['7'] == 'O') == True:
        ganador = True

def pos_validar():
    """
    Función para validar la posición elegida por el jugador
    """
    
    eleccion = 'wrong'
    en_rango = False
    
    while eleccion.isdigit() == False or en_rango == False:
        
        eleccion = input('Elige tu próxima casilla (1-9): ') 
        
        if eleccion.isdigit() == False:
            
            #clear_output()
            print('No has elegido un valor correcto. Elige un número entre el 1 y el 9')
            
        if eleccion.isdigit() == True:
            
            if int(eleccion) in range(1,10):
                #clear_output()
                en_rango = True
            else:
                #clear_output()
                print('No has elegido un valor correcto. Elige un número entre el 1 y el 9')
                en_rango = False
                
    return eleccion

def pos_tablero():
    """
    Función que valida y asigna la posición elegida por el jugador en el tablero
    """
    
    global posicion
    
    while tablero[posicion] != ' ':
        
        print('Esta posición está ocupada, elige otra!')
        
        posicion = pos_validar()
    
    if turno == 'Jugador 1 (X)':
    
        tablero[posicion] = 'X'
    
    else:
        
        tablero[posicion] = 'O'

def display():
    """
    Función que muestra el tablero en la pantalla (modificar esta función ya que está duplicada)
    """
    
    global tablero
    global comienzo_juego
    global game_on
    global turno
    
    clear_output()
    
    if comienzo_juego == True:
        
        turno = 'Jugador 1 (X)'
        tablero = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' ',}
        print('Bienvenidos al 3 en Raya !!')
        print('Poned vuestras mentes a punto y que gane el mejor')
        print('Siempre comienza primero el Jugador 1 (X), Suerte !! \r\n')
        comienzo_juego = False
    
    print(f'Turno de {turno}')
    board()

def verificacion_final():
    """
    Función para verificar el estado de la partida
    """
    
    global game_on
    global comienzo_juego
    global ganador
    empate = True
    tablero_lleno = False
    
    validar_tablero()
    
    if ganador == False:
        
        for x in tablero.values():
            
            if x ==  ' ':
                
                empate = False
            
            else:
                
                tablero_lleno = True            
            
        cambio_turno()
        
    if ganador == True:
        
        clear_output()
        print(f'HA GANADO EL {turno}, ENHORABUENA !!')
        board()
        print(f'HA GANADO EL {turno}, ENHORABUENA !!\r\n')
        
        volver_jugar()
    
    if empate == True and tablero_lleno == True:
        
        clear_output()
        print(f'LA PARTIDA HA ACABADO EN EMPATE !!')
        board()
        print(f'LA PARTIDA HA ACABADO EN EMPATE !!\r\n')
        
        volver_jugar()

def volver_jugar():
    """
    Función para preguntar si se reinicia el juego o se sale de él
    """
    
    global game_on
    global comienzo_juego
    global ganador
    
    respuesta = input('Quereis volver a jugar? (y/n): ')
        
    if (respuesta == 'y') == True:
            
        comienzo_juego = True
        ganador = False
        
    if (respuesta == 'n') == True:
            
        clear_output()
        board()
        print('Hasta la próxima!!')
        game_on = False
        comienzo_juego = True
        ganador = False