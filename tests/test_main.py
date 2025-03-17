#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    [ PyCalc | Unit Test -- Main Module ]

    [ Brief ]
        Lightweight Python calculator using CLI (Command Line Interface).

    [ Description ]
        This calculator provides basic math operators, functions, and constants
        as well as a simple memory that allows user to store and retrieve results
        from previous calculations.
'''


import os  # Per identificare il sistema operativo
import io   # Per la gestione dell'I/O
import math  # Per le funzioni matematiche
import sys  # Per l'interazione con il SO e l'interprete Python
import unittest   # Per l'esecuzione di test automatizzati

from contextlib import redirect_stdout  # Per la redirezione dello standard output

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

    # 4. Assegnazioni di variabili e aggiornamento di ans
    def test_020_variable_assignment(self):
        self.evaluate("x = 10")
        self.assertIn("x", self.calculator.local_vars)
        self.assertEqual(self.evaluate("x * 2"), 20)

    def test_021_assignment_expression(self):
        self.evaluate("y = 3 + 4")
        self.assertEqual(self.calculator.local_vars["y"], 7)

    def test_022_update_ans(self):
        self.evaluate("1+1")
        self.assertEqual(self.calculator.local_vars["ans"], 2)

    def test_023_chain_assignment(self):
        self.evaluate("x = 5")
        self.evaluate("x = x + 2")
        self.assertEqual(self.calculator.local_vars["x"], 7)

    # 5. Comando clear per rimuovere variabili
    def test_024_clear_single_variable(self):
        self.evaluate("a = 15")
        self.calculator.handle_clear("clear a")
        self.assertNotIn("a", self.calculator.local_vars)

    def test_025_clear_invalid_no_param(self):
        with self.assertRaises(SyntaxError):
            self.calculator.handle_clear("clear")

    def test_026_clear_nonexistent_variable(self):
        with self.assertRaises(NameError):
            self.calculator.handle_clear("clear z")

    def test_027_clear_all(self):
        self.evaluate("b = 20")
        self.evaluate("c = 30")
        self.calculator.handle_clear("clear all")
        self.assertNotIn("b", self.calculator.local_vars)
        self.assertNotIn("c", self.calculator.local_vars)
        self.assertIn("ans", self.calculator.local_vars)
        self.assertEqual(self.calculator.local_vars["ans"], 0)

    # 6. Gestione degli errori
    def test_028_division_by_zero(self):
        with self.assertRaises(Exception):
            self.evaluate("1/0")

    def test_029_invalid_syntax(self):
        with self.assertRaises(Exception):
            self.evaluate("2 +")

    def test_030_unknown_function(self):
        with self.assertRaises(Exception):
            self.evaluate("unknown_func(2)")

    # 7. Altre operazioni aritmetiche
    def test_031_subtraction_negative_result(self):
        self.assertEqual(self.evaluate("3 - 5"), -2)

    def test_032_negative_multiplication(self):
        self.assertEqual(self.evaluate("-3 * 5"), -15)

    def test_033_negative_division(self):
        self.assertEqual(self.evaluate("-10 / 2"), -5.0)

    def test_034_float_multiplication(self):
        self.assertAlmostEqual(self.evaluate("3.5 * 2"), 7.0)

    def test_035_float_division(self):
        self.assertAlmostEqual(self.evaluate("7.0 / 2"), 3.5)

    def test_036_negative_exponent(self):
        self.assertAlmostEqual(self.evaluate("2 ** -1"), 0.5)

    def test_037_modulo_operator(self):
        self.assertEqual(self.evaluate("10 % 3"), 1)

    def test_038_complex_expression(self):
        # 2 + 3 * 4 - 5/5 = 2 + 12 - 1 = 13
        self.assertEqual(self.evaluate("2 + 3 * 4 - 5/5"), 13.0)

    def test_039_nested_parentheses(self):
        self.assertEqual(self.evaluate("((2 + 3) * (4 - 1))"), 15)

    def test_040_multiple_functions(self):
        self.assertAlmostEqual(self.evaluate("sqrt(25) + sin(pi/2)"), 6.0)

    # 8. Altri casi con assegnazioni e aggiornamenti
    def test_041_variable_assignment_with_function(self):
        self.evaluate("z = sqrt(9)")
        self.assertEqual(self.calculator.local_vars["z"], 3.0)

    def test_042_handle_vars_output(self):
        self.evaluate("var_test = 123")
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            self.calculator.handle_vars()
        output = captured_output.getvalue()
        self.assertIn("var_test = 123", output)

    def test_043_assignment_returns_none(self):
        # Verifica che un assegnamento ritorni None
        result = self.evaluate("a = 5")
        self.assertIsNone(result)

    def test_044_ans_update_after_expression(self):
        self.evaluate("3+3")
        self.assertEqual(self.calculator.local_vars["ans"], 6)

    def test_045_boolean_expression(self):
        self.assertTrue(self.evaluate("3 > 2"))

    def test_046_complex_arithmetic(self):
        self.assertAlmostEqual(self.evaluate("((2+3)**2 - 4)/2"), 10.5)

    def test_047_float_precision(self):
        self.assertAlmostEqual(self.evaluate("0.1 + 0.2"), 0.3)

    def test_048_large_number_multiplication(self):
        self.assertEqual(self.evaluate("1000000 * 1000000"), 1000000000000)


if __name__ == '__main__':
    unittest.main()
