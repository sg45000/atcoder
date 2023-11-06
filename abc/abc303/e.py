"""
星だった頂点の集合の中心点は、次数が3以上か2のどちらかである
次数3以上の頂点はTになっても確実に星の中心点といえる
次数3以上の頂点を調べれば全ての星の中心点がわかるので、その星の葉もわかる
星の構成頂点を全て抜いて残った頂点はレベル2の星だけなので、星の構成頂点数 3 で割れば、星の数を算出できる

"""

N = int(input())

deg = [0] * (N)
for _ in range(N - 1):
    u, v = list(map(int, input().split(" ")))
    deg[u - 1] += 1
    deg[v - 1] += 1


for i in range(N):
    if deg[i] == 1:
        s = i
        break

S = 0
ans = []
for i in range(N):
    if deg[i] >= 3:
        ans.append(deg[i])
        S += deg[i] + 1

for _ in range((N - S) // 3):
    ans.append(2)

print(*sorted(ans))