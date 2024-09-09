from chess.piezas.piezas import *
from chess.piezas.peon import Peon
from chess.piezas.torre import Torre
from chess.piezas.alfil import Alfil
from chess.piezas.dama import Dama
from chess.piezas.rey import Rey
from chess.piezas.caballo import Caballo
from chess.diccionarios import diccionarioSimbolos as simbolos

BLANCO='Blanco'
NEGRO='Negro'
class Tablero:
    def __init__(self):
        self.__tablero__=[
                #El tablero va a ser una matriz de 8x8
                [" "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "], 
                [" "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "], 
                [" "," "," "," "," "," "," "," "], 
                [" "," "," "," "," "," "," "," "],
            ]
        self.letras="abcdefgh"
    def mostrar_tablero(self): #Printea la matriz para que vea como un tablero
        print("  +" + "---+" * 8)
        
        for i in range(len(self.letras)):
            print(f"{self.letras[i]} |", end=" ")
            print(" | ".join(self.__tablero__[i]), end=" |\n")
            print("  +" + "---+" * 8)
        print("  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
    
    def insertarEnTableroEnInicializacion(self,pieza):#recibe la pieza como parametro y la inserta en el tablero
        columna,fila=pieza.columna,pieza.fila
        self.__tablero__[columna][fila]=pieza.simbolo
    def checkearColisiones(self,pieza,nueva_posicion):#se fija que no haya piezas en la posicion final a mover, en caso de que haya, se fija en el color, si es del mismo color devuelve false, sino true
        columna_final,fila_final=nueva_posicion
        if self.__tablero__[columna_final][fila_final]==" ":
            return True
        if self.__tablero__[columna_final][fila_final]!=" ":
            for color, simbolos_color in simbolos.items():
                if self.__tablero__[columna_final][fila_final] in simbolos_color.values():
                    if color==pieza.color:
                        return False
                    else:
                        return True

    def agregarEnTablero(self, pieza, nueva_posicion): #mueve la pieza en el tablero, se fija que se pueda mover y elimina la pieza de la posicion vieja y la coloca en la nueva.Sino la pieza vuelve a la posicion anterior y devuelve false
        columna_inicial, fila_inicial = (pieza.columna, pieza.fila)
        columna_final, fila_final = nueva_posicion
       # casilla_final_simbolo=self.__tablero__[columna_final][fila_final]
        
        if self.checkearColisiones(pieza,nueva_posicion):
       #     if self.checkearColisiones(pieza,nueva_posicion):
                self.__tablero__[columna_inicial][fila_inicial] = " "
                self.__tablero__[columna_final][fila_final] = pieza.simbolo
                pieza.establecerPosicion((columna_final, fila_final))
                return True
        else:
            pieza.establecerPosicion((columna_inicial, fila_inicial))
            return False

    def checkCamino(self, pieza, camino): #metodo para ver si hay piezas interrumpiendo el movimiento de la pieza, en el caso de las piezas que no necesiten esta validacion, devuelve true directamente
        camino_libre=False
        if isinstance(pieza, Peon):
            if len(camino) == 1:
                columna, fila = camino[0]
                avance_lineal = (columna == pieza.columna)
                if avance_lineal:
                    camino_libre = (self.__tablero__[columna][fila]==" ")
                else:
                    camino_libre = (self.__tablero__[columna][fila] !=" ")
            elif len(camino) == 2:#si el movimiento es recto y esta libre    #para la diagonal
                     
                camino_libre = all(self.__tablero__[columna][fila] == " " for columna, fila in camino)
            
        elif isinstance(pieza, (Alfil,Dama,Torre)):
            camino_libre = all(self.__tablero__[columna][fila] == " " for columna, fila in camino[:-1])
        else:
            return True
        return camino_libre