N = int(input())
arr = []
string = ""
for n in str(N):
    arr.append(n)
arr = sorted(arr, reverse=True)
string = "".join(arr)
print(int(string))
