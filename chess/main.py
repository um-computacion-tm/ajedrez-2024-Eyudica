from chess.interfaz import Juego

CLEAR="\033[H\033[J"

def main(): #Calcula el tiempo total de la partida y usa CLEAR para limpiar la pantalla, una vez que juego_finalizado de juego sea true termina la ejecucion y muestra el tiempo total
    print(CLEAR)
    juego=Juego() 
    while not juego.juego_finalizado:
        if  juego.juego_finalizado:
            pass
        else:
            juego.turnos()
            print(CLEAR)
            juego.tablero.mostrar_tablero()
    print(CLEAR)        
    juego.tablero.mostrar_tablero()               
    print(f"El ganador es {juego.ganador}")

if __name__ == '__main__':
    main()