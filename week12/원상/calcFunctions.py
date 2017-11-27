from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n >= 4000:
        return 'Error!'
    romans = {
        1000:'M', 900:'CM', 500:'D', 400:'CD',
        100:'C', 90:'XC', 50:'L', 40:'XL',
        10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'
    }
    result = ""
    for value in sorted(romans.keys(), reverse=True):
        while n >= value:
            result += romans[value]
            n -= value

    return result

    return 'dec -> Roman'

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
