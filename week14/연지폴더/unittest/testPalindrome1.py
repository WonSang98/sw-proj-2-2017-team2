import unittest

from palindrome import Palindrome

class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.p1 = Palindrome('abcd')
        #p1은 abcd를 인자로 받아 생성된 Palindrome의 오브젝트
        self.p2 = Palindrome('abcdedcba')
    
    def tearDown(self):
        pass
    
    def testNormal(self):
        self.assertFalse(self.p1.normal())
        #p1으로 normal함수 실행 -> 팰린드롬이면 true,아니면 false리턴 할것임
        #근데 abcd는 false를 출력해야해.
        self.assertTrue(self.p2.normal())

if __name__ == '__main__':
    unittest.main()
