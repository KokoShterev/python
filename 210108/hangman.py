HANGMAN_PICS = [
    '''
    
    
    
    
    
    ''', '''
    +---+
        |
        |
        |
        |
       ===''', '''
    +---+
    |   |
        |
        |
        |
       ===''', '''
    +---+
    |   |
    O   |
        |
        |
       ===''', '''
    +---+
    |   |
    O   |
    |   |
        |
       ===''', '''
    +---+
    |   |
    O   |
   /|   |
        |
       ===''', '''
    +---+
    |   |
    O   |
   /|\\  |
        |
       ===''', '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
       ===''', '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
       ==='''
]

import random
import os

words = [
    'Пловдив', 'Габрово', 'Благоевград', 'Несебър', 'Казанлък', 'Карлово',
    'Калофер', 'Лясковец', 'Павликени', 'Сандански', 'Стамболийски',
    'Сунгурларе', 'Чепеларе', 'Якоруда', 'Черноморец', 'Чипровци', 'Силистра',
    'Търговище', 'Пазарджик', 'Кюстендил', 'Копривщица', 'Кърджали'
]
word_whole = words[random.randint(0, len(words) - 1)]
word = list(word_whole)
r1 = random.randint(0, len(word) - 1)
r2 = random.randint(0, len(word) - 1)
while word[r2] == word[r1]:
    r2 = random.randint(0, len(word) - 1)

for i in range(0, (len(word))):
    if word[i].lower() != word[r1].lower() and word[i].lower() != word[r2].lower():
        word[i] = '_'
wrong_guess = 0

while True:
    if '_' not in word:
        print(HANGMAN_PICS[wrong_guess])
        print('   You win!')
        break

    if wrong_guess < 8:
        print(HANGMAN_PICS[wrong_guess])
    else:
        print(HANGMAN_PICS[8])
        print('  You lose!')
        break

    print(' '.join(word))
    guess = input('Input your guess character: ')
    os.system('cls' if os.name == 'nt' else 'clear')

    if guess in word_whole.lower():
        for i in range(len(word)):
            if word_whole[i].lower() == guess:
                word[i] = word_whole[i]
    else:
        wrong_guess += 1
