N = int(input())
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

A = sorted(A)
B = sorted(B)

answer = 0
for a, b in zip(A, B):
    answer += abs(a - b)

print(answer)