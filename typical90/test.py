class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs_postorder(node):
    if node is None:
        return

    stack = [node]
    visited = set()

    while stack:
        current = stack[-1]

        if current.children and current not in visited:
            visited.add(current)
            for child in current.children[::-1]:
                stack.append(child)
        else:
            node = stack.pop()
            print(node.value)

# ノードの作成と接続
# 例: A -> B -> C, B -> D, C -> E
root = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')

root.children = [B]
B.children = [C, D]
C.children = [E]

# 帰りがけ順の探索
dfs_postorder(root)