N = int(input())  # 駅の数
D = list(map(int, input().split(" ")))  # 駅間の距離
V = list(map(int, input().split(" ")))  # 経由駅番号

fd = [0]
for d in D:
    fd.append(fd[-1] + d)

s = 0
ans = 0
for v in V:
    ans += fd[v - 1] - fd[s]

print(ans)
