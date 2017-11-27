Week13 CodeReview
=

Roman to Dec
-

```python
def romanToDec(numStr):
    result = 0
    cnt = 0
    l = len(numStr)
    romans = {
        'M':1000, 'CM':900, 'D':500, 'CD':400,
        'C':100, 'XC':90, 'L':50, 'XL':40,
        'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}

    while l != 0:
        if numStr[:2] in romans and cnt == 0:
            result += romans[numStr[:2]]
            numStr = numStr[2:]
            l -= 2


        if l > 0:
            if numStr[0] in romans and cnt == 1:
                result += romans[numStr[0]]
                numStr = numStr[1:]
                cnt = 0
                l -= 1
        if cnt == 2:
            return "Error!"
        cnt += 1



    return str(result)
```



주석 대신 작성하는 코드 설명
#

반복문의 종료 조건 : 변환전 로마자들의 길이를 l이라고 저장 후 로마자가 숫자로 변환되어 사라질
때마다 l에서 줄어든 숫자만큼의 값을 빼 준다. l이 0이될 경우 종료

조건문

처음 numStr[:2]까지, 즉 두개짜리 로마자가 있는지 찾아본다. 없을 경우 cnt가 1증가한 후 다음 반복
그 다음 cnt가 1인경우, 2개짜리 로마자가 아닌 1개자리 로마자라는 가정하에 1개짜리 로마자를 찾아본다.
있으면 로마자를 지우고 숫자를 추가해 준다. 그 다음 cnt는 0으로 다시 초기화 해 준다.
만약 1개짜리도 없다면 존재하지 않는 로마자라는 뜻이므로 조건문은 성립하지 않고 cnt+=1
즉 cnt는 2가 된다. cnt가 2가 되는 경우는 올바르지 않은 문자가 있다는 것이므로 Error를 출력해 준다.

