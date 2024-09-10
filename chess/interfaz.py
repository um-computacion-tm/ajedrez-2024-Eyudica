from chess.piezas.piezas import *
from chess.piezas.peon import Peon
from chess.piezas.torre import Torre
from chess.piezas.alfil import Alfil
from chess.piezas.dama import Dama
from chess.piezas.rey import Rey
from chess.piezas.caballo import Caballo
from chess.tablero import Tablero
from chess.diccionarios import diccionarioSimbolos as simbolos
from chess.diccionarios import diccionarioFilas as posiciones

BLANCO='Blanco'
NEGRO='Negro'
#Clase que establece el flujo del juego
class Juego:
    def __init__(self,mostrar_tablero=True):
        #self.__tablero__=Tablero()
        self.__tablero__=Tablero()
        self.__turno_actual__=BLANCO
        self.__turno_color_inicial__=BLANCO
        self.__turno_color_segundo__=NEGRO
        self.__juego_finalizado__=False
        self.__piezas__=[]
        self.__contador_jugadas__=0
        self.__primera_jugada__=True
        self.__ganador__=None
        
      
    def inicializarPiezas(self): #inicializa las piezas en sus posiciones y alamacena las piezas en una lista para poder determinar el color ganador mas adelante
        #Blancas
        
        self.__piezas__.extend([
            Peon(self.__turno_color_inicial__, (0,1)), Peon(self.__turno_color_inicial__, (1,1)),
            Peon(self.__turno_color_inicial__, (2,1)), Peon(self.__turno_color_inicial__, (3,1)),
            Peon(self.__turno_color_inicial__, (4,1)), Peon(self.__turno_color_inicial__, (5,1)),
            Peon(self.__turno_color_inicial__, (6,1)), Peon(self.__turno_color_inicial__, (7,1)),
            Torre(self.__turno_color_inicial__, (0,0)), Torre(self.__turno_color_inicial__, (7,0)),
            Caballo(self.__turno_color_inicial__, (1,0)), Caballo(self.__turno_color_inicial__, (6,0)),
            Alfil(self.__turno_color_inicial__, (2,0)), Alfil(self.__turno_color_inicial__, (5,0)),            
            Dama(self.__turno_color_inicial__, (3,0)), Rey(self.__turno_color_inicial__, (4,0))
       ])
        #negras
        self.__piezas__.extend([
            Peon(self.__turno_color_segundo__, (0,6)), Peon(self.__turno_color_segundo__, (1,6)),
            Peon(self.__turno_color_segundo__, (2,6)), Peon(self.__turno_color_segundo__, (3,6)),
            Peon(self.__turno_color_segundo__, (4,6)), Peon(self.__turno_color_segundo__, (5,6)), 
            Peon(self.__turno_color_segundo__, (6,6)), Peon(self.__turno_color_segundo__, (7,6)),
            Torre(self.__turno_color_segundo__, (0,7)), Torre(self.__turno_color_segundo__, (7,7)),
            Caballo(self.__turno_color_segundo__, (1,7)), Caballo(self.__turno_color_segundo__, (6,7)),
            Alfil(self.__turno_color_segundo__, (2,7)), Alfil(self.__turno_color_segundo__, (5,7)),            
            Dama(self.__turno_color_segundo__, (3,7)), Rey(self.__turno_color_segundo__, (4,7))
            
        ])
    def agregarPiezasEnTablero(self): #inserta las piezas de la lista __piezas__en el tablero
        for pieza in self.__piezas__:
            self.__tablero__.insertarEnTableroEnInicializacion(pieza)
   
    def determinarPieza(self, posicion): #se le pasa como parametro de la posicion de la pieza que queremos conocer y retorna la pieza en el caso de que la posicion sea correcta, sino devuelve false
        columna,fila=posicion
        for pieza in self.__piezas__:
            if (pieza.columna==columna and pieza.fila==fila) and pieza.color==self.__turno_actual__:
                return pieza
        return False
    def determinarPiezaDestino(self,posicion): #devuelve las pieza en la posicion destino, en el caso de que la pieza sea del rival, la devuelve
        columna,fila=posicion
        for pieza in self.__piezas__:
            if (pieza.columna==columna and pieza.fila==fila) and pieza.color!=self.__turno_actual__:
                return pieza
        return False
    def moverPieza(self, posicion_inicial, nueva_posicion): #metodo para mover las piezas, se le pasa como parametro la posicion inicial y la nueva posicion, si la pieza puede moverse, se devuelve true y aumenta el contador de jugadas para que el metodo turnos determine a que color le toca mover, sino false
        pieza = self.determinarPieza(posicion_inicial)      #en el caso del peon, modifica movido para que no se pueda mover dos posiciones en los proxmimos movimientos.Si la pieza no se puede mover, convierte la posicion de la pieza en la posicion anterior y devuelve false
        if not pieza:
            return False
        columna_inicial, fila_inicial = posicion_inicial
        columna_final, fila_final = nueva_posicion
        pieza_destino=self.determinarPiezaDestino(nueva_posicion)
        camino = pieza.checkMovimiento(nueva_posicion)
        if camino and self.__tablero__.checkCamino(pieza, camino) and self.__tablero__.agregarEnTablero(pieza, nueva_posicion):
            self.__tablero__.agregarEnTablero(pieza, nueva_posicion)
            if pieza_destino:
                self.__piezas__.remove(pieza_destino)

            self.__contador_jugadas__+=1
            if isinstance(pieza, Peon):
                pieza.__movido__=True
            return True
        else:
            pieza.establecerPosicion((columna_inicial, fila_inicial))
            return False
    def ProcesarInput(self):# metodo para ingreso de coordenas, espera las coordenadas iniciales y finales, si son correctas, se devuelve una tupla, sino false, para que no se pueda mover la pieza
        coordenadas = None
        while coordenadas is None:
            coordenadas = input("Ingresar movimiento: ").replace(" ","").strip()
            if coordenadas=="exit":
                self.__juego_finalizado__=True
                return False
            
            if self.excepcion(coordenadas):
                primerLetra = posiciones[coordenadas[0].lower()]
                primerNumero = int(coordenadas[1]) - 1
                segundaLetra = posiciones[coordenadas[2].lower()]
                segundoNumero = int(coordenadas[3]) - 1
                return (primerLetra, primerNumero), (segundaLetra, segundoNumero)
            coordenadas = None

    def excepcion(self, coordenadas):#metodo para comprobar si las coordenadas son correctas, si no, se devuelve false
        try:
            coord = coordenadas.replace(" ", "").lower()
            if len(coord) != 4:
                raise ValueError("Se esperan 2 coordenadas(columna y fila)")
            letras, numeros = 'abcdefgh', '12345678'
            if (coord[0] not in letras or coord[2] not in letras or coord[1] not in numeros or coord[3] not in numeros):
                raise ValueError("Formato incorrecto")
            if (coord[0] == coord[2] and coord[1] == coord[3]):
                raise ValueError("No se puede mover a la misma posicion")
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def determinarGanador(self):#itera sobre todas la lista piezas y si no hay un rey de un color, retorna el otro color
        rey_blanco = False
        rey_negro = False
    
        for rey in self.__piezas__:
            if isinstance(rey, Rey):
                if rey.color == BLANCO:
                    rey_blanco = True
                elif rey.color == NEGRO:
                    rey_negro = True
        if not rey_negro:
            return BLANCO   
        elif not rey_blanco:
            return NEGRO
        return None
    def turnos(self): #Si contador_jugadas es par el turno es de blancas, sino de negras.En el caso de que determinar ganador devuelva un color, el juego termina
        if self.determinarGanador() is not None:
            self.__ganador__=self.determinarGanador()
            #print(f"El jugador {self.__ganador__} ha ganado")
            self.__juego_finalizado__ = True
            return True
        if self.__contador_jugadas__%2==0:
            self.__turno_actual__=BLANCO
        elif self.__contador_jugadas__%2==1:
            self.__turno_actual__=NEGRO
        print(f"Turno de {self.__turno_actual__}") 

