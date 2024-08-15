import unittest
from chess.tablero import Tablero
from io import StringIO
from unittest.mock import patch
class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()
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
        self.assertEqual(self.tablero.tablero,tablero)
    #testea que el tablero inicialmente tiene espacios vacios
    def test_espacios(self):
        self.assertEqual(self.tablero.tablero[0][0]," ")
        self.assertEqual(self.tablero.tablero[7][7]," ")

        self.assertNotEqual(self.tablero.tablero[4][5],"♟")
    #para capturar la salida de la impresión del tablero y verificar que la estructura se muestra correctamente
    @patch('sys.stdout', new_callable=StringIO)
    def test_mostrar_tablero(self, mock_stdout): 
        self.tablero.mostrar_tablero()
        output = mock_stdout.getvalue()
        
        self.assertIn("+---+---+---+---+---+---+---+---+", output)
       
if __name__ == '__main__':
    unittest.main()