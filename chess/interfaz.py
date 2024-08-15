from chess.piezas import Torre, Caballo, Alfil, Dama, Rey, Peon, BLANCO, NEGRO
from chess.tablero import Tablero
from chess.diccionarios import diccionarioSimbolos as simbolos

BLANCO='Blanco'
NEGRO='Negro'
CLEAR="\033[H\033[J"  # para limpiar la pantalla sin importar la libreria os
class Juego:
    def __init__(self,mostrar_tablero=True):
        self.__tablero__=Tablero()
        self.__turno_actual__=BLANCO
        self.__turno_color_inicial__=BLANCO
        self.__turno_color_segundo__=NEGRO
        self.__juego_finalizado__=False
        self.__piezas__=[]
        self.__mostrar_tablero__=mostrar_tablero
        self.__contador_jugadas__=0
        self.__primera_jugada__=True
        self.PonerPiezas()
        self.__ganador__=""
        #self.tablero.mostrar_tablero()
        if self.__mostrar_tablero__: #para que cuando ejecute los tests del juego no se muestre el tablero
            self.__tablero__.mostrar_tablero()
    def PonerPiezas(self): #inicializa las piezas en sus posiciones y alamacena las piezas en una lista para poder determinar el color ganador mas adelante
        #blancas
        
        self.__piezas__.extend([
            Peon(self.__turno_color_inicial__, "a2",self.__tablero__), Peon(self.__turno_color_inicial__, "b2",self.__tablero__),
            Peon(self.__turno_color_inicial__, "c2",self.__tablero__), Peon(self.__turno_color_inicial__ ,"d2",self.__tablero__),
            Peon(self.__turno_color_inicial__, "e2",self.__tablero__), Peon(self.__turno_color_inicial__, "f2",self.__tablero__),
            Peon(self.__turno_color_inicial__, "g2",self.__tablero__), Peon(self.__turno_color_inicial__, "h2",self.__tablero__),
            Torre(self.__turno_color_inicial__, "a1",self.__tablero__), Torre(self.__turno_color_inicial__, "h1",self.__tablero__),
            Caballo(self.__turno_color_inicial__, "b1",self.__tablero__), Caballo(self.__turno_color_inicial__, "g1",self.__tablero__),
            Alfil(self.__turno_color_inicial__, "c1",self.__tablero__), Alfil(self.__turno_color_inicial__, "f1",self.__tablero__),            
            Dama(self.__turno_color_inicial__, "e1",self.__tablero__), Rey(self.__turno_color_inicial__, "d1",self.__tablero__)
        ])

        #negras
        self.__piezas__.extend([
            Peon(self.__turno_color_segundo__, "a7",self.__tablero__), Peon(self.__turno_color_segundo__, "b7",self.__tablero__),
            Peon(self.__turno_color_segundo__, "c7",self.__tablero__), Peon(self.__turno_color_segundo__, "d7",self.__tablero__),
            Peon(self.__turno_color_segundo__, "e7",self.__tablero__), Peon(self.__turno_color_segundo__, "f7",self.__tablero__),
            Peon(self.__turno_color_segundo__, "g7",self.__tablero__), Peon(self.__turno_color_segundo__, "h7",self.__tablero__),
            Torre(self.__turno_color_segundo__, "a8",self.__tablero__), Torre(self.__turno_color_segundo__, "h8",self.__tablero__),
            Caballo(self.__turno_color_segundo__, "b8",self.__tablero__), Caballo(self.__turno_color_segundo__, "g8",self.__tablero__),
            Alfil(self.__turno_color_segundo__, "c8",self.__tablero__), Alfil(self.__turno_color_segundo__, "f8",self.__tablero__),            
            Dama(self.__turno_color_segundo__, "e8",self.__tablero__), Rey(self.__turno_color_segundo__, "d8",self.__tablero__)
            
        ])
    def procesarJuego(self): #sirve para la entrada del usuario y valida con excepciones que las coordenadas sean validas, en el caso que sean validas mueve la pieza, sino pide devuelta la entrada de datos
                             #si determinarGanador devuelve true, juego_finalizado es true y el ciclo de juego en el archivo main termina
        if not self.determinarGanador():
            coordenadas = None
            while not coordenadas:
                try:
                    input_pos_pieza = input("Movimiento: ")
                    coordenadas = input_pos_pieza.split(" ")
                    if len(coordenadas) != 2:
                        raise ValueError("Debes ingresar exactamente 2 coordenadas.")

                    for coord in coordenadas:
                        if len(coord) != 2 or coord[0] not in "abcdefgh" or coord[1] not in "12345678":
                            raise ValueError(f"Coordenada invalida")
                    
                except ValueError as e:
                    print(e)
                    coordenadas = None 

            posicion_inicial = coordenadas[0]
            posicion_final = coordenadas[1]
            
            if self.moverPieza(posicion_inicial, posicion_final):
                return True
            return False

        self.__juego_finalizado__ = True
        
    def moverPieza(self, posicion_inicial, posicion_final): #recibe posicion inicial y final, almacena en pieza la pieza que retorna determinarPieza
        pieza=self.determinarPieza(posicion_inicial)        #Y en base a la posicion inicial que le pasemos selecciona la pieza y la mueve a la posicion final y aumenta el contador para el cambio de turno
        if pieza:
            posicion_original = pieza.posicion
            if pieza.mover(posicion_final,self.__tablero__):
                self.__contador_jugadas__+=1
                return True
            else:
                pieza.establecerPosicion(posicion_original)
                return False
        return False
    def determinarPieza(self, posicion): #se le pasa como parametro de la posicion de la pieza que queremos conocer y retorna la pieza en el caso de que la posicion sea correcta
        for pieza in self.__piezas__:
            if pieza.posicion==posicion and pieza.color==self.__turno_actual__:
                print(pieza)
                return pieza
        return False
    def determinarGanador(self):#itera sobre todas las posiciones del tablero, y si no hay piezas de un color, se da como ganador el otro color
        piezas_blanco = False
        piezas_negro = False
    
        for x in range(8):
            for y in range(8):
                pieza = self.__tablero__.__tablero__[x][y]
                if pieza in simbolos[BLANCO].values():
                    piezas_blanco = True
                elif pieza in simbolos[NEGRO].values():
                    piezas_negro = True
                
                if piezas_blanco and piezas_negro:
                    return None #
        
        if not piezas_negro:
            #print("El jugador blanco ha ganado")
            self.__ganador__=BLANCO
            return True
        elif not piezas_blanco:
            #print("El jugador negro ha ganado")
            self.__ganador__=NEGRO
            return True
        return False
    def turnos(self): #Si contador_jugadas es par el turno es de blancas, sino de negras y llama a procesarJuego

        if self.__contador_jugadas__%2==0:
            self.__turno_actual__=BLANCO
        elif self.__contador_jugadas__%2==1:
            self.__turno_actual__=NEGRO
        print(f"Turno de {self.__turno_actual__}")  
       
        self.procesarJuego()

