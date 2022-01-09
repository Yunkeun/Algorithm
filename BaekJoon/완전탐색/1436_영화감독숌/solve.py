N = int(input())
first_movie = 666
new_movie = 666
count = 0
while True:
    if str(first_movie) in str(new_movie):
        N -= 1
        count += 1
    if N == 0:
        break
    new_movie += 1
print(new_movie)