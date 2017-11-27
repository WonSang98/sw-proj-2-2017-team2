class Guess:

    def __init__(self, word):
        self.word = word
        #추측에 사용된 글자들의 집합
        self.guessedChars = []
        #실패한 추측의 회수를 기록하기 위한 변수
        self.numTries = 0
        #현재 맞춘상황을 리스트에 문자열 하나씩 저장, 리스트인이유는 변경을위해
        self.current = ["_"]*len(self.word)
        #보기좋게 하기위한 리스트를 순서대로 이어붙인 str현재상황
        self.strcurrent = "_"*len(self.word)


    def display(self):
        print("Current :", self.strcurrent)
        print("")
        print("Tries: ", self.numTries)


    def guess(self, character):
        cnt = 0
        self.strcurrent = ""
        self.guessedChars.append(character)
        #랜덤단어의 처음부터 끝까지 돌아가며 주어받은 문자열이 있을경우 '_'과 바꿈
        for i in range(len(self.word)):
            if self.word[i] == character:
                cnt += 1
                self.current[i] = character
            self.strcurrent += self.current[i]

        if cnt == 0:
            self.numTries += 1

        if self.word == self.strcurrent:
            return True
        else:
            return False