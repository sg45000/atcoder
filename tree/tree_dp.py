"""
木の最長経路を探索
メモ化再帰

これだとスターグラフの時に N^2の計算量になる
"""

N = 14
adjacents = [[1, 4, 6], [0, 2, 3], [1], [1], [0, 5], [4], [0, 7, 10, 11], [6, 8, 9], [7], [7, 12], [6], [6], [9, 13], [12]]
# スターグラフ
# N = 9
# adjacents = [[1,2,3,4,5,6,7,8], [0], [0], [0], [0], [0], [0], [0], [0]]


memo = [[-1] * N for _ in range(N)]
count = 0
def dfs(root, parent):
    global count
    
    result = 0
    for i in range(len(adjacents[root])):
        count += 1
        adjacent = adjacents[root][i]
        if adjacent == parent:
            continue
        if memo[root][i] < 0:
            memo[root][i] = dfs(adjacent, root)
        result = max(result, memo[root][i])
    return result + 1

for i in range(N):
    dfs(i, -1) - 1
    print(count)
    count = 0