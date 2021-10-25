import sys

N = int(sys.stdin.readline())   # input()보다 약 10배 빠르다.
words = []

for i in range(N):
    words.append(sys.stdin.readline().strip())
words = set(words) # 중복 제거
words = sorted(words)   # 사전순
words = sorted(words, key=len) # 길이순
for word in words:
    print(word)