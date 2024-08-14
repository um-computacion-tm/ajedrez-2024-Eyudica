import unittest
from unittest.mock import patch
from chess.interfaz import Juego, BLANCO, NEGRO
from chess.diccionarios import diccionarioSimbolos as simbolos
class TestJuego(unittest.TestCase):

    def setUp(self):
        self.juego = Juego(mostrar_tablero=False)
    #testea que el juego inicia correctamente, que el turno actual es el de blanco y que hayan 32 piezas
    def test_inicio(self):
        self.assertEqual(self.juego.turno_actual, BLANCO)
        self.assertEqual(len(self.juego.piezas), 32)
        self.assertFalse(self.juego.juego_finalizado)
    #testea que haya una pieza en la posicion e2 y que sea un peon blanco
    def test_determinar_pieza(self):
        pieza = self.juego.determinarPieza("e2")
        self.assertIsNotNone(pieza)
        self.assertEqual(pieza.color, BLANCO)
        self.assertEqual(pieza.__class__.__name__, "Peon")
    #simula un movmiento y se fija que el turno sea el blanco 
    @patch('builtins.input', return_value="a2 b2")
    def test_turno_blanco(self, mock_input):
        self.juego.contador_jugadas = 0
        self.juego.turnos()
        self.assertEqual(self.juego.turno_actual, BLANCO)
    #simula un movmiento y se fija que el turno sea el negro
    @patch('builtins.input', return_value="h7 h6")
    def test_turno_negro(self, mock_input):
        self.juego.contador_jugadas = 1
        self.juego.turnos()
        self.assertEqual(self.juego.turno_actual, NEGRO)
    #se fija que determinar ganador retorne None, porque no hay ganador todavia
    def test_determinar_ganador_sin_ganador_momentaneamente(self):
        result = self.juego.determinarGanador()
        self.assertIsNone(result)
    #testea un inteno de mover una pieza que no existe
    def test_moverPieza_sin_pieza(self):
        self.juego.contador_jugadas = 0
        resultado = self.juego.moverPieza("a3", "a4")
        self.assertFalse(resultado)
    #testea un intento de mover una pieza fuera de los limites del tablero
    def test_moverPieza_fuera_de_limites(self):
        self.juego.contador_jugadas = 0
        resultado = self.juego.moverPieza("e2", "e9") 
        self.assertFalse(resultado)
    #testea un intento de mover una pieza desde una posicion que no es valida
    def test_mover_pieza_invalida(self):
        resultado = self.juego.moverPieza("a3", "a4")
        self.assertFalse(resultado)
    #simula un movimiento y se fija que el contador de jugadas haya aumentado a 1

    @patch('builtins.input', return_value="e2 e4")
    def test_turnos_juego_no_finalizado(self, mock_input):
        self.juego.juego_finalizado = False
        self.juego.turnos()
        self.assertEqual(self.juego.contador_jugadas, 1)



if __name__ == '__main__':
    unittest.main()