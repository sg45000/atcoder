from collections import deque

def find_start(H, W, objects):
    for y in range(H):
        for x in range(W):
            if objects[y][x] == 's':
                return (x, y)

def check(H, W):
    def fn(point):
        return 0 <= point[0] < W and 0 <= point[1] < H
    return fn

def get_next(x, y):
    steps = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    return list(map(lambda p: (p[0] + x, p[1] + y), steps))



def main():
    H, W = list(map(int, input().split(" ")))
    objects = [list(input()) for _ in range(H)]

    start = find_start(H, W, objects)

    Q = deque()
    Q.append(start)

    visited = [[-1] * W for _ in range(H)]

    visited[start[1]][start[0]] = 1

    while len(Q) > 0:
        x, y = Q.pop()
        
        for next_x, next_y in list(filter(check(H, W), get_next(x, y))):
            if visited[next_y][next_x] > 0:
                continue
            if objects[next_y][next_x] == 'g':
                print('Yes')
                return
            elif objects[next_y][next_x] == '.':
                Q.append((next_x, next_y))
                visited[next_y][next_x] = 1
    print('No')


main()