N, M = map(int, input().split(" "))
list = list(map(int, input().split(" ")))
len_list = len(list)
answer_list = []
for i in range(len_list):
    for j in range(i+1, len_list):
        for k in range(j+1, len_list):
            sum = list[i]+list[j]+list[k]
            if sum <= M:
                answer_list.append(sum)
print(max(answer_list)) 
