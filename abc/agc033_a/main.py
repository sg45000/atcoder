from collections import deque


def main(h, w, lines):
    que = deque()
    count = 0
    for y in range(h):
        for x in range(w):
            if(lines[y][x] == "#"):
                que.append((y, x))
                count += 1
    visited = [[False] * w for _ in range(h)]
    answer = 0
    while count < h*w:
        answer += 1
        next_que = deque()
        while len(que) > 0:
            point = que.popleft()
            for p in around(point):
                if lines[y][x] == '.' and check(h, w, p) and not visited[p[0]][p[1]]:
                    count += 1
                    visited[p[0]][p[1]] = True
                    next_que.append(p)
        que = next_que

    return answer

def around(point):
    y = point[0]
    x = point[1]
    return [(y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x)]

def check(h, w, point):
    y = point[0]
    x = point[1]
    return y < h and 0 <= y and x < w and 0 <= x

h, w = list(map(int, input().split(' ')))
lines = [list(input()) for _ in range(h)]
print(main(h, w, lines))

# lines = ["." * 1000] * 1000
# lines[480] = "." * 500 + "#" + "." * 499
# print(main(1000, 1000, lines))