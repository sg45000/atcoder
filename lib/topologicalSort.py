from collections import deque
from typing import List


def topologicalSort(V: int, G: List[List[int]], indeg: List[int]) -> List[int]:
    """
    DAGのトポロジカルソートを行い、順序付けられた頂点のリストを返します。
    V: 頂点数
    G: DAGのグラフ
    indeg: 各頂点の入次数
    """
    indeg = indeg.copy()
    q = deque()

    # 1.入次数0の頂点を発見し、キューに追加
    for i in range(V):
        if indeg[i] == 0:
            q.append(i)
    
    sorted_list = []
    while q:
        v = q.popleft()
        sorted_list.append(v)  # キューの中の頂点は入次数が0の頂点なのでリストに追加

        for adj in G[v]:
            indeg[adj] -= 1  # 2. 入次数0の頂点から到達できる頂点の入次数を1減らす
            if indeg[adj] == 0:
                q.append(adj)  # 入次数0になったらキューに追加
    return sorted_list


def is_DAG(V: int, G: List[List[int]], indeg: List[int]):
    """
    与えられたグラフがDAG（Directed Acyclic Graph）であるかどうかを判断します。
    V: 頂点数
    G: グラフの隣接リスト表現
    indeg: 各頂点の入次数のリスト
    """
    sorted_list = topologicalSort(V, G, indeg)
    return len(sorted_list) == V
