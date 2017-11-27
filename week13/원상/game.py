from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    word = Word('words.txt')
    #guess에 랜덤단어 저장
    guess = Guess(word.randFromDB())

    finished = False

    hangman = Hangman()

    maxTries = hangman.getLife()

    while guess.numTries < maxTries:

        display = hangman.get(maxTries - guess.numTries)
        print(display)
        guess.display()


        guessedChar = input('Select a letter: ')
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        else:
            if guessedChar in numbers:
                print("Not numbers!")
                continue

        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue

        finished = guess.guess(guessedChar)
        if finished == True:
            break

    if finished == True:
        print('Success')
    else:
        print(hangman.get(0))
        print('word [' + guess.word + ']')
        print('guess [' , guess.strcurrent , ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()

