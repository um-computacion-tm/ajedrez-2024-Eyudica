from piezas import Torre, Caballo, Alfil, Dama, Rey, Peon, BLANCO, NEGRO
from diccionarios import diccionarioSimbolos as simbolos

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
    
    def insertarEnTableroEnInicializacion(self,pieza):
        columna,fila=pieza.columna,pieza.fila
        self.__tablero__[columna][fila]=pieza.simbolo
    def checkearColisiones(self,pieza,nueva_posicion):
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

    def agregarEnTablero(self, pieza, nueva_posicion):
        columna_inicial, fila_inicial = (pieza.columna, pieza.fila)
        columna_final, fila_final = nueva_posicion
       # casilla_final_simbolo=self.__tablero__[columna_final][fila_final]
        
        if pieza.checkMovimiento(nueva_posicion):
            if self.checkearColisiones(pieza,nueva_posicion):
                self.__tablero__[columna_inicial][fila_inicial] = " "
                self.__tablero__[columna_final][fila_final] = pieza.simbolo
                pieza.establecerPosicion((columna_final, fila_final))
                return True
        else:
            pieza.establecerPosicion((columna_inicial, fila_inicial))
            return False

    def checkCamino(self, camino):
        for columna, fila in camino[0:-1]:
            if self.__tablero__[columna][fila] != " ":
                return False
        return True