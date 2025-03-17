# 🧮 PyCalc

## Panoramica
PyCalc è una semplice calcolatrice scritta interamente in Python che si può utilizzare mediante interfaccia a riga di comando (CLI, Command Line Interface). Questo strumento offre un'esperienza di computazione intuitiva ma versatile, fornendo accesso a operatori e funzioni di base, gestione della memoria e un ambiente interattivo (REPL, Read-Evaluate-Print-Loop) per effettuare calcoli al volo dal proprio computer.

## Caratteristiche

- **Operatori matematici fondamentali** ➕➖✖️➗: somma, differenza, prodotto, rapporto ed elevazione a potenza;
- **Funzioni scientifiche** 📊: radice quadrata, funzioni trigonometriche, logaritmiche e altre funzioni dalla libreria `math` del Python;
- **Costanti matematiche** 🔢: accesso a `π`, ed `e` (base del logaritmo naturale);
- **Funzionalità di memoria** 💾: salvataggio dell'ultimo risultato in una variabile speciale `ans`;
- **Definizione di variabili** 🔄: creazione, modifica, visualizzazione ed eliminazione di variabili custom;
- **Interfaccia semplice** 🖥️: interfaccia a riga di comando per la gestione della calcolatrice.

## Requisiti di sistema 🖥️

- Python 3.x.x
- Moduli standard di Python (math, os, subprocess)
- Sistema operativo Windows, macOS o distro Linux

### Comandi disponibili

- **Valutazione di espressioni matematiche** 🔢: inserisci l'espressione da calcolare da tastiera (es. `2 + 3`, `sin(pi)`);
- **Assegnazione di variabili** 📝: memorizza valori in variabili custom (es. `x = 10`);
- **`vars`** 📋: mostra le variabili salvate;
- **`clear`** 🧹: pulisce la console;
- **`clear <nome_variabile>`** 🗑️: elimina una variabile;
- **`clear all`** 🔄: ripristina l'ambiente di calcolo;
- **`help`** ❓: mostra un messaggio di help;
- **CTRL+C** 🚪: termina l'applicazione.

## Funzionalità nel dettaglio ⚙️

PyCalc fornisce accesso a molte funzioni e costanti della libreria `math` del Python:

- Funzioni trigonometriche 📐: `sin()`, `cos()`, `tan()`, ecc.
- Funzioni esponenziali e logaritmiche 📈: `exp()`, `log()`, `log10()`, ecc.
- Funzioni di arrotondamento 🔄: `floor()`, `ceil()`, ecc.
- Costanti matematiche 🧠: `pi`, `e`, ecc.

## Licenza 📄

Questo progetto è distribuito con licenza MIT. Vedere il file [LICENSE](LICENSE) per maggiori dettagli.
