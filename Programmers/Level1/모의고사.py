def solution(answers):
    answer = []
    first_answer = [1,2,3,4,5]
    first_answers = []
    first_cnt = 0
    second_answer = [2,1,2,3,2,4,2,5]
    second_answers = []
    second_cnt = 0
    third_answer = [3,3,1,1,2,2,4,4,5,5]
    third_answers = []
    third_cnt = 0
    for i in range(len(answers)):
        first_answers.append(first_answer[i % len(first_answer)])
        second_answers.append(second_answer[i % len(second_answer)])
        third_answers.append(third_answer[i % len(third_answer)])
        
    for i in range(len(answers)):
        if answers[i] == first_answers[i]:
            first_cnt += 1
        if answers[i] == second_answers[i]:
            second_cnt += 1
        if answers[i] == third_answers[i]:
            third_cnt += 1
    score = [first_cnt, second_cnt, third_cnt]
    highest = max(score)
    for i, cnt in enumerate(score):
        i += 1
        if cnt == highest:
            answer.append(i)
    return answer