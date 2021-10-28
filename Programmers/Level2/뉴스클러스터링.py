from collections import Counter

def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str1_arr = []
    str2 = str2.upper()
    str2_arr = []
    arr1 = []
    arr2 = []
    
    twoChr = ""
    for i, c in enumerate(str1):
        if i == len(str1)-1:
            break
        twoChr = c + str1[i+1]
        str1_arr.append(twoChr)
    for i, c in enumerate(str2):
        if i == len(str2)-1:
            break
        twoChr = c + str2[i+1]
        str2_arr.append(twoChr)
    for x in str1_arr:
        if x.isalpha() == True:
            arr1.append(x)
    for x in str2_arr:
        if x.isalpha() == True:
            arr2.append(x)
    Counter1 = Counter(arr1)
    Counter2 = Counter(arr2)
    intersection = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    if len(union) == 0:
        answer = 65536
    else:
        answer = int(len(intersection) / len(union) * 65536)
    return answer