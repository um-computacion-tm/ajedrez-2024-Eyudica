from chess.piezas.piezas import Piezas
BLANCO='Blanco'
NEGRO='Negro'
#Peon
class Peon(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Peon", color, posicion)
        self.__movido__ = False  # Para el doble avance inicial

    def checkMovimiento(self, nueva_posicion):#metodo para los distintos mismos movimientos permitidos del peon, en el caso de que el color de la pieza sea negro, su direccion es negativa por propiedad del tablero
        nueva_columna, nueva_fila = nueva_posicion
        direccion = 1 if self.__color__ == BLANCO else -1
        casillas = []
        if nueva_columna == self.columna and nueva_fila == self.fila + direccion: #avanzar linealmente
            casillas.append((self.columna, self.fila + direccion))
        if (nueva_columna == self.columna + direccion or nueva_columna == self.columna - direccion) and nueva_fila == self.fila + direccion: #movimiento en diagonal
            casillas.append((nueva_columna, nueva_fila))
        fila_doble_avance = self.fila + (2 * direccion)
        if not self.__movido__ and nueva_columna == self.columna and nueva_fila == fila_doble_avance:# avance doble
            casillas.append((self.columna + (nueva_columna - self.columna), self.fila + direccion))
            casillas.append((self.columna, fila_doble_avance))
        return casillas
