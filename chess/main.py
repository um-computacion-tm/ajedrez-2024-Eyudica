from chess.interfaz import Juego
import time
CLEAR="\033[H\033[J"

def main(): #Calcula el tiempo total de la partida y usa CLEAR para limpiar la pantalla, una vez que juego_finalizado de juego sea true termina la ejecucion y muestra el tiempo total de partida
    inicio=time.time()
    print(CLEAR)
    juego=Juego() 
    while not juego.__juego_finalizado__:
        if  juego.__juego_finalizado__:
            pass
        else:
            juego.turnos()
            print(CLEAR)
            juego.__tablero__.mostrar_tablero()
    print(CLEAR)        
    juego.__tablero__.mostrar_tablero()               
    print(f"El ganador es {juego.ganador}")
    fin=time.time()
    total=fin-inicio
    print(f"Tiempo total de partida: {round(total,2)} segundos")
if __name__ == '__main__':
    main()