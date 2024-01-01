"""
https://twitter.com/e869120/status/1402758934268571648/photo/1
全て黒になった状態から全て白に戻すと言い換えた時、
ボールiを白く塗り替えられる条件として、
(i = A or i = B) もしくは(AまたはBが白) が成立する

i = A or i = B のボールを探してそこからbfsやdfsで探索した結果全て探索できた場合は、全てを白に塗り替えることが可能
最後に問題を白から黒に塗り替えるに 戻すと、
先ほどの探索順を逆にしたものが、ボールを黒くする順番になる
"""

from collections import deque
N = int(input())


G = [[] for _ in range(N)]

visited = [False] * N
q = deque()

for i in range(N):
    a, b = list(map(int, input().split(" ")))
    a -= 1
    b -= 1

    if a == i or b == i:
        q.append(i)
        visited[i] = True
    G[a].append(i)
    G[b].append(i)

ans = []

while q:
    s = q.popleft()
    ans.append(s)

    for nex in G[s]:
        if visited[nex]:
            continue
        visited[nex] = True
        q.append(nex)

if not all(visited):
    print(-1)
    exit()

for a in reversed(ans):
    print(a + 1)
