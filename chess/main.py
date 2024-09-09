from chess.interfaz import Juego
import time
CLEAR = "\033[H\033[J" # para limpiar la pantalla

def main(): #funcion main , mientras que juego_finalizado de juego sea false se ejecuta, sino termina y muestra el tiempo total de partida
    juego = Juego()
   # tablero = Tablero()
    inicio = time.time()

    juego.inicializarPiezas()
    juego.agregarPiezasEnTablero()

    while not juego.__juego_finalizado__:
	#print(CLEAR)
        juego.__tablero__.mostrar_tablero()
        juego.turnos()
        juego.determinarGanador()

        if juego.__juego_finalizado__:
            break
        posiciones=juego.ProcesarInput()
        if not posiciones:
            break
        posicion_actual, posicion_final = posiciones
        if not juego.moverPieza(posicion_actual, posicion_final):
            continue
          
        print(CLEAR)    

    print(CLEAR)
    juego.__tablero__.mostrar_tablero()               
    fin = time.time()
    total = fin - inicio
    print(f"El ganador es {juego.__ganador__}")
    print(f"Tiempo total de partida: {round(total/60, 2)} minutos")

if __name__ == '__main__':
    main()
