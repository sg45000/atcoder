"""
N個の頂点がM本の有効辺によって有向グラフを形作っていると捉えられる
全ての頂点が一直線になっていればYes
一直線になっていなければNo

スタートかゴールの頂点がわかればDFSで解けるんだが、、、
1の可能性がある頂点をバケットで探る
有効辺の先の頂点は1の可能性がない
"""
import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)


N, M = list(map(int, input().split(" ")))

into_num = [0] * N

G = [[] for _ in range(N)]

for _ in range(M):
    X, Y = list(map(int, input().split(" ")))
    G[X - 1].append(Y - 1)
    into_num[Y - 1] += 1



def topological_sort(V, G, into_num):
    #入ってくる有向辺を持たないノードを列挙
    q = deque()
    #V: 頂点数
    for i in range(V):
        if into_num[i] == 0:
            q.append(i)
    
    #以下、幅優先探索
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for adj in G[v]:
            into_num[adj] -= 1 #入次数を減らす
            if into_num[adj] == 0:
                q.append(adj) #入次数が0になったら、キューに入れる
    
    return ans

ans = topological_sort(N, G, into_num)

for i in range(N - 1):
    if ans[i + 1] not in G[ans[i]]:
        print("No")
        exit()


answer = [0] * N

for i in range(N):
    answer[ans[i]] = str(i + 1)

print("Yes")
print(" ".join(answer))