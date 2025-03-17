#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    [ PyCalc vers. 1.1.0 ]

    [ Brief ]
        Lightweight Python calculator using CLI (Command Line Interface).

    [ Description ]
        This calculator provides basic math operators, functions, and constants
        as well as a simple memory that allows user to store and retrieve results
        from previous calculations.
'''

import os  # Per identificare il sistema operativo
import math  # Per le funzioni matematiche
import subprocess  # Per eseguire comandi della shell


class PyCalc:
    def __init__(self):
        self.local_vars = {name: getattr(math, name) for name in dir(math)
                           if not name.startswith("__") and name not in ['inf', 'nan', 'tau']}
        self.local_vars['ans'] = 0

    def clear(self):
        '''Pulisce la console'''
        if os.name == 'nt':
            subprocess.call('cls', shell=True)
        else:
            subprocess.call('clear', shell=True)

    def header(self):
        '''Stampa l'header della calcolatrice'''
        print('\n  PyCalc vers. 1.1.0')
        print('  Lightweight Python CLI calculator\n')
        print('  Premere CTRL+C per uscire.\n')

    def alert(self, message: str):
        '''Visualizza un alert'''
        print(f'[!]  {message}')

    def handle_clear(self, prompt: str):
        '''Elimina alcune o tutte le variabili locali'''
        args = prompt.split()
        if len(args) != 2:
            raise SyntaxError('invalid `clear` command')
        target = args[1]
        if target == 'all':
            self.local_vars.clear()
            self.local_vars.update({name: getattr(math, name) for name in dir(math)
                                    if not name.startswith("__") and name not in ['inf', 'nan', 'tau']})
            self.local_vars['ans'] = 0
        else:
            if target not in self.local_vars:
                raise NameError(f'name "{target}" is not defined')
            del self.local_vars[target]

    def handle_vars(self):
        '''Visualizza le variabili locali'''
        numeric_local_vars = [key for key in self.local_vars if isinstance(self.local_vars[key], (int, float))]
        if len(numeric_local_vars) == 0:
            self.alert('No saved variables.')
        for local_var_name in numeric_local_vars:
            print(f'{local_var_name} = {self.local_vars[local_var_name]}')

    def handle_help(self):
        '''Stampa le informazioni di help'''
        help_text = '''
Comandi disponibili in PyCalc:
------------------------------
- Operazioni aritmetiche (es. 2 + 3, 5 * 6, 2 ** 3)
- Assegnazioni: es. x = 10
- Memoria: il risultato dell'ultima valutazione è memorizzato in 'ans'.
- Funzioni: disponibili un'ampia gamma di funzioni matematiche (sqrt, sin, cos, log, ecc.).
- Costanti: fornisce costanti matematiche come pi ed e.
- Comandi speciali:
  - vars        : Visualizza le variabili salvate.
  - clear       : Pulisce la console.
  - clear <var> : Elimina una variabile salvata.
  - clear all   : Ripristina l'ambiente di calcolo (mantiene funzioni e costanti).
  - help        : Mostra questo messaggio di aiuto.
- Premere CTRL+C per uscire.'''
        print(help_text)

    def evaluate(self, prompt: str):
        '''Esegue la valutazione dell'espressione'''
        if any(item in prompt for item in ["'", '"', '`', ',']):
            raise SyntaxError('invalid syntax')
        if '=' in prompt:
            exec(prompt, {'__builtins__': {}}, self.local_vars)
        elif prompt == 'clear':
            self.clear()
        elif prompt.startswith('clear'):
            self.handle_clear(prompt)
        elif prompt == 'vars':
            self.handle_vars()
        elif prompt == 'help':
            self.handle_help()
        else:
            last_result = eval(prompt, {'__builtins__': {}}, self.local_vars)
            self.local_vars['ans'] = last_result
            return last_result

    def run(self):
        '''Avvia il ciclo REPL'''
        self.clear()
        self.header()
        while True:
            try:
                result = self.evaluate(input('> ').strip())
                if result is not None:
                    print(f'  {result}')
                print()
            except KeyboardInterrupt:
                print()
                break
            except Exception as e:
                self.alert('Error: ' + str(e).split('(')[0].capitalize() + '\n')


if __name__ == '__main__':
    PyCalc().run()
