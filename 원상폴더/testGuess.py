import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Guess('test')

    def tearDown(self):
        pass
    #생성자가 잘 작동되나 확인

    def testConstruct(self):
        self.assertEqual(self.g2.secretWord, 'test')
        self.assertEqual(self.g2.currentStatus, '_e__')
        self.assertEqual(self.g2.guessedChars, {'', 'e', 'n'})

    #guess함수 확인, False 와 True리턴값 확인
    def testGuess(self):
        self.assertEqual(self.g1.guess('q'), False)
        self.assertEqual(self.g1.guessedChars, {'', 'q', 'e', 'n'})
        self.assertEqual(self.g1.guess('D'), True)
        self.assertEqual(self.g1.currentStatus, 'de_____')


    #정답을 맞췄을 때와 아닐 때 리턴값확인
    def testFinished(self):
        word_list = ['d', 'a', 'f', 'a', 'u', 'l', 't']
        self.assertEqual(self.g1.finished(), False)
        for w in word_list:
            self.g1.guess(w)
        self.assertEqual(self.g1.finished(), True)





    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        #없는 문자 추가되었을 때
        self.g1.guess('q')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        #중복된 문자추가
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        #len(charater) > 1인 문자
        self.g1.guess('aa')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        #이 경우 에러가발생해서 guess함수내에서 character판단하도록함
        #그런데 이 에러는 guess함수 문제라 testGuess에서 해야할까?

if __name__ == '__main__':
    unittest.main()