
from chess.piezas.piezas import Piezas

class Torre(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Torre", color, posicion)

    def checkMovimiento(self, nueva_posicion):
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
