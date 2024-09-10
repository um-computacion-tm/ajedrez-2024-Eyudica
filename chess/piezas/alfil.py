from chess.piezas.piezas import Piezas
#Alfil
class Alfil(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Alfil", color, posicion)

    def checkMovimiento(self, nueva_posicion): #metodo para el movimiento del alfil, comprueba que el movimiento sea diagonal, que la cantidad de filas y columnas a mover sean iguales
                                               #itera sobre las posiciones entre la inicial y la final, y agrega todas estas posiciones a la lista casillas y la retorna para posteriormente verificar si hay una pieza bloqueando en el tablero
                                               #en el caso de que la casilla seria como devolver false(si el jugador intenta mover la pieza a la posicion actual de la pieza)
        casillas = []
        nueva_columna, nueva_fila = nueva_posicion
        direccion_columna = 1 if self.columna < nueva_columna else -1
        direccion_fila = 1 if self.fila < nueva_fila else -1
        if abs(self.columna - nueva_columna) == abs(self.fila - nueva_fila):
            columna_actual = self.columna + direccion_columna
            fila_actual = self.fila + direccion_fila
            while (columna_actual != nueva_columna) and (fila_actual != nueva_fila):
                casillas.append((columna_actual, fila_actual))
                columna_actual += direccion_columna
                fila_actual += direccion_fila
            casillas.append((columna_actual, fila_actual))
        return casillas
