N = int(input())
rope_info = []
value = []
for x in range(N):
    rope_info.append(int(input()))
rope_info.sort(reverse=True)
for i in range(N):
    value.append(rope_info[i]*(i+1))
print(max(value))