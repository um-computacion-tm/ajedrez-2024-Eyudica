
from chess.piezas.piezas import Piezas
#Torre
class Torre(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Torre", color, posicion)

    def checkMovimiento(self, nueva_posicion):#metodo para el movimiento de la torre, comprueba que el movimiento sea horizontal o vertical
                                             #itera sobre las posiciones entre la inicial y la final, y agrega todas estas posiciones a la lista casillas y la retorna para posteriormente verificar si hay una pieza bloqueando en el tablero
                                            #en el caso de que la casilla seria como devolver false(si el jugador intenta mover la pieza a la posicion actual de la pieza)
        nueva_columna, nueva_fila = nueva_posicion
        casillas = []
        if nueva_columna == self.columna:
            inicio_fila = min(self.fila, nueva_fila)
            fin_fila = max(self.fila, nueva_fila)
            for i in range(inicio_fila + 1, fin_fila):
                if i != self.fila:
                    casillas.append((self.columna, i))
            casillas.append(nueva_posicion)
        elif nueva_fila == self.fila:
            inicio_columna = min(self.columna, nueva_columna)
            fin_columna = max(self.columna, nueva_columna)
            for i in range(inicio_columna + 1, fin_columna):
                if i != self.columna:
                    casillas.append((i, self.fila))
            casillas.append(nueva_posicion)
        return casillas
