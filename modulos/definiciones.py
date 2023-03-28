
from IPython.display import clear_output

def inicio_variables():
    """
    Función que establece el valor inicial de las variables generales del juego. Válido para primera ejecución o como para reinicio del juego.
    """
    #Primero, se hacen las variables globales
    global game_on
    global comienzo_juego
    global ganador
    global empate
    global posicion
    global turno
    global jugador1
    global jugador2
    global tablero

    #Segundo, se establecen los valores iniciales de las variables
    #Variables del juego
    game_on = True
    comienzo_juego = True
    ganador = False
    empate = False
    
    #Variables de jugadores
    posicion = ''
    turno = 'Jugador 1 (X)'
    jugador1 = 'X'
    jugador2 = 'O'
    
    #Variables de posiciones del tablero. Se establece un diccionario con un valor asignado a cada posición.
    tablero = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' ',}

def display_board():
    """
    Función que muestra el estado actual del tablero.
    """
    global tablero

    print(' ___________')
    print('|   |   |   |')
    print(f"| {tablero['7']} | {tablero['8']} | {tablero['9']} |")
    print('|___|___|___|')
    print('|   |   |   |')
    print(f"| {tablero['4']} | {tablero['5']} | {tablero['6']} |")
    print('|___|___|___|')
    print('|   |   |   |')
    print(f"| {tablero['1']} | {tablero['2']} | {tablero['3']} |")
    print('|___|___|___|\r\n')

def cambio_turno():
    """
    Función que cambia el turno de Jugador 1 a Jugador 2 y viceversa.
    """
    global turno

    if turno == 'Jugador 1 (X)':
        turno = 'Jugador 2 (O)'
    
    else:
        turno = 'Jugador 1 (X)'

def pregunta_posicion():
    """
    Pregunta al jugador la posición que elige y verifica que sea una respuesta válida.
    Una vez la posicion escogida es correcta, la asigna al diccionario 'tablero'.
    Válido tanto para Jugador 1 como para Jugador 2.
    """
    while True:
        
        global posicion

        #Se pregunta al jugador que casilla quiere marcar
        posicion = input('Elige tu próxima casilla (1-9): ') 
        
        #Se comprueba que el valor introducido es un número y no un string
        if posicion.isdigit() == False:
            #clear_output()
            print('No has elegido un valor correcto. Elige un número entre el 1 y el 9')
            
        else:
            if int(posicion) in range(1,10):
                #clear_output()

                #Se comprueba que la posición escogida no está ocupada
                if tablero[posicion] != ' ':
                    print('Esta posición está ocupada, elige otra!')
                    continue
                else:
                    if turno == 'Jugador 1 (X)':
                        tablero[posicion] = 'X'
                        break
                    else:
                        tablero[posicion] = 'O'
                        break
            else:
                #clear_output()
                print('No has elegido un valor correcto. Elige un número entre el 1 y el 9')

def buscar_resultado():
    """
    Función que verifica el tablero, buscando el estado de la partida entre estos casos:
        - Hay un ganador
        - La partida sigue (se produce cambio de turno)
        - Hay un empate
    """
    global ganador
    global empate

    #Con esta serie de if's, se comprueba si algún jugador ha ganado
    if (tablero['1'] == tablero['2'] == tablero['3'] == 'X') or (tablero['1'] == tablero['2'] == tablero['3'] == 'O'):
        ganador = True
    if (tablero['4'] == tablero['5'] == tablero['6'] == 'X') or (tablero['4'] == tablero['5'] == tablero['6'] == 'O'):
        ganador = True
    if (tablero['7'] == tablero['8'] == tablero['9'] == 'X') or (tablero['7'] == tablero['8'] == tablero['9'] == 'O'):
        ganador = True
    if (tablero['1'] == tablero['4'] == tablero['7'] == 'X') or (tablero['1'] == tablero['4'] == tablero['7'] == 'O'):
        ganador = True
    if (tablero['2'] == tablero['5'] == tablero['8'] == 'X') or (tablero['2'] == tablero['5'] == tablero['8'] == 'O'):
        ganador = True
    if (tablero['3'] == tablero['6'] == tablero['9'] == 'X') or (tablero['3'] == tablero['6'] == tablero['9'] == 'O'):
        ganador = True
    if (tablero['1'] == tablero['5'] == tablero['9'] == 'X') or (tablero['1'] == tablero['5'] == tablero['9'] == 'O'):
        ganador = True
    if (tablero['3'] == tablero['5'] == tablero['7'] == 'X') or (tablero['3'] == tablero['5'] == tablero['7'] == 'O'):
        ganador = True
    
    #Si hay ganador se da mensaje de victoria
    if ganador == True:
        print("\r\n---------------------------------")
        print(f"EL {turno} HA GANADO LA PARTIDA !!")
        print("---------------------------------\r\n")
    
    else:
        #Se busca si queda algún movimiento por hacer, si no queda ninguno, la partida acabó en empate
        for x in tablero.values():
            if x == ' ':
                break
            else:
                empate = True
                print("\r\n---------------------------------")
                print(f"LA PARTIDA HA ACABADO EN EMPATE !!")
                print("---------------------------------\r\n")
                
        empate = False
        cambio_turno()

def verificacion_final():
    """
    Función para verificar el estado de la partida
    """
    
    global game_on
    global comienzo_juego
    global ganador
    empate = True
    tablero_lleno = False
    
    buscar_resultado()
    
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
        print(f'HA GANADO EL {turno}, ENHORABUENA !!\r\n')
        
        volver_jugar()
    
    if empate == True and tablero_lleno == True:
        
        clear_output()
        print(f'LA PARTIDA HA ACABADO EN EMPATE !!')
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
        print('Hasta la próxima!!')
        game_on = False
        comienzo_juego = True
        ganador = False