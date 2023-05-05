from collections import deque

def main(n, m, connections):
    graph = [[] for _ in range(n + 1)]
    for con in connections:
        graph[con[0]].append(con[1])
        graph[con[1]].append(con[0])
    
    signs = [0] * (n+1)

    q = deque()
    q.append(1)
    visited = [False] * (n + 1)
    while len(q) > 0:
        room_no = q.popleft()
        for next_room_no in graph[room_no]:
            if visited[next_room_no]:
                continue
            visited[next_room_no] = True
            signs[next_room_no] = room_no
            q.append(next_room_no)
    if all(visited[2:]):
        print("Yes")
        for s in signs[2:]:
            print(s)
    else:
        print("No")



n, m = list(map(int, input().split(' ')))
connections = [list(map(int, input().split(' '))) for _ in range(m)]

main(n, m, connections)