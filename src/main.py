#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    [ PyCalc vers. 1.0.0 ]

    [ Brief ]
        Lightweight Python calculator using CLI (Command Line Interface).

    [ Description ]
        This calculator provides basic math operators, functions, and constants.
'''

import os  # Per identificare il sistema operativo
import math  # Per le funzioni matematiche
import subprocess  # Per eseguire comandi della shell

class PyCalc:
    def __init__(self):
        '''Inizializza la calcolatrice'''
        self.local_vars = {name: getattr(math, name) for name in dir(math) if not name.startswith("__")}
        self.local_vars['ans'] = 0
    
    def clear(self) -> None:
        '''Effettua il `clear` del Prompt dei Comandi/Terminale'''
        if os.name == 'nt':
            subprocess.call('cls', shell=True)
        else:
            subprocess.call('clear', shell=True)
    
    def header(self) -> None:
        '''Stampa l'header della calcolatrice'''
        print('\n  PyCalc vers. 1.0.0')
        print('  Lightweight Python CLI calculator\n')
        print('  Premere CTRL+C per uscire.\n')
    
    def alert(self, message: str) -> None:
        '''Visualizza un alert'''
        print(f'[!]  {message}')
    
    def init(self) -> None:
        '''Inizializzazione dell'ambiente'''
        self.clear()
        self.header()
    
    def handle_help(self) -> None:
        '''Stampa le informazioni di help'''
        help_text = '''
Comandi disponibili in PyCalc:
------------------------------
- Operazioni aritmetiche (es. 2 + 3, 5 * 6, 2 ** 3)
- Memoria: il risultato dell'ultima valutazione è memorizzato in 'ans'.
- Funzioni: disponibili un'ampia gamma di funzioni matematiche (sqrt, sin, cos, log, ecc.).
- Costanti: fornisce costanti matematiche come pi ed e.
- Comandi speciali:
  - help        : Mostra questo messaggio di aiuto.
- Premere CTRL+C per uscire.'''
        print(help_text)
    
    def evaluate(self, prompt: str) -> str | None:
        '''Esegue la valutazione dell'espressione'''
        result = None
        if any(item in prompt for item in ["'", '"', '`', ',']):
            raise SyntaxError('invalid syntax')
        
        if prompt == 'help':
            self.handle_help()
        elif prompt == 'clear':
            self.clear()
        else:
            last_result = eval(
                prompt,
                {'__builtins__': {}},
                self.local_vars
            )
            self.local_vars['ans'] = last_result
            result = last_result
        return result
    
    def run(self) -> None:
        '''Funzione principale che implementa il REPL loop'''
        self.init()
        while True:
            try:
                last_result = self.evaluate(input('> ').strip())
                if last_result is not None:
                    print(f'  ' + str(last_result))
                print()
            except KeyboardInterrupt:
                print()
                break
            except Exception as e:
                self.alert('Error: ' + str(e).split('(')[0].capitalize() + '\n')

if __name__ == '__main__':
    PyCalc().run()
