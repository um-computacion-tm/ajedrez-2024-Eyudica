import unittest
from chess.tablero import Tablero
from io import StringIO
from unittest.mock import patch
import unittest
from chess.piezas.piezas import *
from chess.piezas.peon import Peon
from chess.piezas.torre import Torre
from chess.piezas.alfil import Alfil
from chess.piezas.dama import Dama
from chess.piezas.rey import Rey
from chess.piezas.caballo import Caballo
from chess.tablero import Tablero
from chess.diccionarios import diccionarioSimbolos as simbolos
class TestTablero(unittest.TestCase):
    def setUp(self):

        self.tablero = Tablero()
        self.peon_blanco = Peon('Blanco',(1, 1))
        self.torre_negra = Torre('Negro', (0, 0))
        self.alfil_blanco = Alfil('Blanco', (2, 2))
        self.dama_negra = Dama('Negro', (3, 3))
        self.rey_blanco = Rey('Blanco',(4, 4))
        self.caballo_negro = Caballo('Negro', (5, 5))
    #testea que el tablero inicia correctamente
    def inicio_tablero(self):
        tablero=[
                
                [" "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "], 
                [" "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "], 
                [" "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "],
            ]
        self.assertEqual(self.tablero,tablero)
    def test_espacios(self):#testea que el tablero  tenga espacios en blanco
        self.assertEqual(self.tablero.__tablero__[0][0]," ")
        self.assertEqual(self.tablero.__tablero__[7][7]," ")

        self.assertNotEqual(self.tablero.__tablero__[4][5],"♟")
    @patch('sys.stdout', new_callable=StringIO)#teesta que una parte del tablero se muestra correctamente
    def test_mostrar_tablero(self, mock_stdout): 
        self.tablero.mostrar_tablero()
        output = mock_stdout.getvalue()
        
        self.assertIn("+---+---+---+---+---+---+---+---+", output)
    def test_insertar_en_tablero(self):#testea que se pueda insertar una pieza en el tablero
        self.tablero.insertarEnTableroEnInicializacion(self.peon_blanco)
        self.assertEqual(self.tablero.__tablero__[1][1], self.peon_blanco.simbolo)

    def test_agregar_en_tablero(self):#testea que hayan piezas o no en las posiciones pedidas
        self.tablero.insertarEnTableroEnInicializacion(self.peon_blanco)
        nueva_posicion = (2, 2)
        self.tablero.agregarEnTablero(self.peon_blanco, nueva_posicion)
        self.assertEqual(self.tablero.__tablero__[2][2], self.peon_blanco.simbolo)
        self.assertEqual(self.tablero.__tablero__[1][1], " ")

    def test_checkear_colisiones_vacio(self):#testea que no haya colisiones si no hay piezas en la posicion
        self.assertTrue(self.tablero.checkearColisiones(self.peon_blanco, (2, 2)))
    
    def test_checkear_colisiones_con_pieza(self):#testea que haya colisiones si hay una pieza en la posicion
        self.tablero.insertarEnTableroEnInicializacion(self.torre_negra)
        self.assertFalse(self.tablero.checkearColisiones(self.dama_negra, (0, 0)))
        self.assertTrue(self.tablero.checkearColisiones(self.dama_negra, (0, 1)))

    def test_check_camino(self):#testea que la pieza se pueda mover en el camino dado
        self.tablero.insertarEnTableroEnInicializacion(self.peon_blanco)
        camino = [(1, 2)]
        self.assertTrue(self.tablero.checkCamino(self.peon_blanco, camino))

        camino_dos = [(1, 2), (2, 2)]
        self.assertTrue(self.tablero.checkCamino(self.peon_blanco, camino_dos))

    # def test_check_camino_con_obstaculos(self):
    #     self.tablero.insertarEnTableroEnInicializacion(self.torre_negra)
    #     camino = [(2, 3), (3, 3),(3,4)]
    #     self.assertTrue(self.tablero.checkCamino(self.torre_negra, camino))
if __name__ == '__main__':
    unittest.main()