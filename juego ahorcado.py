# -*- coding: utf-8 -*-
import random

IMAGES = ['''
        +---+
        |   |
            |
            |
            |
            |
            =======''', '''
        
        +---+
        |   |
        O   |
            |
            |
            |
            =======''', '''
        
        +---+
        |   |
        O   |
        |   |
            |
            |
            =======''', '''

        +---+
        |   |
        O   |
       /|   |
            |
            |
            =======''', '''

        +---+
        |   |
        O   |
       /|\  |
            |
            |
            =======''', '''


        +---+
        |   |
        O   |
       /|\  |
        |   |
            |
            =======''', '''

        +---+
        |   |
        O   |
       /|\  |
        |   |
       /    |
            =======''', '''

        +---+
        |   |
        O   |
       /|\  |
        |   |
       / \  |
            =======''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'rosa',
    'amor',
    'torre'
]

def random_word():
    idx = random.randint(0, len(WORDS) - 1)  
    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * ---') 

def run():
    word = random_word() 
    hidden_word = ['-'] * len(word)  #Usamos una palabra escondida.
    tries = 0                        # Va guardar cuantas veces hemos tenido errores.

    while True:                              # : significa infinita.
        display_board(hidden_word, tries)    # Mostrar el tablero. Recive dos paraametros.
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)
        
        if len(letter_indexes) == 0:
            tries += 1
        
            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('Perdistes! La palabra correcta era {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('Felicidades! Ganaste. La palabra es: {}'.format(word))
            break

if __name__ == "__main__":
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()