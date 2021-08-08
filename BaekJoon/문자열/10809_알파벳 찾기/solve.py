word = input()
# 97: 'a' 123 : 'z'
alphabet = list(range(97,123))

for x in alphabet :
    print(word.find(chr(x))) 

# chr() : 아스키코드 -> 문자로 변환
# ord() : 문자 -> 아스키코드 변환
# find() : 문자열 안에서 chr 함수로 변환된 문자가 있는지 찾는 함수