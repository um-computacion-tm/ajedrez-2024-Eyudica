from chess.piezas.piezas import Piezas

class Alfil(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Alfil", color, posicion)

    def checkMovimiento(self, nueva_posicion):
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
