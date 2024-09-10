from chess.piezas.piezas import Piezas
from chess.piezas.torre import Torre
from chess.piezas.alfil import Alfil
#Dama
class Dama(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Dama", color, posicion)

    def checkMovimiento(self, nueva_posicion):#metodo para el movimiento de la dama, si el movimiento es diagonal, logicamente funciona como un alfil.En el caso de que el movimiento es lineal, funciona logicamente como una torre
        movimiento_como_torre = Torre(self.color, self.__posicion__).checkMovimiento(nueva_posicion)
        movimiento_como_alfil = Alfil(self.color, self.__posicion__).checkMovimiento(nueva_posicion)
        if movimiento_como_torre or movimiento_como_alfil:
            return movimiento_como_torre + movimiento_como_alfil
        else:
            return []
