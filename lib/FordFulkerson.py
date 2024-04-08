from collections import defaultdict


"""
 最大フローを求めるライブラリ

 使用問題例: https://atcoder.jp/contests/abc091/tasks/arc092_a
"""


class NetWorkFlowGraph:
    """
    使用例

    g = Graph(6)
    g.add_edge(0, 1, 16 )
    g.add_edge(0, 2, 13 )
    g.add_edge(1, 2, 10 )
    g.add_edge(1, 3, 12 )
    g.add_edge(2, 1, 4 )
    g.add_edge(2, 4, 14)
    g.add_edge(3, 2, 9 )
    g.add_edge(3, 5, 20 )
    g.add_edge(4, 3, 7 )
    g.add_edge(4, 5, 4)

    print("The maximum possible flow is %d " % g.FordFulkerson(0, 5))

    """

    def __init__(self, vertices):
        # グラフの頂点数を初期化
        self.V = vertices
        # グラフを初期化。defaultdictは存在しないキーへのアクセスがあるとデフォルト値を返す。
        self.graph = defaultdict(lambda: defaultdict(int))

    def add_edge(self, u, v, w):
        # グラフにエッジを追加。uは始点、vは終点、wはエッジの重み(容量)を表す。
        self.graph[u][v] = w

    def BFS(self, s, t, parent):
        # ソースノードからシンクノードへのパスを探すためのBFSアルゴリズム。
        # 全頂点を未訪問に設定
        visited = [False] * (self.V)

        # ソースノードをキューに追加し、訪問済みとマーク
        queue = []
        queue.append(s)
        visited[s] = True

        # BFSループ
        while queue:
            u = queue.pop(0)

            # uから出る全エッジに対して
            for v, val in self.graph[u].items():

                # エッジが残容量を持ち、終点が未訪問である場合
                if visited[v] == False and val > 0:

                    # キューにエッジの終点を追加し、訪問済みとマーク
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

                    # 終点がシンクノードの場合、パスが見つかったのでTrueを返す
                    if v == t:
                        return True

        # シンクへのパスがない場合、Falseを返す
        return False

    def FordFulkerson(self, source, sink):
        # Ford-Fulkersonアルゴリズムを実装。sourceはソースノード、sinkはシンクノードを表す。

        # 親リストを初期化。これはBFSで見つけたパスを格納する。
        parent = [-1] * (self.V)

        # 最大フローを0に初期化
        max_flow = 0

        # ソースからシンクへのパスが見つかる限りループ
        while self.BFS(source, sink, parent):

            # パスを通じて送ることができるフローを見つける。最初は無限大とする。
            path_flow = float("Inf")
            s = sink

            # シンクからソースまでのパスを逆にたどる
            while s != source:
                # 経路上の最小容量を見つける
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # 最大フローにパスフローを追加
            max_flow += path_flow

            # シンクからソースまでパスを再度逆にたどり、エッジの残容量を更新
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow  # 前方エッジの容量を減らす
                self.graph[v][u] += path_flow  # 逆方向エッジの容量を増やす
                v = parent[v]

        # 最大フローを返す
        return max_flow


# ライブラリ end
