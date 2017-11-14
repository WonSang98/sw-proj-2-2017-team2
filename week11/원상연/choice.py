from calcFunctions import *
from keypad import functionList

def choice(key, n):
    if key == functionList[0]:
        return factorial(n)

    elif key == functionList[1]:
        return decToBin(n)

    elif key == functionList[2]:
        return binToDec(n)

    elif key == functionList[3]:
        return decToRoman(n)
