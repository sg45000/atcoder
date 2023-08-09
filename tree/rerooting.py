"""

"""

# N = 14
# adjacents = [[1, 4, 6], [0, 2, 3], [1], [1], [0, 5], [4], [0, 7, 10, 11], [6, 8, 9], [7], [7, 12], [6], [6], [9, 13], [12]]
# スターグラフ
# N = 9
# adjacents = [[1,2,3,4,5,6,7,8], [0], [0], [0], [0], [0], [0], [0], [0]]

N = 12
edges =[[0,1],[1,2],[1,3],[0,4],[4,5],[0,6],[6,7],[7,8],[7,9],[6,10],[6,11]]

adjacents = [[] for _ in range(N)]
indexForAdjacents = [[] for _ in range(N)]
for edge in edges:
    a, b = edge
    indexForAdjacents[a].append(len(adjacents[b]))
    indexForAdjacents[b].append(len(adjacents[a]))
    adjacents[a].append(b)
    adjacents[b].append(a)

child_subtree_result = [[0] * len(adjacents[i]) for i in range(N)]

node_result = []

def merge(left, right):
    # TODO: 未実装
    pass

def add_node(value, node_id):
    # TODO: 未実装
    pass

"""
行きがけ順で訪問順を記録
"""
parents = [0] * N
order = [0] * N

index = 0
stack = [0]
parents[0] = -1

while len(stack) > 0:
    node = stack.pop()
    order[index] = node
    index += 1
    for i in range(len(adjacents[node])):
        adjacent = adjacents[node][i]
        if adjacent == parents[node]:
            continue
        stack.append(adjacent)
        parents[adjacent] = node


# 帰りがけ順
for i in reversed(range(1, N)):
    node = order[i]
    parent = parents[node]

    result = 0 # TODO: ?
    parentIndex = -1
    for j in range(len(adjacents[node])):
        if adjacents[node][j] == parent:
            parentIndex = j
            continue
        result = merge(result, child_subtree_result[node][j])
    child_subtree_result[parent][indexForAdjacents[node][parentIndex]] = add_node(result, node)

print(child_subtree_result)