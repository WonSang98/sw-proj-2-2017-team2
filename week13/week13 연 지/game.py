from hangman import Hangman
from guess import Guess
from word import Word

#메인함수
def gameMain():
    #Word클래스로 만든 오브젝트 
    word = Word('words.txt')
    #guess 는 랜덤 단어로 만든 Guess의 오브젝트
    guess = Guess(word.randFromDB())
    #
    finished = False
    #Hangman의 오브젝트 만들어서 남은생명
    hangman = Hangman()
    #남은생명==리스트 아이템 개수
    maxTries = hangman.getLife()

    #아마 numtries는 실행횟수 일듯@@@@@@@@@
    #실행횟수 < 남은생명 일때.. loop
    while guess.numTries < maxTries:
        #현재 행맨의 모습..
        display = hangman.get(maxTries - guess.numTries)
        print(display)

        #현재까지의 상황출력 (맞춘글자, 실패횟수)
        guess.display()
        #알파벳 제시!
        guessedChar = input('Select a letter: ')
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        #guseedChars는 내가 이미 제시한 알파벳들의 리스트 일듯.
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue
        #guess()는 해당 알파벳이 단어안에 있으면 위치를기록.
        #없으면 실패횟수를 증가시킴
        #모든글자를 다 맞추었으면 True 아니면 False.
        finished = guess.guess(guessedChar)
        if finished == True:
            break

    if finished == True:
        print('Success')
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.currentStatus + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()
