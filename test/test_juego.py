import unittest
from unittest.mock import patch
from chess.interfaz import Juego, BLANCO, NEGRO
from chess.diccionarios import diccionarioSimbolos as simbolos
class TestJuego(unittest.TestCase):

    def setUp(self):
        self.__juego__ = Juego(mostrar_tablero=False)
        self.__tablero__=self.__juego__.__tablero__
    #testea que el juego inicia correctamente, que el turno actual es el de blanco y que hayan 32 piezas
    def test_inicio(self):
        self.assertEqual(self.__juego__.__turno_actual__, BLANCO)
        self.assertEqual(len(self.__juego__.__piezas__), 32)
        self.assertFalse(self.__juego__.__juego_finalizado__)
    #testea que haya una pieza en la posicion e2 y que sea un peon blanco
    def test_determinar_pieza(self):
        pieza = self.__juego__.determinarPieza("e2")
        self.assertIsNotNone(pieza)
        self.assertEqual(pieza.color, BLANCO)
        self.assertEqual(pieza.__class__.__name__, "Peon")
    #simula un movmiento y se fija que el turno sea el blanco 
    @patch('builtins.input', return_value="a2 b2")
    def test_turno_blanco(self, mock_input):
        self.__juego__.__contador_jugadas__ = 0
        self.__juego__.turnos()
        self.assertEqual(self.__juego__.__turno_actual__, BLANCO)
    #simula un movmiento y se fija que el turno sea el negro
    @patch('builtins.input', return_value="h7 h6")
    def test_turno_negro(self, mock_input):
        self.__juego__.__contador_jugadas__ = 1
        self.__juego__.turnos()
        self.assertEqual(self.__juego__.__turno_actual__, NEGRO)
    #se fija que determinar ganador retorne None, porque no hay ganador todavia
    def test_determinar_ganador_sin_ganador_momentaneamente(self):
        resultado = self.__juego__.determinarGanador()
        self.assertIsNone(resultado)
    #testea un inteno de mover una pieza que no existe
    def test_moverPieza_sin_pieza(self):
        self.__juego__.__contador_jugadas__ = 0
        resultado = self.__juego__.moverPieza("a3", "a4")
        self.assertFalse(resultado)
    #testea un intento de mover una pieza fuera de los limites del tablero
    def test_moverPieza_fuera_de_limites(self):
        self.__juego__.__contador_jugadas__ = 0
        resultado = self.__juego__.moverPieza("e2", "e9") 
        self.assertFalse(resultado)
    #testea un intento de mover una pieza desde una posicion que no es valida
    def test_mover_pieza_invalida(self):
        resultado = self.__juego__.moverPieza("a3", "a4")
        self.assertFalse(resultado)
    #simula un movimiento y se fija que el contador de jugadas haya aumentado a 1
 
    @patch('builtins.input', return_value="e2 e4") #testea el funcionamiento del contador de jugadas
    def test_turnos_juego_no_finalizado(self, mock_input):
        self.__juego__.__juego_finalizado__ = False
        self.__juego__.turnos()
        self.assertEqual(self.__juego__.__contador_jugadas__, 0)

<<<<<<< HEAD
    @patch('builtins.input', return_value="e2 e4") #testea el funcionamiento de obeterCoordenadas
    def test_turnos_juego_finalizado(self, mock_input):
        self.assertEqual(self.__juego__.obtenerCoordenadas(), ("e2", "e4"))
    def test_determinar_ganador_negro(self): #simula que gana el negro y testea que el ganador sea el negro
=======

    @patch('builtins.input', return_value="e2 e4") #prueba que contador de jugadas sea 0 
    def test_turnos_juego_no_finalizado(self, mock_input):
        self.__juego__.__juego_finalizado__ = False
        self.__juego__.turnos()
        self.assertEqual(self.__juego__.__contador_jugadas__, 0)
    @patch('builtins.input', return_value="e2 e4") #prueba que obtenerCoordenadas funcione correctamente
    def test_turnos_juego_finalizado(self, mock_input):
        self.assertEqual(self.__juego__.obtenerCoordenadas(), ("e2", "e4"))
    def test_determinar_ganador_negro(self): #simula que no hay piezas de blanco y se fija que el ganador es negro
>>>>>>> 21546ad660191d52356b8d31acbe277637f542a6
        for i in range(8):
            for x in range(2):
                self.__tablero__.__tablero__[i][x]=" "
        self.assertTrue(self.__juego__.determinarGanador())
        self.assertEqual(self.__juego__.__ganador__, NEGRO)
<<<<<<< HEAD
    def test_determinar_ganador_blanco(self): #simula que gana el blanco y testea que el  ganador sea el blanco
=======
    def test_determinar_ganador_blanco(self): #simula que no hay piezas de negro y se fija que el ganador es blanco
>>>>>>> 21546ad660191d52356b8d31acbe277637f542a6
        for i in range(8):
            for x in range(6,8):
                self.__tablero__.__tablero__[i][x]=" "
        self.__tablero__.__tablero__[0][0]="♙"
        self.assertTrue(self.__juego__.determinarGanador())
        self.assertEqual(self.__juego__.__ganador__, BLANCO)


if __name__ == '__main__':
    unittest.main()