from piezas import Torre, Caballo, Alfil, Dama, Rey, Peon, BLANCO, NEGRO
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
        
    def agregarEnTablero(self,pieza):
        if pieza.mover(nueva_posicion):
            columna_anterior = pieza.__columna__
            fila_anterior = pieza.__fila__
            pieza.__columna__,pieza.__fila__  = pieza.establecerPosicion(pieza.__posicion__)
            posicion_actual = self.__tablero__[pieza.__columna__][pieza.__fila__]
            if  posicion_actual not in simbolos[pieza.__color__].values(): 
                self.__tablero__[columna_anterior][fila_anterior] = " "
                self.__tablero__[pieza.__columna__][pieza.__fila__] = pieza.__simbolo__
                return True
            elif posicion_actual == pieza.__simbolo__: 
                #print(f"Ya tenes un {self.__tipo__}({simbolos[self.__color__][self.__tipo__]}) en {self.__posicion__}")
                pieza.__columna__, pieza.__fila__ = columna_anterior, fila_anterior
                return False
            else:
                pieza.__columna__, pieza.__fila__ = columna_anterior, fila_anterior
                return False
    def mover_pieza(self,pieza,nueva_posicion):
        posicion_original = pieza.__posicion__
        if self.checkMovimientoPeon(pieza,nueva_posicion):
            pieza.establecerPosicion(nueva_posicion)
            return True
        else:
            pieza.establecerPosicion(posicion_original)
            return False
   # def checkMovimientoPeon(self,pieza,nueva_posicion):
    def checkCaminoDiagonal(self, columna_inicial, fila_inicial, columna_final, fila_final):
        if pieza.checkMovimiento(nueva_posicion):
            direccion_columna = 1 if columna_inicial < columna_final else -1
            direccion_fila = 1 if fila_inicial < fila_final else -1
            if abs(columna_inicial - columna_final) == abs(fila_inicial - fila_final):
                columna_actual = columna_inicial + direccion_columna
                fila_actual = fila_inicial + direccion_fila
                while columna_actual != columna_final and fila_actual != fila_final:
                    if self.__tablero__[columna_actual][fila_actual] != " ":
                        return False 
                    columna_actual += direccion_columna
                    fila_actual += direccion_fila
            return True  


    def checkCaminoLineal(self, columna_inicial, fila_inicial, columna_final, fila_final):
        if pieza.checkMovimiento(nueva_posicion):           
            if columna_final==columna_inicial and fila_final!=fila_inicial: #avanzar horizontalmente 
                inicio_fila = min(fila_inicial, fila_final) + 1;
                fin_fila = max(fila_inicial, fila_final)
                for i in range(inicio_fila, fin_fila):
                    if tablero.__tablero__[self.__columna__][i]!=" ":
                        return False
                return True 
            if columna_final==fila_inicial and columna_final!=columna_inicial: #avanzar verticalmente
                incio_columna = min(columna_inicial, columna_final) + 1
                fin_columna = max(columna_inicial, columna_final)
                for i in range(incio_columna,fin_columna): #para las filas
                    if tablero.__tablero__[i][self.__fila__]!=" ":
                        return False
                return True
