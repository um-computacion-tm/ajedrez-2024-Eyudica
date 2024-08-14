import unittest
from chess.tablero import Tablero
from chess.piezas import *

class TestPiezas(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()
        self.Peon = Peon(BLANCO, 'e2', self.tablero)
        self.Torre = Torre(BLANCO, 'a1', self.tablero)
        self.Alfil = Alfil(BLANCO, 'c1', self.tablero)
        self.Dama = Dama(BLANCO, 'd1', self.tablero)
        self.Caballo = Caballo(BLANCO, 'b1', self.tablero)
        self.Rey = Rey(BLANCO, 'e1', self.tablero)
        self.PeonNegro = Peon(NEGRO, 'f5', self.tablero)
    #testea que un peon se pueda mover y comer correctamente
    def test_Peon_movimiento(self):
        
        self.assertTrue(self.Peon.mover('e4', self.tablero))
        self.assertEqual(self.Peon.posicion, 'e4')
        self.assertTrue(self.Peon.mover('f5', self.tablero))
        self.assertEqual(self.Peon.posicion, 'f5')
        
        self.assertFalse(self.Peon.mover('e6', self.tablero)) #!!!
    #testea que una torre se pueda mover linealmente correctamente
    def test_Torre_movimiento(self):
        self.assertTrue(self.Torre.mover('a4', self.tablero))
        self.assertEqual(self.Torre.posicion, 'a4')
        
        self.assertTrue(self.Torre.mover('d4', self.tablero))
        self.assertEqual(self.Torre.posicion, 'd4')
        
        self.assertFalse(self.Torre.mover('e5', self.tablero))
    #testea que un alfil se pueda mover diagonalmente correctamente
    def test_Alfil_movimiento(self):
        self.assertTrue(self.Alfil.mover('f4', self.tablero)) #!!
        self.assertEqual(self.Alfil.posicion, 'f4')
        
        self.assertFalse(self.Alfil.mover('h1', self.tablero))
    #teste que una dama se pueda mover linealmente y diagonalmente correctamente
    def test_Dama_movimiento(self):
        self.assertTrue(self.Dama.mover('a4', self.tablero))
        self.assertEqual(self.Dama.posicion, 'a4')
        
        self.assertFalse(self.Dama.mover('h6', self.tablero))
        self.assertEqual(self.Dama.posicion, 'a4')
        
        self.assertFalse(self.Dama.mover('e5', self.tablero))
    #testea que un caballo se pueda mover correctamente
    def test_Caballo_movimiento(self):
        self.assertTrue(self.Caballo.mover('c3', self.tablero))
        self.assertEqual(self.Caballo.posicion, 'c3')
        
        self.assertFalse(self.Caballo.mover('c8', self.tablero))
    #testea que un rey se pueda mover correctamente
    def test_Rey_movimiento(self):
        self.assertTrue(self.Rey.mover('d2', self.tablero))
        self.assertEqual(self.Rey.posicion, 'd2')
        
        self.assertFalse(self.Rey.mover('e6', self.tablero))
    #testea que las piezas puedan obtener sus simbolos correctamente
    def test_obtenerSimbolos(self):
        self.assertEqual(self.Peon.obtenerSimbolos(), '♙')
        self.assertEqual(self.Torre.obtenerSimbolos(), '♖')
        self.assertEqual(self.Alfil.obtenerSimbolos(), '♗')
        self.assertEqual(self.Dama.obtenerSimbolos(), '♕')
        self.assertEqual(self.Caballo.obtenerSimbolos(), '♘')
        self.assertEqual(self.Rey.obtenerSimbolos(), '♔')
        self.assertEqual(self.PeonNegro.obtenerSimbolos(), '♟')

if __name__ == '__main__':
    unittest.main()
