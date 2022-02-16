inputString = input()
splittedString = inputString.split(" ")
nullCount = 0
for word in splittedString:
    if word == "":
        nullCount += 1

print(len(splittedString) - nullCount)