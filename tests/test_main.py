#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    [ PyCalc | Unit Test -- Main Module ]

    [ Brief ]
        Lightweight Python calculator using CLI (Command Line Interface).

    [ Description ]
        This calculator provides basic math operators, functions, and constants.
'''


import os  # Per identificare il sistema operativo
import math  # Per le funzioni matematiche
import sys  # Per l'interazione con il SO e l'interprete Python
import unittest   # Per l'esecuzione di test automatizzati

# Inserisce la cartella 'src' nel path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import PyCalc  # Classe da testare

class TestPyCalc(unittest.TestCase):
    '''Classe di test per il modulo principale'''

    def setUp(self):
        # Inizializza un'istanza della calcolatrice
        self.calculator = PyCalc()

    def evaluate(self, prompt):
        return self.calculator.evaluate(prompt)

    # 1. Operazioni aritmetiche di base
    def test_001_addition(self):
        self.assertEqual(self.evaluate("1 + 1"), 2)

    def test_002_subtraction(self):
        self.assertEqual(self.evaluate("5 - 2"), 3)

    def test_003_multiplication(self):
        self.assertEqual(self.evaluate("3 * 4"), 12)

    def test_004_division(self):
        self.assertEqual(self.evaluate("8 / 2"), 4.0)

    def test_005_float_division(self):
        self.assertEqual(self.evaluate("7 / 2"), 3.5)

    def test_006_exponentiation(self):
        self.assertEqual(self.evaluate("2 ** 3"), 8)

    def test_007_modulo(self):
        self.assertEqual(self.evaluate("10 % 3"), 1)

    # 2. Funzioni matematiche
    def test_008_sqrt(self):
        self.assertAlmostEqual(self.evaluate("sqrt(16)"), 4.0)

    def test_009_sine(self):
        self.assertAlmostEqual(self.evaluate("sin(pi / 2)"), 1.0)

    def test_010_cosine(self):
        self.assertAlmostEqual(self.evaluate("cos(0)"), 1.0)

    def test_011_tangent(self):
        self.assertAlmostEqual(self.evaluate("tan(pi/4)"), 1.0, places=5)

    def test_012_logarithm(self):
        self.assertAlmostEqual(self.evaluate("log(e)"), 1.0)

    def test_013_log10(self):
        self.assertAlmostEqual(self.evaluate("log10(100)"), 2.0)

    def test_014_factorial(self):
        self.assertEqual(self.evaluate("factorial(5)"), 120)

    def test_015_pi_constant(self):
        self.assertAlmostEqual(self.evaluate("pi"), math.pi)

    def test_016_e_constant(self):
        self.assertAlmostEqual(self.evaluate("e"), math.e)

    # 3. Espressioni con numeri negativi e parentesizzazioni
    def test_017_negative_numbers(self):
        self.assertEqual(self.evaluate("-5 + 3"), -2)

    def test_018_parentheses(self):
        self.assertEqual(self.evaluate("(2 + 3) * 4"), 20)

    def test_019_order_of_operations(self):
        self.assertEqual(self.evaluate("2 + 3 * 4"), 14)

    # 4. Gestione degli errori
    def test_020_division_by_zero(self):
        with self.assertRaises(Exception):
            self.evaluate("1/0")

    def test_021_invalid_syntax(self):
        with self.assertRaises(Exception):
            self.evaluate("2 +")

    def test_022_unknown_function(self):
        with self.assertRaises(Exception):
            self.evaluate("unknown_func(2)")

    # 5. Altre operazioni aritmetiche
    def test_023_subtraction_negative_result(self):
        self.assertEqual(self.evaluate("3 - 5"), -2)

    def test_024_negative_multiplication(self):
        self.assertEqual(self.evaluate("-3 * 5"), -15)

    def test_025_negative_division(self):
        self.assertEqual(self.evaluate("-10 / 2"), -5.0)

    def test_026_float_multiplication(self):
        self.assertAlmostEqual(self.evaluate("3.5 * 2"), 7.0)

    def test_027_float_division(self):
        self.assertAlmostEqual(self.evaluate("7.0 / 2"), 3.5)

    def test_028_negative_exponent(self):
        self.assertAlmostEqual(self.evaluate("2 ** -1"), 0.5)

    def test_029_modulo_operator(self):
        self.assertEqual(self.evaluate("10 % 3"), 1)

    def test_030_complex_expression(self):
        self.assertEqual(self.evaluate("2 + 3 * 4 - 5/5"), 13.0)

    def test_031_nested_parentheses(self):
        self.assertEqual(self.evaluate("((2 + 3) * (4 - 1))"), 15)

    def test_032_multiple_functions(self):
        self.assertAlmostEqual(self.evaluate("sqrt(25) + sin(pi/2)"), 6.0)

    def test_033_ans_update_after_expression(self):
        self.evaluate("3+3")
        self.assertEqual(self.calculator.local_vars["ans"], 6)

    def test_034_boolean_expression(self):
        self.assertTrue(self.evaluate("3 > 2"))

    def test_035_complex_arithmetic(self):
        self.assertAlmostEqual(self.evaluate("((2+3)**2 - 4)/2"), 10.5)

    def test_036_float_precision(self):
        self.assertAlmostEqual(self.evaluate("0.1 + 0.2"), 0.3)

    def test_037_large_number_multiplication(self):
        self.assertEqual(self.evaluate("1000000 * 1000000"), 1000000000000)


if __name__ == '__main__':
    unittest.main()
