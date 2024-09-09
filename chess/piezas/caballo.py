from chess.piezas.piezas import Piezas
#Caballo
class Caballo(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Caballo", color, posicion)

    def checkMovimiento(self, nueva_posicion):#metodo para el movimiento del caballo, comprueba que el movimiento sea de 2 columnas o 1 y de 2 o 1 filas 
        nueva_columna, nueva_fila = nueva_posicion
        col_actual = self.columna
        fila_actual = self.fila
        movimiento_columna = abs(nueva_columna - col_actual)
        movimiento_fila = abs(nueva_fila - fila_actual)
        if (movimiento_columna == 2 and movimiento_fila == 1) or (movimiento_columna == 1 and movimiento_fila == 2):
            return True
        return False
