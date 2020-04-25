import sys
import random


theBoard = {"7": "", "8": "", "9": "",
    "4": "", "5": "", "6": "",
    "1": "", "2":"", "3": ""
}

# Ajuda do jogo
def help():
    print("  {}  ||  {}  ||  {}".format(7, 8, 9))
    print("=======================")
    print("  {}  ||  {}  ||  {}".format(4, 5, 6))
    print("=======================")
    print("  {}  ||  {}  ||  {}".format(1, 2, 3))

# Printar o tabuleiro
def printBoard(board):
    print("  {:3}||  {:3}||  {:3}".format(board["7"], board["8"], board["9"]))
    print("====================")
    print("  {:3}||  {:3}||  {:3}".format(board["4"], board["5"], board["6"]))
    print("====================")
    print("  {:3}||  {:3}||  {:3}".format(board["1"], board["2"], board["3"]))

# Ganhar
def ganhar(board, turn):
    if(board["1"] == turn and board["2"] == turn and board["3"] == turn):
        printBoard(theBoard)
        print(f"O jogador {turn} ganhou")
        print("Parabéns!!")
        return True
    elif(board["4"] == turn and board["5"] == turn and board["6"] == turn):
        printBoard(theBoard)
        print(f"O jogador {turn} ganhou")
        print("Parabéns!!")
        return True
    elif(board["7"] == turn and board["8"] == turn and board["9"] == turn):
        printBoard(theBoard)
        print(f"O jogador {turn} ganhou")
        print("Parabéns!!")
        return True
    elif(board["1"] == turn and board["4"] == turn and board["7"] == turn):
        printBoard(theBoard)
        print(f"O jogador {turn} ganhou")
        print("Parabéns!!")
        return True
    elif(board["2"] == turn and board["5"] == turn and board["8"] == turn):
        printBoard(theBoard)
        print(f"O jogador {turn} ganhou")
        print("Parabéns!!")
        return True
    elif(board["3"] == turn and board["6"] == turn and board["9"] == turn):
        printBoard(theBoard)
        print(f"O jogador {turn} ganhou")
        print("Parabéns!!")
        return True
    elif(board["1"] == turn and board["5"] == turn and board["9"] == turn):
        printBoard(theBoard)
        print(f"O jogador {turn} ganhou")
        print("Parabéns!!")
        return True
    elif(board["3"] == turn and board["5"] == turn and board["7"] == turn):
        printBoard(theBoard)
        print(f"O jogador {turn} ganhou")
        print("Parabéns!!")
        return True


