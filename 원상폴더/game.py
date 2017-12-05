from hangman import Hangman
from guess import Guess
from word import Word

def getChar():
    guessedChar = input('Select a letter: ')
    return guessedChar


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())
    hangman = Hangman()

    while hangman.remainingLives > 0:

        display = hangman.currentShape()
        print(display)
        display = guess.displayCurrent()
        print('Current: ' + display)
        display = guess.displayGuessed()
        print('Already Used: ' + display)

        success = guess.guess(getChar())
        if success == 1:
            continue
        elif success == 2:
            continue
        elif success == False:
            hangman.decreaseLife()
        
        if guess.finished():
            break

    if guess.finished() == True:
        print('**** ' + guess.displayCurrent() + ' ****')
        print('Success')
    else:
        print(hangman.currentShape())
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.displayCurrent() + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()
