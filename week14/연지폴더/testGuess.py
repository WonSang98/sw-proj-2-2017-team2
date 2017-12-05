import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        #일단 default라는 단어가지고 실험할 것임..
        #(추가)다른 단어로도 해보자..
        self.g1 = Guess('default')
        #(추가)같은알파벳이 두개이상 들어있는 단어
        self.g2 = Guess('anaconda') 
    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        #1.처음 상태에서 e를 알려주었나?
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        #2.있는 문자를 입력했을때 반영을 하나?
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        
        #3.(추가)없는 문자를 입력했을때 제대로 되나?
        self.g1.guess('x')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

        
        #4.(추가)잘못 입력을 했을때 무시하나?
        self.g1.guess('!')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')        
        #5.(추가)빈 문자를 입력했을때 무시하나?
        self.g1.guess(' ')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

        #(추가) 다른 단어
        self.assertEqual(self.g2.displayCurrent(), '_ n _ _ _ n _ _ ')        
        self.g2.guess('a')
        self.assertEqual(self.g2.displayCurrent(), 'a n a _ _ n _ a ')

        

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        #근데.. 알파벳이 아닌건 애초에 guess함수에 인자로 못넣게 되어있어서..
        #알파벳이 아닌 입력을 거르는 코드는 guess안에 써야 이 테스트가 유효한가
        #(추가)잘못된 걸 입력했을때 추가가 안되냐?
        #self.g1.guess('!')
        #self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        #(추가)빈문자 입력했을때 추가 안되냐?
        #self.g1.guess(' ')
        #self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        

if __name__ == '__main__':
    unittest.main()
