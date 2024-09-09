from diccionarios import diccionarioSimbolos as simbolos
from diccionarios import diccionarioFilas
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
        self.__fila__ = value
    @columna.setter
    def columna(self, value):
        self.__columna__ = value
    def establecerPosicion(self, nueva_posicion): #Recibe como parametro las coordenadas de la nueva posicion de la pieza, convierte el primer valor de las coordenadas(columnas) a letras como el estandar usado en el ajedrez
        self.columna_anterior, self.fila_anterior = self.__posicion__
        self.__posicion__=nueva_posicion
    def __str__(self):
       return f'La pieza es {self.__tipo__} con color {self.__color__} en la posicion {(self.columna,self.fila)} y el simbolo es {self.__simbolo__}'

class Peon(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Peon", color, posicion)
        self.__movido__=False #Para el doble avance inicial
    def checkMovimiento(self,nueva_posicion): #determina los distintos movimientos permitidos del peon con condicionales
        nueva_columna, nueva_fila =  nueva_posicion
        direccion=1 if self.__color__==BLANCO else -1
        casillas=[]
        if nueva_columna==self.columna and nueva_fila==self.fila+direccion: #avanzar linealmente
            casillas.append((self.columna,self.fila+direccion))
        if (nueva_columna == self.columna + direccion or nueva_columna == self.columna - direccion) and nueva_fila == self.fila + direccion:
            casillas.append((nueva_columna, nueva_fila))

        fila_doble_avance=self.fila+(2*direccion)
        if not self.__movido__ and nueva_columna==self.columna and nueva_fila==fila_doble_avance :#doble avance
            casillas.append((self.columna+(nueva_columna-self.columna),self.fila+direccion))
            casillas.append((self.columna,fila_doble_avance))
        return casillas


class Torre(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Torre", color, posicion)
    def checkMovimiento(self, nueva_posicion):
        nueva_columna, nueva_fila = nueva_posicion
        casillas = []
        #if nueva_columna != self.columna and nueva_fila != self.fila:  #bloquear el movimiento diagonal
        #    return False
        
        if nueva_columna == self.columna:
            inicio_fila = min(self.fila, nueva_fila)
            fin_fila = max(self.fila, nueva_fila)
            for i in range(inicio_fila+1, fin_fila):
                if i != self.fila:  
                    casillas.append((self.columna, i))
            casillas.append(nueva_posicion)
        elif nueva_fila == self.fila:
            inicio_columna = min(self.columna, nueva_columna)
            fin_columna = max(self.columna, nueva_columna)
            for i in range(inicio_columna+1, fin_columna):
                if i != self.columna: 
                    casillas.append((i, self.fila))
            casillas.append(nueva_posicion)
        return casillas

class Alfil(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Alfil", color, posicion)
    def checkMovimiento(self,nueva_posicion): #comprueba que el movimiento sea diagonal
        casillas=[]
        nueva_columna, nueva_fila =  nueva_posicion
        
        direccion_columna=1 if self.columna<nueva_columna else -1
        direccion_fila=1 if self.fila<nueva_fila else -1
        if abs(self.columna-nueva_columna)==abs(self.fila-nueva_fila):
            columna_actual=self.columna+direccion_columna
            fila_actual=self.fila+direccion_fila
            while (columna_actual!=nueva_columna) and (fila_actual!=nueva_fila):
                casillas.append((columna_actual,fila_actual))
                columna_actual+=direccion_columna
                fila_actual+=direccion_fila
            casillas.append((columna_actual,fila_actual))
        return casillas
        
class Dama(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Dama", color, posicion)

    def checkMovimiento(self, nueva_posicion):
        movimiento_como_torre = Torre(self.color, self.__posicion__).checkMovimiento(nueva_posicion)
        movimiento_como_alfil = Alfil(self.color, self.__posicion__).checkMovimiento(nueva_posicion)

        if movimiento_como_torre or movimiento_como_alfil:
            return movimiento_como_torre + movimiento_como_alfil
        else:
            return []

class Caballo(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Caballo", color, posicion)
    
    def checkMovimiento(self, nueva_posicion):#crea una tupla con los movimientos permitidos del caballo, si la nueva posicion esta en la tupla, devuelve true
        nueva_columna, nueva_fila =  nueva_posicion
        col_actual=self.columna
        fila_actual=self.fila
        movimiento_columna = abs(nueva_columna - col_actual)
        movimiento_fila = abs(nueva_fila - fila_actual)
        if (movimiento_columna == 2 and movimiento_fila == 1) or (movimiento_columna == 1 and movimiento_fila == 2):
            return True
        return False
class Rey(Piezas):
    def __init__(self, color, posicion):
        super().__init__("Rey", color, posicion)
    
    def checkMovimiento(self, nueva_posicion, ):#Lo mismo que con el caballo solo que separe las distintas combinaciones dependiendo del tipo de movimiento para mayor legibilidad
        nueva_columna, nueva_fila =  nueva_posicion
        col_actual=self.columna
        fila_actual=self.fila
        movimiento_columna = abs(nueva_columna - col_actual)
        movimiento_fila = abs(nueva_fila - fila_actual)

        if movimiento_columna <= 1 and movimiento_fila <= 1:
            return True
        return False
