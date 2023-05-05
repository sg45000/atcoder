from functools import cmp_to_key

def cmp(a, b):
    if a[1] == b[1]:
        return b[0] - a[0]
    return a[1] - b[1]


n = int(input())

works = [list(map(int, input().split(" "))) for _ in range(n)]

works = sorted(works, key=cmp_to_key(cmp))

total_time = 0
answer = "Yes"
for i in range(n):
    time = works[i][0]
    expire = works[i][1]
    total_time += time
    if expire < total_time:
        answer = "No"
        break
print(answer)

