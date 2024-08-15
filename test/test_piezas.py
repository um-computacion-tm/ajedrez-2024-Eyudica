import unittest
from chess.tablero import Tablero
from chess.piezas import *

class TestPiezas(unittest.TestCase):

    def setUp(self):
        self.__tablero__ = Tablero()
        self.__peon__ = Peon(BLANCO, 'e2', self.__tablero__)
        self.__torre__ = Torre(BLANCO, 'a1', self.__tablero__)
        self.__alfil__ = Alfil(BLANCO, 'c1', self.__tablero__)
        self.__dama__ = Dama(BLANCO, 'd1', self.__tablero__)
        self.__caballo__ = Caballo(BLANCO, 'b1', self.__tablero__)
        self.__rey__ = Rey(BLANCO, 'e1', self.__tablero__)
        self.__peon__Negro = Peon(NEGRO, 'f5', self.__tablero__)
    #testea que un peon se pueda mover y comer correctamente
    def test_Peon_movimiento(self):
        
        self.assertTrue(self.__peon__.mover('e4', self.__tablero__))
        self.assertEqual(self.__peon__.posicion, 'e4')
        self.assertTrue(self.__peon__.mover('f5', self.__tablero__))
        self.assertEqual(self.__peon__.posicion, 'f5')
        
        self.assertFalse(self.__peon__.mover('e6', self.__tablero__)) #!!!
    #testea que una torre se pueda mover linealmente correctamente
    def test_Torre_movimiento(self):
        self.assertTrue(self.__torre__.mover('a4', self.__tablero__))
        self.assertEqual(self.__torre__.posicion, 'a4')
        
        self.assertTrue(self.__torre__.mover('d4', self.__tablero__))
        self.assertEqual(self.__torre__.posicion, 'd4')
        
        self.assertFalse(self.__torre__.mover('e5', self.__tablero__))
    #testea que un alfil se pueda mover diagonalmente correctamente
    def test_Alfil_movimiento(self):
        self.assertTrue(self.__alfil__.mover('f4', self.__tablero__)) #!!
        self.assertEqual(self.__alfil__.posicion, 'f4')
        
        self.assertFalse(self.__alfil__.mover('h1', self.__tablero__))
    #teste que una dama se pueda mover linealmente y diagonalmente correctamente
    def test_Dama_movimiento(self):
        self.assertTrue(self.__dama__.mover('a4', self.__tablero__))
        self.assertEqual(self.__dama__.posicion, 'a4')
        
        self.assertFalse(self.__dama__.mover('h6', self.__tablero__))
        self.assertEqual(self.__dama__.posicion, 'a4')
        
        self.assertFalse(self.__dama__.mover('e5', self.__tablero__))
    #testea que un caballo se pueda mover correctamente
    def test_Caballo_movimiento(self):
        self.assertTrue(self.__caballo__.mover('c3', self.__tablero__))
        self.assertEqual(self.__caballo__.posicion, 'c3')
        
        self.assertFalse(self.__caballo__.mover('c8', self.__tablero__))
    #testea que un rey se pueda mover correctamente
    def test_Rey_movimiento(self):
        self.assertTrue(self.__rey__.mover('d2', self.__tablero__))
        self.assertEqual(self.__rey__.posicion, 'd2')
        
        self.assertFalse(self.__rey__.mover('e6', self.__tablero__))
    #testea que las piezas puedan obtener sus simbolos correctamente
    def test_obtenerSimbolos(self):
        self.assertEqual(self.__peon__.obtenerSimbolos(), '♙')
        self.assertEqual(self.__torre__.obtenerSimbolos(), '♖')
        self.assertEqual(self.__alfil__.obtenerSimbolos(), '♗')
        self.assertEqual(self.__dama__.obtenerSimbolos(), '♕')
        self.assertEqual(self.__caballo__.obtenerSimbolos(), '♘')
        self.assertEqual(self.__rey__.obtenerSimbolos(), '♔')
        self.assertEqual(self.__peon__Negro.obtenerSimbolos(), '♟')
#
if __name__ == '__main__':
    unittest.main()
