import unittest
from unittest.mock import patch
from chess.piezas.piezas import *
from chess.piezas.peon import Peon
from chess.piezas.torre import Torre
from chess.piezas.alfil import Alfil
from chess.piezas.dama import Dama
from chess.piezas.rey import Rey
from chess.piezas.caballo import Caballo
from chess.tablero import Tablero
from chess.diccionarios import diccionarioSimbolos as simbolos
from chess.diccionarios import diccionarioFilas as posiciones
from chess.interfaz import Juego

class TestJuego(unittest.TestCase):

    def setUp(self):
        self.juego = Juego(mostrar_tablero=False)
        self.juego.inicializarPiezas()
        self.juego.agregarPiezasEnTablero()
        self.piezas = self.juego.__piezas__

    def test_piezas_iniciales(self):
        self.assertEqual(len(self.piezas), 32)

    def test_determinar_pieza(self):
        pieza = self.juego.determinarPieza((0, 1))
        self.assertIsInstance(pieza, Peon)
        self.assertEqual(pieza.color, BLANCO)
        pieza = self.juego.determinarPieza((4, 0))
        self.assertIsInstance(pieza, Rey)
        self.assertEqual(pieza.color, BLANCO)
        pieza = self.juego.determinarPieza((0, 6))
        self.assertFalse(pieza)

    def test_determinar_pieza_destino(self):
        pieza = Peon(NEGRO, (1, 2))
        self.juego.__piezas__.append(pieza)
        pieza_encontrada = self.juego.determinarPiezaDestino((1, 2))
        self.assertIsNotNone(pieza_encontrada)
        self.assertEqual(pieza_encontrada.color, NEGRO)
        pieza_encontrada = self.juego.determinarPiezaDestino((3, 3))
        self.assertFalse(pieza_encontrada)

    def test_mover_pieza(self):
        pieza = Peon(BLANCO, (0, 1))
        self.juego.__piezas__.append(pieza)
        resultado = self.juego.moverPieza((0, 1), (0, 2))
        self.assertTrue(resultado)
        self.assertEqual(pieza.columna, 0)
        resultado = self.juego.moverPieza((0, 2), (0, 6))
        self.assertFalse(resultado)

    def test_excepcion(self):
        self.assertTrue(self.juego.excepcion("a1 b2"))
        self.assertFalse(self.juego.excepcion("a2 a9"))
        self.assertFalse(self.juego.excepcion("a1 b"))
        self.assertFalse(self.juego.excepcion("a1 b20"))
        self.assertFalse(self.juego.excepcion("asdfasfdsaf3b6wq6baeba4*%)&($&%^($&))"))

    def test_determinar_ganador(self):
        self.assertIsNone(self.juego.determinarGanador())
        self.juego.__piezas__ = [pieza for pieza in self.juego.__piezas__ if pieza.color == BLANCO]
        self.assertEqual(self.juego.determinarGanador(), BLANCO)

    def test_turnos(self):
        self.juego.turnos()
        self.assertEqual(self.juego.__turno_actual__, BLANCO)
        self.juego.__contador_jugadas__ = 1
        self.juego.turnos()
        self.assertEqual(self.juego.__turno_actual__, NEGRO)

    @patch('builtins.input', side_effect=['a2a3'])
    def test_procesar_input_valido(self, mock_input):
        resultado = self.juego.ProcesarInput()
        self.assertEqual(resultado, ((0, 1), (0, 2)))
        self.assertFalse(self.juego.__juego_finalizado__)

    @patch('builtins.input', side_effect=['exit'])
    def test_procesar_input_exit(self, mock_input):
        resultado = self.juego.ProcesarInput()
        self.assertFalse(resultado)
        self.assertTrue(self.juego.__juego_finalizado__)
    def test_no_pieza_en_posicion_inicial(self):
        resultado = self.juego.moverPieza((5, 5), (5, 6))
        self.assertFalse(resultado)

    def test_pieza_en_posicion_inicial(self):
        pieza = Peon(BLANCO, (0, 1))
        self.juego.__piezas__.append(pieza)

        resultado = self.juego.moverPieza((0, 1), (0, 2))
        self.assertTrue(resultado)

if __name__ == '__main__':
    unittest.main()
