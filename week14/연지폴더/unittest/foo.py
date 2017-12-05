import unittest
 
#unittest라는 모듈에 TestCase라는 클래스가 있는것 같음.. 얘를 상속받아 만든 클래스
class TestStringMethods(unittest.TestCase):

    #TestCase라는 클래스에 assert뭐시기 라는 함수들이 있음
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        #a와 b가 같으면 테스트 통과
    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        #FOO가 대문자 이면 테스트 통과.
        self.assertFalse('Foo'.isupper())
    
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

if __name__ == '__main__':
    unittest.main()
    #단위테스트를 실행하게함
    #Ran 3 tests in 0.008s;  OK; 이렇게 두줄이 뜸.

    #실행 코드없이 커맨드 라인에서 단위테스트를 하고싶으면
    #python -m unittest -v 파이썬코드이름 '' 을 입력하면 됨
    #여기서 -v 는 더욱 자세히 출력하기 위한 옵션
    #test_isupper(foo..) ..OK
    #test_split ... OK
    #test_upper .. OK 이런식으로 함수하나하나 확인하고 출력해줌

    #주의! 테스트할 함수들이 있는 클래스 이름은 Test로 시작해야함!
    #아니다..함수이름이 test로 시작해야하는 거였나..?:3