# Computador
class Computador():

        def __init__(self, board, turn, reverse):
            self.board = board
            self.turn = turn
            self.reverse = reverse
        
        # Função para defender os Ataques
        def defender(self):
            # Primeira Linda do Tabuleiro
            if(self.board["1"] == self.turn and self.board["2"] == self.turn and self.board["3"] == ""):
                self.board["3"] = self.reverse
                return self.board["3"]
            elif(self.board["1"] == self.turn and self.board["3"] == self.turn and self.board["2"] == ""):
                self.board["2"] = self.reverse
                return self.board["2"]
            elif(self.board["3"] == self.turn and self.board["2"] == self.turn and self.board["1"] == ""):
                self.board["1"] = self.reverse
                return self.board["1"]

            # Segunda linha
            elif(self.board["4"] == self.turn and self.board["5"] == self.turn and self.board["6"] == ""):
                self.board["6"] = self.reverse
                return self.board["6"]
            elif(self.board["4"] == self.turn and self.board["6"] == self.turn and self.board["5"] == ""):
                self.board["5"] = self.reverse
                return self.board["5"]
            elif(self.board["5"] == self.turn and self.board["6"] == self.turn and self.board["4"] == ""):
                self.board["4"] = self.reverse
                return self.board["4"]
            
            # Terceira Linha
            elif(self.board["7"] == self.turn and self.board["8"] == self.turn and self.board["9"] == ""):
                self.board["9"] = self.reverse
                return self.board["9"]
            elif(self.board["9"] == self.turn and self.board["8"] == self.turn and self.board["7"] == ""):
                self.board["7"] = self.reverse
                return self.board["7"]
            elif(self.board["7"] == self.turn and self.board["9"] == self.turn and self.board["8"] == ""):
                self.board["8"] = self.reverse
                return self.board["8"]
            
            # Primeira coluna
            elif(self.board["1"] == self.turn and self.board["4"] == self.turn and self.board["7"] == ""):
                self.board["7"] = self.reverse
            elif(self.board["7"] == self.turn and self.board["4"] == self.turn and self.board["1"] == ""):
                self.board["1"] = self.reverse
            elif(self.board["7"] == self.turn and self.board["1"] == self.turn and self.board["4"] == ""):
                self.board["4"] = self.reverse
            
            #segunda Linha
            elif(self.board["2"] == self.turn and self.board["5"] == self.turn and self.board["8"] == ""):
                self.board["8"] = self.reverse
            elif(self.board["2"] == self.turn and self.board["8"] == self.turn and self.board["5"] == ""):
                self.board["5"] = self.reverse
            elif(self.board["8"] == self.turn and self.board["5"] == self.turn and self.board["2"] == ""):
                self.board["2"] = self.reverse
            
            # Terceira linha
            elif(self.board["3"] == self.turn and self.board["6"] == self.turn and self.board["9"] == ""):
                self.board["9"] = self.reverse
            elif(self.board["3"] == self.turn and self.board["9"] == self.turn and self.board["6"] == ""):
                self.board["6"] = self.reverse
            elif(self.board["9"] == self.turn and self.board["6"] == self.turn and self.board["3"] == ""):
                self.board["3"] = self.reverse

            # \
            elif(self.board["7"] == self.turn and self.board["5"] == self.turn and self.board["3"] == ""):
                self.board["3"] = self.reverse
            elif(self.board["7"] == self.turn and self.board["3"] == self.turn and self.board["5"] == ""):
                self.board["5"] = self.reverse
            elif(self.board["5"] == self.turn and self.board["3"] == self.turn and self.board["7"] == ""):
                self.board["7"] = self.reverse
            
            # /
            elif(self.board["9"] == self.turn and self.board["5"] == self.turn and self.board["1"] == ""):
                self.board["1"] = self.reverse
            elif(self.board["9"] == self.turn and self.board["1"] == self.turn and self.board["5"] == ""):
                self.board["5"] = self.reverse
            elif(self.board["5"] == self.turn and self.board["1"] == self.turn and self.board["9"] == ""):
                self.board["9"] = self.reverse
            elif(self.board["5"] == ""):
                self.board["5"] = self.reverse
            else:
                other = random.randint(1,9)
                count = 0
                while(self.board[str(other)] != ""):
                    other = random.randint(1,9)
                    if(count == 20):
                        print("Empate!")
                        sys.exit(0)
                    else:
                        count += 1
                self.board[str(other)] = self.reverse
        
        def atacar(self):
            # Primeira Linda do Tabuleiro
            if(self.board["1"] == self.turn and self.board["2"] == self.turn and self.board["3"] == ""):
                self.board["3"] = self.reverse
                return self.board["3"]
            elif(self.board["1"] == self.turn and self.board["3"] == self.turn and self.board["2"] == ""):
                self.board["2"] = self.reverse
                return self.board["2"]
            elif(self.board["3"] == self.turn and self.board["2"] == self.turn and self.board["1"] == ""):
                self.board["1"] = self.reverse
                return self.board["1"]

            # Segunda linha
            elif(self.board["4"] == self.turn and self.board["5"] == self.turn and self.board["6"] == ""):
                self.board["6"] = self.reverse
                return self.board["6"]
            elif(self.board["4"] == self.turn and self.board["6"] == self.turn and self.board["5"] == ""):
                self.board["5"] = self.reverse
                return self.board["5"]
            elif(self.board["5"] == self.turn and self.board["6"] == self.turn and self.board["4"] == ""):
                self.board["4"] = self.reverse
                return self.board["4"]
            
            # Terceira Linha
            elif(self.board["7"] == self.turn and self.board["8"] == self.turn and self.board["9"] == ""):
                self.board["9"] = self.reverse
                return self.board["9"]
            elif(self.board["9"] == self.turn and self.board["8"] == self.turn and self.board["7"] == ""):
                self.board["7"] = self.reverse
                return self.board["7"]
            elif(self.board["7"] == self.turn and self.board["9"] == self.turn and self.board["8"] == ""):
                self.board["8"] = self.reverse
                return self.board["8"]
            
            # Primeira coluna
            elif(self.board["1"] == self.turn and self.board["4"] == self.turn and self.board["7"] == ""):
                self.board["7"] = self.reverse
            elif(self.board["7"] == self.turn and self.board["4"] == self.turn and self.board["1"] == ""):
                self.board["1"] = self.reverse
            elif(self.board["7"] == self.turn and self.board["1"] == self.turn and self.board["4"] == ""):
                self.board["4"] = self.reverse
            
            #segunda Linha
            elif(self.board["2"] == self.turn and self.board["5"] == self.turn and self.board["8"] == ""):
                self.board["8"] = self.reverse
            elif(self.board["2"] == self.turn and self.board["8"] == self.turn and self.board["5"] == ""):
                self.board["5"] = self.reverse
            elif(self.board["8"] == self.turn and self.board["5"] == self.turn and self.board["2"] == ""):
                self.board["2"] = self.reverse
            
            # Terceira linha
            elif(self.board["3"] == self.turn and self.board["6"] == self.turn and self.board["9"] == ""):
                self.board["9"] = self.reverse
            elif(self.board["3"] == self.turn and self.board["9"] == self.turn and self.board["6"] == ""):
                self.board["6"] = self.reverse
            elif(self.board["9"] == self.turn and self.board["6"] == self.turn and self.board["3"] == ""):
                self.board["3"] = self.reverse

            #Cruz
            elif(self.board["7"] == self.turn and self.board["5"] == self.turn and self.board["3"] == ""):
                self.board["3"] = self.reverse
            elif(self.board["7"] == self.turn and self.board["3"] == self.turn and self.board["5"] == ""):
                self.board["5"] = self.reverse
            elif(self.board["5"] == self.turn and self.board["3"] == self.turn and self.board["7"] == ""):
                self.board["7"] = self.reverse
            
            # Cruz
            elif(self.board["9"] == self.turn and self.board["5"] == self.turn and self.board["1"] == ""):
                self.board["1"] = self.reverse
            elif(self.board["9"] == self.turn and self.board["1"] == self.turn and self.board["5"] == ""):
                self.board["5"] = self.reverse
            elif(self.board["5"] == self.turn and self.board["1"] == self.turn and self.board["9"] == ""):
                self.board["9"] = self.reverse

            else:
                return False
            

