
from collections import defaultdict


N = int(input())
AB = [list(map(int, input().split(" "))) for _ in range(N - 1)]
Q = int(input())
KV = [list(map(int, input().split(" "))) for _ in range(Q)]

G = defaultdict(list)
for a, b in AB:
    G[a].append(b)
    G[b].append(a)
    

def dfs(root, parent, nodes):
    result = 0
    for child in G[root]:
        if child == parent:
            continue
        child_value = dfs(child, root)
        result += child_value
    if root in nodes:
        result += 1
        if 1 <= result <= len(nodes) - 1:


    else:
        return result

dfs(0, -1, set(KV[1:]))

