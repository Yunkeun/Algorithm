N = int(input())
words = dict()
for i in range(N):
    words.update({input():i})
for word in words.keys():
    words[word] = len(word)
alphaSorted_words = dict(sorted(words.items()))
sorted_words = sorted(alphaSorted_words.items(), key = lambda item: item[1])

for word in sorted_words:
    print(word[0])