from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'error'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'error'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'error'
    return r

def decToRoman(n):
    try:
        #정수 아닌거 거르고
        n = int(n)
    except:
        return 'error'
    #양의정수 아니거나 4000넘는 수 거르고
    if n <= 0 or n >= 4000:
        return 'error'
    result = ''

    #그냥 for value in romans.keys(): 하면 키들의 순서가 뒤죽박죽이라 안돼에
    #romans.keys()는 키값들의 리스트, 그걸 역순으로 정렬한것
    for value in sorted(romans.keys(), reverse=True):
        while n >= value:
            result += romans[value]
            n -= value
    return result
def romanToDec(n):
    ro = n
    result = 0
    #더해지는 value들을 리스트에 차곡차곡 쌓자
    valuelist = []
    valuecount = {}
    #위에랑 포문 똑같음
    for value in sorted(romans.keys(), reverse=True):
        #value바뀔때마다 count 0으로 초기화
        count = 0
        #키값(로마문자)이 스트링의 제일 처음에 있으면 계속 while loop돌림
        while ro.find(romans[value]) == 0:
            length = len(romans[value])
            ro = ro[length:]
            valuelist.append(value)
            result += value
            
    #4,5,9 는 총 한번만 나올수있고.. 40,50,90 도 마찬가지.        
    count_459 = 0 #4,5,9 세기
    count_4590 = 0 # 40,50,90 세기
    count_45900 = 0 # 400, 500, 900 세기

    #value들이 몇번씩 더해졌는지 세자
    for value in valuelist:
        if value in valuecount:
            valuecount[value] += 1
        else:
            valuecount[value] = 1
            
    for value,count in valuecount.items():
        #얘네는 4번이상 나오면 에러.. (ex. IIII)
        if value in [1, 10, 100, 1000] and count >= 4:
            return 'error'
            break
        
        elif value in [4, 5, 9]:
            count_459 += count
        elif value in [40, 50, 90]:
            count_4590 += count
        elif value in [400, 500, 900]:
            count_45900 += count
            
    #셋중에 하나라도 2 이상이면 에러.
    if count_459 >= 2 or count_4590 >= 2 or count_45900 >= 2:
        return 'error'
    #위의경우 말고 같은자리수가 중복으로 나온것도 에러 ex.IVI
    elif valuecount[1] != 0 and count_459 != 0:
        return 'error'
    elif valuecount[10] != 0 and count_4590 != 0:
        return 'error'
    elif valuecount[100] != 0 and count_45900 != 0:
        return 'error'
    
    #어떤 멍청이가 로마문자를 작은자리수부터 쓰면 (ex. IVXX )
    #XX는 for문에 걸리지도 않고 끝남. 이런경우 에러처리.
    elif ro != '':
        return 'error'
    else:
        return str(result)

romans = {
   1000: 'M', 900:'CM', 500: 'D', 400: 'CD',
   100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
   10: 'X', 9:'IX', 5:'V', 4:'IV', 1:'I'
}

    
        
numPadList = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=',
    ]

operatorList = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C',
]

constantList = [
    'pi',
    '빛의 이동 속도 (m/s)',
    '소리의 이동 속도 (m/s)',
    '태양과의 평균 거리 (km)',
]

functionList = [
    'factorial (!)',
    '-> binary',
    'binary -> dec',
    '-> roman',
]



#def romanToDec(n):

print(romanToDec("XXIVI"))

#9 ,5, 4 ... 90,50,40 ... 900,500,400 도 연달아 쓰면안됑..ㅜㅠ
#다더하고 났는데 ro가 ''가 아니면 에러(순서잘못된 로마문자)
