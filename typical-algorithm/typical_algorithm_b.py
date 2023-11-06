# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_b

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort(key=lambda x: x[1])
ans = 0
t = 0  # 前回消化したタスクの終了時間
for i in range(N):
    a, b = AB[i]
    if t < a:
        ans += 1
        t = b
    
print(ans)