class Guess:

    def __init__(self, word):

        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0
        self.currentStatus = '_' * len(word)


    def display(self):

        print('Current : ' + self.currentStatus)
        print('Tries : ' + str(self.numTries))

    def guess(self, guessedChar):
        self.guessedChars.append(guessedChar)
        if guessedChar not in self.secretWord:
            self.numTries += 1
            return  False
        else:
            result = ''
            for i in self.secretWord:
                if i in self.guessedChars:
                    result += i
                else:
                    result += '_'
            self.currentStatus = result

            return self.currentStatus == self.secretWord