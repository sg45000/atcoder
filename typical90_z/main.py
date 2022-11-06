from collections import deque

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.child_nodes = []


def make_tree(N, graph):
    q = deque()
    node = Node(1)

    q.append(node)
    solved = [False] * (N + 1)
    while len(q) > 0:
        current = q.popleft()
        child_values = graph[current.value]
        for child_value in child_values:
            if solved[child_value]:
                continue
            else:
                solved[child_value] = True
            child_node = Node(child_value)
            current.child_nodes.append(child_node)
            q.append(child_node)
    return node

def solve(N, edges):
    graph = [[] for _ in range(0, N + 1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    tree = make_tree(N, graph)
    q = deque()
    q.append(tree)
    answer = []
    count = 0
    while len(q) > 0:
        current = q.popleft()
        for child_node in current.child_nodes:
            if count % 2 != 0:
                answer.append(child_node.value)
            q.append(child_node)
        count += 1
    return answer

def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    
    return " ".join([str(i) for i in solve(N, edges)])
    

# print(main())

print(solve(4, [[1,2], [2,3], [2,4]]))
