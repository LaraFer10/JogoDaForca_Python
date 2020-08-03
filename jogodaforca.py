# Hangman Game (Jogo da Forca)
#encoding: utf-8

# Imports
import random
from unidecode import unidecode

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman():

    trice = ""
    hits = 0
    errors = 0
    # Método Construtor
    def __init__(self, word):
        self.word = word
    # Método para adivinhar a letra
    def guess(self, letter):
        sub = self.trice.split()
        cont = 0
        final = ''
        hits = 0
        word = unidecode(self.word)
        for char in word:
            if char.count(letter) == 1:
                sub[cont] = char
                hits += 1
            final += sub[cont] + ' '
            cont += 1
        self.trice = final
        if hits > 0:
            self.hits += 1
        else:
            self.errors += 1
    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if self.hits == len(self.word) or self.errors == 6:
            return False
        else:
            return True
    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if self.hits == len(self.word):
            return True
        else:
            return False
    # Método para não mostrar a letra no board
    def hide_word(self):
        for iten in self.word:
            self.trice += '_ '

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self, board):
        return board[self.errors]


def secret_word():
    archive = []
    for iten in open('palavras.txt', 'r'):
        archive.append(iten)
    return archive[random.randint(0, len(archive))].strip()

def main():

    game = Hangman(secret_word())
    game.hide_word()
    wrong_letter = []
    right_letter = []
    while game.hangman_over():
        print(game.print_game_status(board))
        print("Palavra: %s" %(game.trice))
        print("Letras erradas:")
        for iten in wrong_letter:
            print(iten)
        print("Letras certas:")
        for iten in right_letter:
            print(iten)
        letter = input('Digite a letra:')
        game.guess(letter)
        if game.hits > game.errors:
            print("Valor da acertos %r" %(game.hits))
            right_letter.append(letter)
        else:
            print("Valor da erros %r" % (game.errors))
            wrong_letter.append(letter)
    print(game.print_game_status(board))
    print("Palavra: %s" % (game.trice))
    print("Letras erradas:")
    for iten in wrong_letter:
        print(iten)
    print("Letras certas:")
    for iten in right_letter:
        print(iten)
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')

main()