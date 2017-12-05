from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())
    hangman = Hangman()
    #사라진 변수:finished, maxTries

    #guess클래스에 있던 numTries없애고 hangman클래스에 remainingLives만듬
    while hangman.remainingLives > 0:

        display = hangman.currentShape()
        print(display)
        display = guess.displayCurrent()
        print('Current: ' + display)
        display = guess.displayGuessed()
        print('Already Used: ' + display)

        guessedChar = input('Select a letter: ')
        guessedChar = guessedChar.lower()##
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        if guessedChar.isalpha() != True:##
            print('알파벳만 입력해 주세요')
            continue
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue

        success = guess.guess(guessedChar)
        if success == False:
            #guess에서 목숨관리 안하고 행맨에서 목숨관리
            hangman.decreaseLife()

        #game에서 finished라는 변수를 없앤 대신 guess에 finished() 함수 만듬
        #단어가 완성되면 true리턴..
        if guess.finished():
            break

    if guess.finished() == True:
        #짝짝짝
        print('**** ' + guess.displayCurrent() + ' ****')
        print('Success')
    else:
        print(hangman.currentShape())
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.displayCurrent() + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()
