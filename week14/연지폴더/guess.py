class Guess:

    def __init__(self, word):
        
        #사라진 변수: numTries
        self.secretWord = word
        self.currentStatus = '_' * len(word)
        #e랑 n은 알려주고 시작. (집합)
        self.guessedChars = {'e', 'n'}

        #객체 생성과 동시에 guess함수 실행 ?
        self.guess('')


    def guess(self, character):
        #합집합
        #이미 game에서 제시된 문자인지는 확인함.

        #if character.isalpha() != True:
        #    print("알파벳만 입력해 주세요")
        #    return '흥'

        #else:
        self.guessedChars |= {character}
        if character not in self.secretWord:
            return False

        else:
            currentStatus = ''
            #c는 알파벳 하나하나..
            for c in self.secretWord:
                if c in self.guessedChars:
                    currentStatus += c
                else:
                    currentStatus += '_'

            self.currentStatus = currentStatus

            return True


    def finished(self):
        if self.currentStatus == self.secretWord:
            return True
        else:
            return False


    def displayCurrent(self):

        guessWord = ''
        for c in self.currentStatus:
            guessWord += (c + ' ')
        return guessWord


    def displayGuessed(self):

        guessed = ''
        for c in sorted(list(self.guessedChars)):
            guessed += (c + ' ')
        return guessed
