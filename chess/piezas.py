from diccionarios import diccionarioSimbolos as simbolos
from diccionarios import diccionarioFilas
#from tablero import Tablero
#Global vars
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
    def obtenerSimbolos(self): #Entra en el diccionario de simbolos para obtener basandose en el color y el tipo de pieza
        return simbolos[self.__color__][self.__tipo__]
    @property
    def columna_anterior(self):
        return self.__columna_anterior__
    @property
    def fila_anterior(self):
        return self.__fila_anterior__
    def establecerPosicion(self, nueva_posicion): #Recibe como parametro las coordenadas de la nueva posicion de la pieza, convierte el primer valor de las coordenadas(columnas) a letras como el estandar usado en el ajedrez
        self.__columna_anterior__ = self.columna
        self.__fila_anterior__ =self.fila
        self.__posicion__ = nueva_posicion
        columna = nueva_posicion[0]
        fila = int(nueva_posicion[1]) - 1
        
        return columna, fila
    def __str__(self):
        return f'La pieza es {self.__tipo__} con color {self.__color__} en la posicion {(self.columna,self.fila)} y el simbolo es {self.__simbolo__}'

class Peon(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Peon", color, posicion)
        self.__movido__=False #Para el doble avance inicial
    def checkMovimiento(self,nueva_posicion): #determina los distintos movimientos permitidos del peon con condicionales
        nueva_columna, nueva_fila =  nueva_posicion
        direccion=1 if self.__color__==BLANCO else -1
        if nueva_columna==self.columna and nueva_fila==self.fila+direccion: #avanzar linealmente
            return True
        if (nueva_columna==self.columna+1 or nueva_columna==self.columna-1) and nueva_fila==self.fila+direccion: #comer en diagonal   
            return True
        fila_doble_avance=self.fila+(2*direccion)
        if not self.__movido__ and nueva_columna==self.columna and nueva_fila==fila_doble_avance :#doble avance
            return True
        return False


class Torre(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Torre", color, posicion)
    def checkMovimiento(self,nueva_posicion): 
        nueva_columna, nueva_fila =  nueva_posicion
        inicio_fila = min(self.fila, nueva_fila) + 1; #para calcular  a partir de la proxima casilla
        fin_fila = max(self.fila, nueva_fila)
        if nueva_columna!=self.columna and nueva_fila!=self.fila: #bloquear el movimiento diagonal
            return False
        return True

class Alfil(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Alfil", color, posicion)
    def checkMovimiento(self,nueva_posicion): #comprueba que el movimiento sea diagonal
        nueva_columna, nueva_fila =  nueva_posicion
        diferencia_columnas=abs(self.columna-nueva_columna) 
        diferencia_filas=abs(self.fila-nueva_fila)
        if diferencia_columnas==diferencia_filas:# al ser un movimiento diagonal, la diferencia de columnas y filas debe ser igual
                return True
        return False
    
class Dama(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Dama", color, posicion)

    def checkMovimiento(self, nueva_posicion): #crea las instancias de torre y alfil, con la posicion y color de la dama. Esto esta para que la dama pueda replicar sus movimientos
        
        self.Torre_movimiento = Torre(self.__color__, self.__posicion__)
        self.Alfil_movimiento = Alfil(self.__color__, self.__posicion__)
        return self.Torre_movimiento.checkMovimiento(nueva_posicion) or self.Alfil_movimiento.checkMovimiento(nueva_posicion)
class Caballo(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Caballo", color, posicion)
    
    def checkMovimiento(self, nueva_posicion):#crea una tupla con los movimientos permitidos del caballo, si la nueva posicion esta en la tupla, devuelve true
        nueva_columna, nueva_fila =  nueva_posicion
        col_actual=self.columna
        fila_actual=self.fila
        posibles_movimientos=((col_actual-2,fila_actual-1),(col_actual-2,fila_actual+1),(col_actual+1,fila_actual+2),(col_actual-1,fila_actual+2),(col_actual+2,\
        fila_actual+1),(col_actual+2,fila_actual-1),(col_actual+1,fila_actual-2),(col_actual-1,fila_actual-2)) #posibles movimientos a partir de la posicio actual
        if (nueva_columna,nueva_fila) in posibles_movimientos:
            return True
        return False
   
class Rey(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Rey", color, posicion)
    
    def checkMovimiento(self, nueva_posicion, ):#Lo mismo que con el caballo solo que separe las distintas combinaciones dependiendo del tipo de movimiento para mayor legibilidad
        nueva_columna, nueva_fila =  nueva_posicion
        posibles_movimientos_lineales=((self.columna-1,self.fila),(self.columna+1,self.fila),(self.columna,self.fila+1),(self.columna,self.fila-1))   
        posibles_movimientos_diagonales=((self.columna-1,self.fila+1),(self.columna+1,self.fila-1),(self.columna+1,self.fila+1),(self.columna-1,self.fila-1))
        if (nueva_columna,nueva_fila)  in (posibles_movimientos_lineales + posibles_movimientos_diagonales):
            return True
        return False
# rey=Rey(BLANCO,(3,3))
# print(rey.checkMovimiento((5,3)))