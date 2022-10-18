import os
import random

types = ["Animal", "País", "Cor", "Marca de Carro", "Marca de Moto", "Marca de Roupa", "Móvel"]


class Hangman:
    def __init__(self):
        """
        Inicia os parâmetros do objeto.
        """
        type = random.choice(types)
        words = open(f"{type}.txt", "r").read().lower().split("; ")
        self.loop = True
        self.type = type
        self.__secretWord = random.choice(words)
        self.rightAnswer = []
        self.wrongAnswer = []
        self.acentuacao = False
        self.stickman = (""" +---------+
 | 
 | 
 | 
 | 
 | 
/|\\""", """ +---------+
 |         |
 | 
 | 
 | 
 | 
/|\\""", """ +---------+
 |         |
 |         O
 | 
 | 
 | 
/|\\""", """ +---------+
 |         |
 |         O
 |        / 
 |        
 | 
/|\\""", """ +---------+
 |         |
 |         O
 |        /|
 |        
 |
/|\\""", """ +---------+
 |         |
 |         O
 |        /|\\
 |        
 | 
/|\\""", """ +---------+
 |         |
 |         O
 |        /|\\
 |        /
 | 
/|\\""", """ +---------+
 |         |
 |         O
 |        /|\\
 |        / \\
 | 
/|\\""")

    def displayGame(self):
        """
        Constrói a tela do jogo.
        """
        os.system('cls')
        title = "Jogo da Forca"
        print("-" * (len(title) + 4))
        print(f"  {title}")
        print("-" * (len(title) + 4))
        print()
        print(f"Dica: {self.type}")
        print()
        print(self.stickman[len(self.wrongAnswer)], end=" ")
        self.blanks = ""
        for x in self.__secretWord:
            if x in "-.()+*%'?ªº/\\°₢&@":
                self.blanks = self.blanks + x
            elif x == " ":
                self.blanks = self.blanks + x
            elif x in self.rightAnswer:
                self.blanks = self.blanks + x
            else:
                self.blanks = self.blanks + "_"
        for x in self.blanks.capitalize():
            print(x, end=" ")
        print()
        print("\nLetras erradas:", end=" ")
        for x in self.wrongAnswer:
            print(x, end=" ")
        print("\n")

    def checkGameStatus(self):
        """
        Confere início e fim do jogo.
        """
        if len(self.wrongAnswer) == 7:
            print(f"Você perdeu!\nA palavra era {self.__secretWord.capitalize()}\n")
            self.loop = False
        elif "_" not in self.blanks:
            print("Você ganhou!")
            self.loop = False

    def checkLetter(self, ans):
        """
        Confere acentuação, insere valor à lista de letras corretas, retorna ans e impede que ans seja inserido nas letras erradas.
        :param ans: valor de entrada de tentativa.
        :return:
        """
        for x in self.__secretWord:
            if x in "áàâãä" and ans in "a":
                self.rightAnswer.append(x)
                self.acentuacao = True
            elif x in "éèêë" and ans == "e":
                self.rightAnswer.append(x)
                self.acentuacao = True
            elif x in "íìîï" and ans == "i":
                self.rightAnswer.append(x)
                self.acentuacao = True
            elif x in "óòôõö" and ans == "o":
                self.rightAnswer.append(x)
                self.acentuacao = True
            elif x in "úùûü" and ans == "u":
                self.rightAnswer.append(x)
                self.acentuacao = True
            elif x in "ç" and ans == "c":
                self.rightAnswer.append(x)
                self.acentuacao = True
        return ans

    def gameInit(self):
        """
        Faz chamada para iniciar o jogo e fazer a chamada de outras funções e métodos.
        :return:
        """
        while True:
            self.displayGame()
            self.checkGameStatus()
            if not self.loop:
                break
            while True:
                try:
                    ans = self.checkLetter(input("Insira uma letra ou um número: ")[0].lower())
                except:
                    ans = ""
                if ans.isalnum():
                    break
                else:
                    print("\nPrecisa ser uma letra ou um número.\n")
            if ans in self.rightAnswer or ans in self.wrongAnswer:
                continue
            if ans in self.__secretWord:
                self.rightAnswer.append(ans)
            elif self.acentuacao:
                self.acentuacao = False
                continue
            else:
                self.wrongAnswer.append(ans)


while True:
    game = Hangman()
    game.gameInit()
    if input("Continuar? [S/N]\n").strip().upper() == "N":
        break
    else:
        del game
