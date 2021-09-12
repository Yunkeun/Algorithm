str = input().upper()
# 중복 제거하기 위해 set 후 list화
unique_str = list(set(str))

cnt_list = []
for chr in unique_str :
    cnt = str.count(chr)
    # count 숫자를 리스트에 append
    cnt_list.append(cnt)
    
# count 숫자 최대값이 중복되면 ? 출력
if cnt_list.count(max(cnt_list)) > 1 : 
    print('?')
# count 숫자 최대인 chr 출력
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_str[max_index])