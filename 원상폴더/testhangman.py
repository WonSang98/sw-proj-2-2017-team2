import unittest

from hangman import Hangman

class TestGuess(unittest.TestCase):
    def setUp(self):
        self.h1 = Hangman()
        self.h2 = Hangman()

    def tearDown(self):
        pass


    #생성자확인
    def testConstruct(self):
        self.assertEqual(self.h1.remainingLives, 6)

    def testDecreaseLife(self):
        test_life = 6
        #일부러 기존횟수보다 오버해서 테스트, indexOutLange 상황가정
        #remainingLive가 0미만이 되지않도록 수정했음
        for i in range(10):
            self.assertEqual(self.h1.remainingLives, test_life)
            self.assertEqual(self.h1.currentShape(), Hangman.text[test_life])
            self.h1.decreaseLife()

            if test_life > 0:
                test_life -= 1



if __name__ == '__main__':
    unittest.main()

