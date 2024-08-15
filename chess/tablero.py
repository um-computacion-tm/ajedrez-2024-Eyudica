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
        


