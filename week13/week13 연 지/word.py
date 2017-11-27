import random

class Word:

    def __init__(self, filename):

        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            #오른쪽에있는 개행문자 제거 
            word = line.rstrip()
            #파일에 있는 단어를 리스트에넣으면서 세어줌
            self.words.append(word)
            self.count += 1

        print('%d words in DB' % self.count)


    def test(self):
        return 'default'

    #임의의 단어를 리턴하는 함수.
    def randFromDB(self):
        #0~count-1 사이의 정수 리턴
        r = random.randrange(self.count)
        return self.words[r]

#class Word설명
#1.생성자 : 파일명을 받으면. 그 파일에있는 단어를 모두 리스트 words에 담음
#2.randFromDB() : 임의의 단어를 리턴함
