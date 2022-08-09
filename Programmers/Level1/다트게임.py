def solution(dartResult):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    bonus = ['S', 'D', 'T']
    option = ['*', '#']
    calculate = []
    order = 0
    for i in range(len(dartResult)):
        if i != 0 and dartResult[i-1] in num and dartResult[i] == '0':
            continue
        if dartResult[i] in num:
            order += 1
            addNumber(dartResult[i], dartResult[i+1], calculate)
        if dartResult[i] in bonus:
            isBonus(dartResult[i], calculate)
        if dartResult[i] in option:
            isOption(dartResult[i], order, calculate)
    return sum(calculate)

def addNumber(currentResult, nextResult, calculate):
    if nextResult == '0':
        calculate.append(10)
    else:
        calculate.append(int(currentResult))
        
def isBonus(currentResult, calculate):
    if currentResult == 'D':
        calculate[-1] *= calculate[-1]
    if currentResult == 'T':
        calculate[-1] *= calculate[-1] * calculate[-1]
        
def isOption(currentResult, order, calculate):
    if order == 1:
        if currentResult == '*':
            calculate[0] *= 2
        else:
            calculate[0] *= -1
    if order != 1:
        if currentResult == '*':
            calculate[order-1] *= 2
            calculate[order-2] *= 2
        else:
            calculate[order-1] *= -1