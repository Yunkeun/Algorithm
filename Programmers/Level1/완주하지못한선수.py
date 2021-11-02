# 나의 풀이 - 테스트2,3 시간초과 발생
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for x in participant:
        if x not in completion:
            answer = x
            return answer
        else:
            completion.remove(x)
    
    return answer



# collection 모듈
# 컨테이너에 들어있는 요소의 갯수를 파악해 딕셔너리 형태로 변환하는 객체 ( {'자료 이름' : '개수'} 형식 )
# hash형 자료들의 값의 개수를 셀 때 사용
# Counter() 객체끼리의 뺄셈도 가능
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0] # 리스트 형태로 변환


# zip 함수
# Python 내장 함수
# 같은 인덱스끼리 짝 지어줌 (배열의 길이가 다를 경우 남는 인덱스는 zip 객체에서 제외)
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]