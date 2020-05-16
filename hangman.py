

import random


def hangman():
    word = random.choice(['love', 'motivation', 'hardwork', 'support', 'determination', 'positivity', 'mindset'])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''


    while(len(word) > 0):
        main = ''
        for letter in word:
            if(letter in guessmade):
                main = main + letter
            else:
                main = main + '_' + ''
        if(main == word):
            print(main)
            print('you win')
            break
        print('Guess the word: ', main)
        guess = input()


        if(guess in validLetters):
            guessmade = guessmade + guess
        else:
            print('enter a valid character')
            guess = input()

        if(guess not in word):
            turns = turns - 1
        if(turns == 9):
            print('9 turns left')
            print('--------------')
        if (turns == 8):
            print('8 turns left')
            print('--------------')
            print('    0     ')
        if (turns == 7):
            print('7 turns left')
            print('--------------')
            print('     0     ')
            print('     |     ')
        if (turns == 6):
            print('6 turns left')
            print('--------------')
            print('   \ 0     ')
            print('     |     ')
        if (turns == 5):
            print('5 turns left')
            print('--------------')
            print('   \ 0 /    ')
            print('     |     ')
        if (turns == 4):
            print('4 turns left')
            print('--------------')
            print('   \ 0 /    ')
            print('     |     ')
            print('    /      ')
        if (turns == 3):
            print('3 turns left')
            print('--------------')
            print('   \ 0 /    ')
            print('     |     ')
            print('    / \    ')
        if (turns == 2):
            print('2 turns left')
            print('--------------')
            print('   \ 0 /_    ')
            print('     |     ')
            print('    / \    ')
        if (turns == 1):
            print('1 turn left')
            print('--------------')
            print('   \ 0 /_|    ')
            print('     |     ')
            print('    / \    ')
        if (turns == 0):
            print('You lost')
            print('you killed a man!')
            print('--------------')
            print('     0_|   ')
            print('   / | \     ')
            print('    / \    ')
            break



name = input('whats your name?')
print('welcome, ', name)
print('-'*30)
print('try to guess the word in less than 10 attempts')
hangman()