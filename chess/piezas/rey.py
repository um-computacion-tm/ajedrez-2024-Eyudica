from chess.piezas.piezas import Piezas

class Rey(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Rey", color, posicion)

    def checkMovimiento(self, nueva_posicion):
        nueva_columna, nueva_fila = nueva_posicion
        col_actual = self.columna
        fila_actual = self.fila
        movimiento_columna = abs(nueva_columna - col_actual)
        movimiento_fila = abs(nueva_fila - fila_actual)

        if movimiento_columna <= 1 and movimiento_fila <= 1:
            return True
        return False
