def solution(s):
    answer = ''
    word_list = s.split(' ')
    for word in word_list:
        new_word = ''
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        answer += new_word + ' '
    return answer[:-1]