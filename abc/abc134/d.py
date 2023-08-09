"""
パリティの問題
iが大きい箱からボールを入れるか決めていけば答えがわかる
"""

N = int(input())
A = list(map(int, input().split(" ")))

memo = [0] * (N + 1)
for i, a in zip(reversed(range(1, N + 1)), reversed(A)):
    count = 0
    mul = 2
    while i * mul <= N:
        count += memo[i * mul]
        mul += 1
    
    if count % 2 ^ a == 0:
        memo[i] = 0
    else:
        memo[i] = 1

answer = []
for i, a in enumerate(memo[1:]):
    if a == 1:
        answer.append(i + 1)
print(len(answer))
print(" ".join(map(str, answer)))