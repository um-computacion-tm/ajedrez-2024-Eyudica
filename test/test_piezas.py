from chess.piezas.piezas import *
from chess.piezas.peon import Peon
from chess.piezas.torre import Torre
from chess.piezas.alfil import Alfil
from chess.piezas.dama import Dama
from chess.piezas.rey import Rey
from chess.piezas.caballo import Caballo
import unittest

BLANCO = 'Blanco'
NEGRO = 'Negro'

class TestPiezas(unittest.TestCase):

    def setUp(self):
        # Configurar algunas piezas comunes para los tests
        self.peon_blanco = Peon(BLANCO, (1,2))
        self.torre_negra = Torre(NEGRO, (0,0))
        self.alfil_blanco = Alfil(BLANCO, (2,0))
        self.dama_negra = Dama(NEGRO, (3,3))
        self.caballo_blanco = Caballo(BLANCO, (1,0))
        self.rey_negro = Rey(NEGRO, (4,4))
    def test_columna_anterior(self):
        self.assertEqual(self.torre_negra.columna_anterior, self.torre_negra.columna)
    
    def test_fila_anterior(self):
        self.assertEqual(self.torre_negra.fila_anterior, self.torre_negra.fila)
    def test_simbolo(self):
        self.assertEqual(self.torre_negra.simbolo, "♖")
    def test_setters_anteriores(self):
        self.torre_negra.columna_anterior = 1
        self.torre_negra.fila_anterior = 1
        self.assertEqual(self.torre_negra.columna_anterior, 1)
        self.assertEqual(self.torre_negra.fila_anterior, 1)

    def test_setters_posicion(self):
        self.torre_negra.columna = 2
        self.torre_negra.fila = 2
        self.assertEqual(self.torre_negra.columna, 2)
        self.assertEqual(self.torre_negra.fila, 2)

    def test_establecer_posicion(self):
        self.torre_negra.establecerPosicion((1, 1))
        self.assertEqual(self.torre_negra.columna, 1)
        self.assertEqual(self.torre_negra.fila, 1)
        self.assertEqual(self.torre_negra.columna_anterior, 0)
        self.assertEqual(self.torre_negra.fila_anterior, 0)

    def test_str(self):
        resultado=self.peon_blanco.__str__()
        self.assertEqual("La pieza es Peon con color Blanco en la posicion (1, 2) y el simbolo es ♟", resultado)


    def test_peon_creacion(self):
        self.assertEqual(self.peon_blanco.tipo, "Peon")
        self.assertEqual(self.peon_blanco.color, BLANCO)
        self.assertEqual((self.peon_blanco.columna, self.peon_blanco.fila), (1, 2))

    def test_peon_movimiento_avance(self):
        posiciones = self.peon_blanco.checkMovimiento((1, 3))
        self.assertIn((1, 3), posiciones)
    def test_peon_movimiento_doble_avance(self):
        self.assertTrue(self.peon_blanco.checkMovimiento((1, 4)))
    def test_peon_movimiento_diagonal(self):
        self.assertTrue(self.peon_blanco.checkMovimiento((2, 3)))
    def test_torre_creacion(self):
        self.assertEqual(self.torre_negra.tipo, "Torre")
        self.assertEqual(self.torre_negra.color, NEGRO)
        self.assertEqual((self.torre_negra.columna, self.torre_negra.fila), (0, 0))

    def test_torre_movimiento_x(self):
        posiciones = self.torre_negra.checkMovimiento((0, 5))
        self.assertIn((0, 5), posiciones)
    def test_torre_movmiento_y(self):
        posiciones = self.torre_negra.checkMovimiento((5, 0))
        self.assertIn((5, 0), posiciones)
        self.assertIn((4, 0), posiciones)
    def test_alfil_creacion(self):
        self.assertEqual(self.alfil_blanco.tipo, "Alfil")
        self.assertEqual(self.alfil_blanco.color, BLANCO)
        self.assertEqual((self.alfil_blanco.columna, self.alfil_blanco.fila), (2, 0))

    def test_alfil_movimiento(self):
        posiciones = self.alfil_blanco.checkMovimiento((4, 2))
        self.assertIn((3, 1), posiciones)
        self.assertIn((4, 2), posiciones)

    def test_dama_creacion(self):
        self.assertEqual(self.dama_negra.tipo, "Dama")
        self.assertEqual(self.dama_negra.color, NEGRO)
        self.assertEqual((self.dama_negra.columna, self.dama_negra.fila), (3, 3))

    def test_dama_movimiento(self):
        posiciones = self.dama_negra.checkMovimiento((7, 7)) 
        self.assertIn((4, 4), posiciones)
        self.assertIn((7, 7), posiciones)
    def test_dama_movimiento_invalido(self): 
        self.assertFalse(self.dama_negra.checkMovimiento((4,7)))
    def test_caballo_creacion(self):
        self.assertEqual(self.caballo_blanco.tipo, "Caballo")
        self.assertEqual(self.caballo_blanco.color, BLANCO)
        self.assertEqual((self.caballo_blanco.columna, self.caballo_blanco.fila), (1, 0))

    def test_caballo_movimiento(self):
        self.assertTrue(self.caballo_blanco.checkMovimiento((2, 2)))
        self.assertFalse(self.caballo_blanco.checkMovimiento((3, 3)))

    def test_rey_creacion(self):
        self.assertEqual(self.rey_negro.tipo, "Rey")
        self.assertEqual(self.rey_negro.color, NEGRO)
        self.assertEqual((self.rey_negro.columna, self.rey_negro.fila), (4, 4))

    def test_rey_movimiento(self):
        self.assertTrue(self.rey_negro.checkMovimiento((5, 5)))
        self.assertFalse(self.rey_negro.checkMovimiento((6, 6)))
 
if __name__ == '__main__':
    unittest.main()
