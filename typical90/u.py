from collections import deque
import sys
 
sys.setrecursionlimit(1 << 30)
 

#---------------------------------------
# 入力の処理とグラフの作成
#---------------------------------------
N, M = list(map(int, input().split(" ")))
AB = [list(map(int, input().split(" "))) for _ in range(M)]

G = [set() for _ in range(N + 1)]
R = [set() for _ in range(N + 1)]

for a, b in AB:
    G[a].add(b)
    R[b].add(a)

# print(G)
# print(R)

#-----------------------------------------------
# 各nodeからDFSして帰りがけ順にnodeを返す関数
#-----------------------------------------------
def postorder_traversal():
    seen = [-1] * (N + 1)
    postorder = []

    def dfs(s):
        seen[s] = 1
        for nex in G[s]:
            if seen[nex] < 0:
                dfs(nex)
        postorder.append(s)

    for n in range(1, N+1):
        if seen[n] < 0:
            dfs(n)
    return reversed(postorder)

#-----------------------------------------------
# 強連結成分分解(SCC)で分解されたグループを返す関数
#-----------------------------------------------
def scc(v, seen):
    group = []

    def dfs(v, seen):
        group.append(v)
        seen[v] = 1
        for nex in R[v]:
            if seen[nex] < 0:
                dfs(nex, seen)

    dfs(v, seen)
    return group

#--------------------------------------------------
# メイン処理
#--------------------------------------------------
groups = []
seen = [-1] * (N + 1)
postorder = postorder_traversal()
# print(postorder)
for n in postorder:
    if seen[n] < 0:
        groups.append(scc(n, seen))

print(int(sum([len(g) * (len(g) - 1) / 2 for g in groups])))