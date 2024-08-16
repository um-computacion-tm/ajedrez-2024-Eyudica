from chess.diccionarios import diccionarioSimbolos as simbolos
from chess.diccionarios import diccionarioFilas
from chess.tablero import Tablero
#Global vars
BLANCO='Blanco'
NEGRO='Negro'
class Piezas():
    def __init__(self,tipo,color,posicion,tablero):
        self.__tipo__ = tipo
        self.__color__ = color
        self.__posicion__ = posicion
        self.__simbolo__ = self.obtenerSimbolos()
        self.__columna__, self.__fila__ = self.establecerPosicion(self.__posicion__)
        self.insertarEnTablero(tablero)
    #para poder acceder a los atributos de la pieza
    @property 
    def posicion(self):
        return self.__posicion__
    @property
    def color(self):
        return self.__color__
    @property
    def tipo(self):
        return self.__tipo__
    def obtenerSimbolos(self): #Entra en el diccionario de simbolos para obtener basandose en el color y el tipo de pieza
        return simbolos[self.__color__][self.__tipo__]
    
    def establecerPosicion(self, nueva_posicion): #Recibe como parametro las coordenadas de la nueva posicion de la pieza, convierte el primer valor de las coordenadas(columnas) a letras como el estandar usado en el ajedrez
        self.__posicion__ = nueva_posicion        #devuelve la posicion de la pieza
        columna=diccionarioFilas[self.__posicion__[0]] 
        fila=int(self.__posicion__[1])-1
        return columna,fila
        
    def insertarEnTablero(self, tablero): #Recibe como parametro el tablero, se fija que no haya ninguna pieza del mismo color en la posicion nueva,las coordenadas las da la funcion establecerPosicion
                                          #Si no hay ninguna pieza del mismo color, inserta el simbolo de la pieza en la posicion nueva, en el caso que haya una pieza del otro color, la "sobresribe"
                                          #Y la posicion anterior se convierte en un espacio vacio, si hay una pieza del mismo color en la posicion nueva, no hace nada y da un mensaje de aviso
        columna_anterior = self.__columna__
        fila_anterior = self.__fila__
        self.__columna__,self.__fila__  = self.establecerPosicion(self.__posicion__) 
        posicion_actual = tablero.__tablero__[self.__columna__][self.__fila__]
        if  posicion_actual not in simbolos[self.__color__].values(): 
            tablero.__tablero__[columna_anterior][fila_anterior] = " "
            tablero.__tablero__[self.__columna__][self.__fila__] = self.__simbolo__
            return True
        elif posicion_actual == self.__simbolo__: 
            #print(f"Ya tenes un {self.__tipo__}({simbolos[self.__color__][self.__tipo__]}) en {self.__posicion__}")
            self.__columna__, self.__fila__ = columna_anterior, fila_anterior
            return False
        else:
            self.__columna__, self.__fila__ = columna_anterior, fila_anterior
            return False
    def __str__(self):
        return f'La pieza es {self.__tipo__} con color {self.__color__} en la posicion {self.__posicion__} y el simbolo es {self.__simbolo__}'

    def mover(self, nueva_posicion, tablero): #Metodo para mover la pieza en el tablero, si la posicion es valida y no hay ninguna pieza del mismo color en la nueva posicion, se ejectua.Sino la pieza vuelve a la posicion anterior
        posicion_original = self.__posicion__
        if self.checkMovimiento(nueva_posicion, tablero):
            self.establecerPosicion(nueva_posicion)
            if self.insertarEnTablero(tablero):
                return True
            else:
                self.establecerPosicion(posicion_original)
                return False
        return False

        

    def checkMovimiento(self,nueva_posicion,tablero): #Si no esta definido el metodo en las clases, al ejecutarlo lanza una excepcion, forza el polimorfismo
        raise NotImplementedError("El metodo checkMovimiento  no esta implementado en la clase")

class Peon(Piezas):
    def __init__(self, color, posicion,tablero):
        super().__init__("Peon", color, posicion,tablero)
        self.__movido__=False #Para el doble avance inicial
    def checkMovimiento(self,nueva_posicion,tablero): #determina los distintos movimientos permitidos del peon con condicionales
        nueva_columna, nueva_fila =  self.establecerPosicion(nueva_posicion) 
        direccion=1 if self.__color__==BLANCO else -1
        if nueva_columna==self.__columna__ and nueva_fila==self.__fila__+direccion and tablero.__tablero__[nueva_columna][nueva_fila]==" ": #avanzar linealmente
            self.__movido__=True
            return True
        if (nueva_columna==self.__columna__+1 or nueva_columna==self.__columna__-1) \
            and nueva_fila==self.__fila__+direccion and tablero.__tablero__[nueva_columna][nueva_fila]!=" ": #comer en diagonal   
            self.__movido__=True
            return True
        fila_doble_avance=self.__fila__+(2*direccion)
        if not self.__movido__ and nueva_columna==self.__columna__ and nueva_fila==fila_doble_avance and tablero.__tablero__[nueva_columna][nueva_fila]==" ":#doble avance
            self.__movido__=True
            return True
        return False


 
