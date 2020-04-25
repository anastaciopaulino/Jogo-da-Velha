""" Jogo da forca """
#!/usr/bin/python3
# Autor: Anastácio Paulino
# Title: Jogo da Forca
# Data: 2020-04-20

from os import system
from logic import *
import platform
import sys

def welcome():
    print(r"""
    ╔═══════════════════════════════════════════════════════════════════════════════╗
════╝
     ┌─────────────────────────────────────────────────────────────────────────────┐
     │                                  Welcome                                    │
     ├─────────────────────────────────────────────────────────────────────────────┤
     │                                                                             │
     │       _                         _        __     __   _ _                    │
     │      | | ___   __ _  ___     __| | __ _  \ \   / /__| | |                   │
     │   _  | |/ _ \ / _` |/ _ \   / _` |/ _` |  \ \ / / _ \ | '_ \ / _` |         │
     │  | |_| | (_) | (_| | (_) | | (_| | (_| |   \ V /  __/ | | | | (_| |         │
     │   \___/ \___/ \__, |\___/   \__,_|\__,_|    \_/ \___|_|_| |_|\__,_|         │
     │              |___/  1.0                                                     │
     │                      https://github.com/anastaciopaulino                    │
     │                                                                             │
     └─────────────────────────────────────────────────────────────────────────────┘
════╗  BY: Anastácio Paulino
    ╚═══════════════════════════════════════════════════════════════════════════════╝
    """)

print(r"""

     _                         _        __     __   _ _           
    | | ___   __ _  ___     __| | __ _  \ \   / /__| | |__   __ _ 
 _  | |/ _ \ / _` |/ _ \   / _` |/ _` |  \ \ / / _ \ | '_ \ / _` |
| |_| | (_) | (_| | (_) | | (_| | (_| |   \ V /  __/ | | | | (_| |
 \___/ \___/ \__, |\___/   \__,_|\__,_|    \_/ \___|_|_| |_|\__,_|
             |___/  1.0

""")


help()
try:
    input("[ENTER] PARA INICIAR: ")
    if("windows" in platform.system().lower()):
        comando = "cls"
    else:
        comando = "clear"

    system(comando)

    welcome()
    print("[1] One Player")
    print("[2] Two Player")

    player = input("Como quer jogar? ")

    while player != "1" and player != "2":
        print("Essa opção não existe!")
        player = input("COmo quer jogar? ")
except:
    print("\n[!]Aconteceu um erro não programavel [!]")
    sys.exit(1)

system(comando)

printBoard(theBoard)
if player == "1":

    if not (onePlayer()):
        print("Empate !")

elif player == "2":

    if not (twoPlayer()):
        print("Empate !")
else:
    print("Aconteceu um erro não programavel")
    sys.exit(1)