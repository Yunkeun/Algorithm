n = int(input())
m = int(input())
friends = []
myFriends = set()
theirFriends = set()
for i in range(m):
    friends.append(list(map(int, input().split())))

for friend in friends:
    if friend[0] == 1:
        myFriends.add(friend[1])

for friend in friends:
    if friend[0] in myFriends and friend[1] not in myFriends and friend[1] != 1:
        theirFriends.add(friend[1])
    if friend[1] in myFriends and friend[0] not in myFriends and friend[0] != 1:
        theirFriends.add(friend[0])
print(len(theirFriends) + len(myFriends))
