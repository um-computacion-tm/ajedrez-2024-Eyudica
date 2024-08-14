from chess.piezas import Torre, Caballo, Alfil, Dama, Rey, Peon, BLANCO, NEGRO
from chess.tablero import Tablero
from chess.diccionarios import diccionarioSimbolos as simbolos

BLANCO='Blanco'
NEGRO='Negro'
CLEAR="\033[H\033[J"  # para limpiar la pantalla sin importar la libreria os
class Juego:
    def __init__(self,mostrar_tablero=True):
        self.tablero=Tablero()
        self.turno_actual=BLANCO
        self.turno_color_inicial=BLANCO
        self.turno_color_segundo=NEGRO
        self.juego_finalizado=False
        self.piezas=[]
        self.mostrar_tablero=mostrar_tablero
        self.contador_jugadas=0
        self.primera_jugada=True
        self.PonerPiezas()
        self.ganador=""
        #self.tablero.mostrar_tablero()
        if self.mostrar_tablero: #para que cuando ejecute los tests del juego no se muestre el tablero
            self.tablero.mostrar_tablero()
    def PonerPiezas(self): #Inicializa las piezas en sus respectivas posiciones y almacena las piezas en una lista para poder determinar el color ganador
        #Blancas
        
        self.piezas.extend([
            Peon(self.turno_color_inicial, "a2",self.tablero), Peon(self.turno_color_inicial, "b2",self.tablero),
            Peon(self.turno_color_inicial, "c2",self.tablero), Peon(self.turno_color_inicial, "d2",self.tablero),
            Peon(self.turno_color_inicial, "e2",self.tablero), Peon(self.turno_color_inicial, "f2",self.tablero),
            Peon(self.turno_color_inicial, "g2",self.tablero), Peon(self.turno_color_inicial, "h2",self.tablero),
            Torre(self.turno_color_inicial, "a1",self.tablero), Torre(self.turno_color_inicial, "h1",self.tablero),
            Caballo(self.turno_color_inicial, "b1",self.tablero), Caballo(self.turno_color_inicial, "g1",self.tablero),
            Alfil(self.turno_color_inicial, "c1",self.tablero), Alfil(self.turno_color_inicial, "f1",self.tablero),            
            Dama(self.turno_color_inicial, "e1",self.tablero), Rey(self.turno_color_inicial, "d1",self.tablero)
        ])

        # Negras
        self.piezas.extend([
            Peon(self.turno_color_segundo, "a7",self.tablero), Peon(self.turno_color_segundo, "b7",self.tablero),
            Peon(self.turno_color_segundo, "c7",self.tablero), Peon(self.turno_color_segundo, "d7",self.tablero),
            Peon(self.turno_color_segundo, "e7",self.tablero), Peon(self.turno_color_segundo, "f7",self.tablero),
            Peon(self.turno_color_segundo, "g7",self.tablero), Peon(self.turno_color_segundo, "h7",self.tablero),
            Torre(self.turno_color_segundo, "a8",self.tablero), Torre(self.turno_color_segundo, "h8",self.tablero),
            Caballo(self.turno_color_segundo, "b8",self.tablero), Caballo(self.turno_color_segundo, "g8",self.tablero),
            Alfil(self.turno_color_segundo, "c8",self.tablero), Alfil(self.turno_color_segundo, "f8",self.tablero),            
            Dama(self.turno_color_segundo, "e8",self.tablero), Rey(self.turno_color_segundo, "d8",self.tablero)
            
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

        self.juego_finalizado = True
        
    def moverPieza(self, posicion_inicial, posicion_final): #recibe posicion inicial y final, almacena en pieza la pieza que retorna determinarPieza
        pieza=self.determinarPieza(posicion_inicial)        #Y en base a la posicion inicial que le pasemos selecciona la pieza y la mueve a la posicion final y aumenta el contador para el cambio de turno
        if pieza:
            posicion_original = pieza.posicion
            if pieza.mover(posicion_final,self.tablero):
                self.contador_jugadas+=1
                return True
            else:
                pieza.establecerPosicion(posicion_original)
                return False
        return False
    def determinarPieza(self, posicion): #se le pasa como parametro de la posicion de la pieza que queremos conocer y retorna la pieza en el caso de que la posicion sea correcta
        for pieza in self.piezas:
            if pieza.posicion==posicion and pieza.color==self.turno_actual:
                print(pieza)
                return pieza
        return False
    def determinarGanador(self):#itera sobre todas las posiciones del tablero, y si no hay piezas de un color, se da como ganador el otro color
        piezas_blanco = False
        piezas_negro = False
    
        for x in range(8):
            for y in range(8):
                pieza = self.tablero.tablero[x][y]
                if pieza in simbolos[BLANCO].values():
                    piezas_blanco = True
                elif pieza in simbolos[NEGRO].values():
                    piezas_negro = True
                
                if piezas_blanco and piezas_negro:
                    return None #
        
        if not piezas_negro:
            #print("El jugador blanco ha ganado")
            self.ganador=BLANCO
            return True
        elif not piezas_blanco:
            #print("El jugador negro ha ganado")
            self.ganador=NEGRO
            return True
        return False
    def turnos(self): #Si contador_jugadas es par el turno es de blancas, sino de negras y llama a procesarJuego

        if self.contador_jugadas%2==0:
            self.turno_actual=BLANCO
        elif self.contador_jugadas%2==1:
            self.turno_actual=NEGRO
        print(f"Turno de {self.turno_actual}")  
       
        self.procesarJuego()

