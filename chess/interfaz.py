from piezas import Torre, Caballo, Alfil, Dama, Rey, Peon, BLANCO, NEGRO
from tablero import Tablero
from diccionarios import diccionarioSimbolos as simbolos
from diccionarios import diccionarioFilas as posiciones

BLANCO='Blanco'
NEGRO='Negro'
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
    def agregarPiezasEnTablero(self):
        for pieza in self.__piezas__:
            self.__tablero__.insertarEnTableroEnInicializacion(pieza)
   
    def determinarPieza(self, posicion): #se le pasa como parametro de la posicion de la pieza que queremos conocer y retorna la pieza en el caso de que la posicion sea correcta
        columna,fila=posicion
        for pieza in self.__piezas__:
            if (pieza.columna==columna and pieza.fila==fila) and pieza.color==self.__turno_actual__:
                return pieza
        return False
    def determinarPiezaDestino(self,posicion):
        columna,fila=posicion
        for pieza in self.__piezas__:
            if (pieza.columna==columna and pieza.fila==fila) and pieza.color!=self.__turno_actual__:
                return pieza
        return False
    def moverPieza(self, posicion_inicial, nueva_posicion):
        pieza = self.determinarPieza(posicion_inicial)
        if not pieza:
            return False
        columna_inicial, fila_inicial = posicion_inicial
        columna_final, fila_final = nueva_posicion
        pieza_destino=self.determinarPiezaDestino(nueva_posicion)
        camino = pieza.checkMovimiento(nueva_posicion)
        if camino and self.__tablero__.checkCamino(pieza, camino) and self.__tablero__.agregarEnTablero(pieza, nueva_posicion):
            # Mover la pieza en el tablero
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
    def ProcesarInput(self):
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

    def excepcion(self, coordenadas):
        try:
            coord = coordenadas.replace(" ", "").lower()
            if len(coord) != 4:
                raise ValueError("Se esperan 2 coordenadas(columna y fila)")
            letras, numeros = 'abcdefgh', '12345678'
            if (coord[0] not in letras or coord[2] not in letras or coord[1] not in numeros or coord[3] not in numeros):
                raise ValueError("Formato incorrecto")
            return True
        except ValueError as e:
            print(f"Error: {e}")
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
                
        if not piezas_negro:
            return BLANCO   
        elif not piezas_blanco:
            return NEGRO
        return None
    def turnos(self): #Si contador_jugadas es par el turno es de blancas, sino de negras y llama a procesarJuego
        if self.determinarGanador() is not None:
            self.__ganador__=self.determinarGanador()
            #print(f"El jugador {self.__ganador__} ha ganado")
            self.__juego_finalizado__ = True
            
        if self.__contador_jugadas__%2==0:
            self.__turno_actual__=BLANCO
        elif self.__contador_jugadas__%2==1:
            self.__turno_actual__=NEGRO
        print(f"Turno de {self.__turno_actual__}") 

