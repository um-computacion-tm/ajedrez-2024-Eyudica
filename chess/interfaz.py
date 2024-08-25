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
        
        if self.checkearColisiones(pieza,nueva_posicion):
       #     if self.checkearColisiones(pieza,nueva_posicion):
                self.__tablero__[columna_inicial][fila_inicial] = " "
                self.__tablero__[columna_final][fila_final] = pieza.simbolo
                pieza.establecerPosicion((columna_final, fila_final))
                return True
        else:
            pieza.establecerPosicion((columna_inicial, fila_inicial))
            return False

    def checkCamino(self, pieza, camino):
        if isinstance(pieza, Peon):
            if len(camino) == 1:
                columna, fila = camino[0]
                avance_lineal = (columna == pieza.columna)
                return (self.__tablero__[columna][fila]==" ") if avance_lineal else (self.__tablero__[columna][fila] !=" ")
            elif len(camino) == 2:#si el movimiento es recto y esta libre    #para la diagonal
                     
                return all(self.__tablero__[columna][fila] == " " for columna, fila in camino)
            return False
        elif isinstance(pieza, (Alfil,Dama,Torre)):
            return all(self.__tablero__[columna][fila] == " " for columna, fila in camino[:-1])
        else:
            return True


    def determinarGanador(self):#itera sobre todas las posiciones del tablero, y si no hay piezas de un color, se da como ganador el otro color
        piezas_blanco = False
        piezas_negro = False
    
        for x in range(8):
            for y in range(8):
                pieza = self.__tablero__[x][y]
                if pieza in simbolos[BLANCO].values():
                    piezas_blanco = True
                elif pieza in simbolos[NEGRO].values():
                    piezas_negro = True
        if not piezas_negro:
            return NEGRO
        elif not piezas_blanco:
            return NEGRO
        return None