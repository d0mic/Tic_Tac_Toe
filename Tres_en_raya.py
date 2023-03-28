#Importación de los módulos y funciones necesarias
from IPython.display import clear_output
from modulos import definiciones as d

#Estableciendo la lógica del juego para retocar las funciones.
#Las funciones no pueden depender de otras, tienen que ser totalmente independientes.
#De forma que al ejecutarlas la lógica del juego sea mucho más clara y no interfieran entre ellas.

#Inicio del juego. Se establecen las variables principales
d.inicio_variables()

#Mensaje de bienvenida al juego.
print('\r\nBIENVENIDOS AL JUEGO DEL TRES EN RAYA')
print('Versión de juego para jugar en la terminal de Windows')
print('Siempre comienza primero el Jugador 1 (X), Suerte !! \r\n')



#while df.game_on:
#    df.display()
#    posicion = df.pos_validar()
#    df.pos_tablero()
#    df.verificacion_final()