class Torre(Piezas):
    def __init__(self, color, posicion,tablero):
        super().__init__("Torre", color, posicion,tablero)
    def checkMovimiento(self,nueva_posicion,tablero): #comprueba los distintos movimientos permitidos de la torre basado en la posicion a mover y la posicion actual
        #Tanto en el movimiento horizontal como en el movimiento vertical, agarra las casillas que hay entre medio de la posicion actual y la final, e itera sobre estas.
        # Si en todas hay espacios vacios, quiere decir que no hay ninguna pieza bloqueando el camino.En el caso contrario, no permite el movimiento
        nueva_columna, nueva_fila =  self.establecerPosicion(nueva_posicion)
        inicio_fila = min(self.__fila__, nueva_fila) + 1; #para calcular  a partir de la proxima casilla
        fin_fila = max(self.__fila__, nueva_fila)
        movimiento_valido=False
        # if nueva_columna!=self.__columna__ and nueva_fila!=self.__fila__: #bloquear el movimiento diagonal
        #     return False
        if nueva_columna==self.__columna__ and nueva_fila!=self.__fila__: #avanzar horizontalmente 
            movimiento_valido=True
            for i in range(inicio_fila, fin_fila):
                if tablero.__tablero__[self.__columna__][i]!=" ":
                    movimiento_valido=False
                    break
        if nueva_fila==self.__fila__ and nueva_columna!=self.__columna__: #avanzar verticalmente
            movimiento_valido=True
            incio_columna = min(self.__columna__, nueva_columna) + 1
            fin_columna = max(self.__columna__, nueva_columna)
            for i in range(incio_columna,fin_columna): #para las filas
                if tablero.__tablero__[i][self.__fila__]!=" ":
                    movimiento_valido=False
                    break
        return movimiento_valido

class Alfil(Piezas):
    def __init__(self, color, posicion,tablero):
        super().__init__("Alfil", color, posicion,tablero)
    def checkMovimiento(self,nueva_posicion,tablero): #comprueba que el movimiento sea diagonal
        nueva_columna, nueva_fila =  self.establecerPosicion(nueva_posicion)
        diferencia_columnas=abs(self.__columna__-nueva_columna) 
        diferencia_filas=abs(self.__fila__-nueva_fila)
        if diferencia_columnas==diferencia_filas:# al ser un movimiento diagonal, la diferencia de columnas y filas debe ser igual
            if self.calcularPosicionDiagonal(nueva_posicion,tablero):
                return True
            return False
        else:
            #print("El movimiento no es diagonal")
            return False
      
    def calcularPosicionDiagonal(self,nueva_posicion,tablero): #comprueba si esta disponible el movimiento, mueve la pieza y llamo a insertarentablero
        nueva_columna, nueva_fila = self.establecerPosicion(nueva_posicion)
        direccion_columnna=1 if self.__columna__ < nueva_columna else -1
        direccion_fila=1 if self.__fila__ < nueva_fila else -1

        columna_actual=self.__columna__ + direccion_columnna
        fila_actual=self.__fila__ + direccion_fila
        while (columna_actual!=nueva_columna) and (fila_actual!=nueva_fila):
            if tablero.__tablero__[columna_actual][fila_actual]!=" ": #va iterando por cada posicion entre la actual y la final por si hay alguna pieza bloqueando el camino del alfil
                #print("No es posible mover la pieza, hay una pieza bloqueando el camino")
                return False
            columna_actual+=direccion_columnna
            fila_actual+=direccion_fila

        return True
    
class Dama(Piezas):
    def __init__(self, color, posicion,tablero):
        super().__init__("Dama", color, posicion,tablero)

    def checkMovimiento(self, nueva_posicion, tablero): #crea las instancias de torre y alfil, con la posicion y color de la dama. Esto esta para que la dama pueda replicar sus movimientos
        
        self.Torre_moves = Torre(self.__color__, self.__posicion__,tablero)
        self.Alfil_moves = Alfil(self.__color__, self.__posicion__,tablero)
        return self.Torre_moves.checkMovimiento(nueva_posicion, tablero) or self.Alfil_moves.checkMovimiento(nueva_posicion, tablero)
        #Si agluno de los movimientos es True, se cumple la condicion del metodo mover de piezas, entonces usa el metodo de la pieza respectiva pero con los atributos de la dama
class Caballo(Piezas):
    def __init__(self, color, posicion,tablero):
        super().__init__("Caballo", color, posicion,tablero)
    
    def checkMovimiento(self, nueva_posicion, tablero):#crea una tupla con los movimientos permitidos del caballo, si la nueva posicion esta en la tupla, devuelve true
        nueva_columna, nueva_fila =  self.establecerPosicion(nueva_posicion)
        col_actual=self.__columna__
        fila_actual=self.__fila__
        posibles_movimientos=((col_actual-2,fila_actual-1),(col_actual-2,fila_actual+1),(col_actual+1,fila_actual+2),(col_actual-1,fila_actual+2),(col_actual+2,\
        fila_actual+1),(col_actual+2,fila_actual-1),(col_actual+1,fila_actual-2),(col_actual-1,fila_actual-2)) #posibles movimientos a partir de la posicio actual
        if (nueva_columna,nueva_fila) in posibles_movimientos:
            return True
        return False
   
class Rey(Piezas):
    def __init__(self, color, posicion,tablero):
        super().__init__("Rey", color, posicion,tablero)
    
    def checkMovimiento(self, nueva_posicion, tablero):#Lo mismo que con el caballo solo que separe las distintas combinaciones dependiendo del tipo de movimiento para mayor legibilidad
        nueva_columna, nueva_fila =  self.establecerPosicion(nueva_posicion)
        posibles_movimientos_lineales=((self.__columna__-1,self.__fila__),(self.__columna__+1,self.__fila__),(self.__columna__,self.__fila__+1),(self.__columna__,self.__fila__-1))   
        posibles_movimientos_diagonales=((self.__columna__-1,self.__fila__+1),(self.__columna__+1,self.__fila__-1),(self.__columna__+1,self.__fila__+1),(self.__columna__-1,self.__fila__-1))
        if (nueva_columna,nueva_fila)  in (posibles_movimientos_lineales + posibles_movimientos_diagonales):
            return True
        return False
