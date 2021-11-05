def solution(nums):
    answer = 0
    catch = []
    for p in nums:
        if p in catch:
            continue
        else:
            if answer >= len(nums)//2:
                break
            catch.append(p)
            answer += 1
    return answer