# Função para jogar contra o computador
def onePlayer():
    turn = "X"

    # Precorendo as 5 jogadas possiveis
    for i in range(5):

        # Caso acontença um erro não programavel
        try: 

            # Nova Jogada
            print("Vez do " + turn + " Onde quer jogar?")
            move = input()

            # Caso o usuario faça uma jogada não existente
            while(move not in theBoard):
                print("Jogada invalida")
                print("Vez do " + turn + " Onde quer jogar?")
                move = input()

            # Caso o oponente joga uma casa ocupada
            while(theBoard[move] == "X" or theBoard[move] == "O"):
                print("Essa casa já foi ocupada")
                print("Vez do " + turn + " Onde quer jogar?")
                move = input()

                # Caso o usuario faça uma jogada não existente
                while(move not in theBoard):
                    print("Jogada invalida")
                    print("Vez do " + turn + " Onde quer jogar?")
                    move = input()
            theBoard[move] = turn

        # Caso acontença um erro não programavel
        except: 
            print("Exit[s/n]? ")
            exit = input()
            if("s" in exit):
                print("Bay, Bay!")
                sys.exit(1)
            else:
                continue
        
        # Verificar se um jogador ganhou
        if(ganhar(theBoard, turn)):
            return True
        
        

        maquinaDefender = Computador(theBoard, turn, "O")
        maquinaAtacar = Computador(theBoard, "O", "O")
        if(maquinaAtacar.atacar() == False):
            maquinaDefender.defender()
        
        if(ganhar(theBoard, "O")):
            return True
    
        # Controlando a Jogada
        """
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        """

        # Imprimindo o tabuleiro
        printBoard(theBoard)

# Função para 2 jogadores
def twoPlayer():
    turn = "X"

    # Precorendo as 9 jogadas possiveis
    for i in range(9):

        # Caso acontença um erro não programavel
        try: 

            # Nova Jogada
            print("Vez do " + turn + " Onde quer jogar?")
            move = input()

            # Caso o usuario faça uma jogada não existente
            while(move not in theBoard):
                print("Jogada invalida")
                print("Vez do " + turn + " Onde quer jogar?")
                move = input()

            # Caso o oponente joga uma casa ocupada
            while(theBoard[move] == "X" or theBoard[move] == "O"):
                print("Essa casa já foi ocupada")
                print("Vez do " + turn + " Onde quer jogar?")
                move = input()

                # Caso o usuario faça uma jogada não existente
                while(move not in theBoard):
                    print("Jogada invalida")
                    print("Vez do " + turn + " Onde quer jogar?")
                    move = input()
            theBoard[move] = turn

        # Caso acontença um erro não programavel
        except: 
            print("Exit[s/n]? ")
            exit = input()
            if("s" in exit):
                print("Bay, Bay!")
                sys.exit(1)
            else:
                continue
        
        # Verificar se um jogador ganhou
        if(ganhar(theBoard, turn)):
            return True
        
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        
        printBoard(theBoard)