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

if __name__ == '__main__':
    unittest.main()
