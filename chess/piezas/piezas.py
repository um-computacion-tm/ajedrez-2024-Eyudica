from chess.diccionarios import diccionarioSimbolos as simbolos
from chess.diccionarios import diccionarioFilas
BLANCO='Blanco'
NEGRO='Negro'
class Piezas():
    def __init__(self,tipo,color,posicion):
        self.__tipo__ = tipo
        self.__color__ = color
        self.__posicion__ = posicion
        self.__simbolo__ = self.obtenerSimbolos()
        self.__columna_anterior__ = self.columna
        self.__fila_anterior__ = self.fila
    @property 
    def columna(self):
        return self.__posicion__[0]
    @property
    def fila(self):
        return self.__posicion__[1]
    @property
    def color(self):
        return self.__color__
    @property
    def tipo(self):
        return self.__tipo__
    @property
    def simbolo(self):
        return self.__simbolo__
    def obtenerSimbolos(self):
        return simbolos[self.__color__][self.__tipo__]
    @property
    def columna_anterior(self):
        return self.__columna_anterior__
    @property
    def fila_anterior(self):
        return self.__fila_anterior__
    #--------------------------------------------------------------------
    @fila_anterior.setter
    def fila_anterior(self, value):
        self.__fila_anterior__ = value
    @columna_anterior.setter
    def columna_anterior(self, value):
        self.__columna_anterior__ = value
    @fila.setter
    def fila(self, value):
        self.__posicion__= (self.columna,value)
    @columna.setter
    def columna(self, value):
        self.__posicion__ = (value,self.fila)
    def establecerPosicion(self, nueva_posicion): #Recibe como parametro las coordenadas de la nueva posicion de la pieza, convierte el primer valor de las coordenadas(columnas) a letras como el estandar usado en el ajedrez
        self.columna_anterior, self.fila_anterior = self.__posicion__
        self.__posicion__=nueva_posicion
    def __str__(self):
       return f'La pieza es {self.__tipo__} con color {self.__color__} en la posicion {(self.columna,self.fila)} y el simbolo es {self.__simbolo__}'

