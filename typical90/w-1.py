from collections import deque
"""
bit全探索で全ての組み合わせを調べ上げる
ルール通りに駒を置ているかはBFSで調べる
"""

H, W = list(map(int, input().split(" ")))
C = [list(input()) for _ in range(H)]
modulus = 10 ** 9 + 7

def in_range(coord):
    return 0 <= coord[0] < W and 0 <= coord[1] < H

def to_num(coord):
    return coord[0] + coord[1] * W

def to_coord(num):
    return (num // W, num % W)

vec = [(1,0), (0,1), (-1,0), (0,-1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

answer = 0

for b in range(1 << H * W):
    # bitが立っているマスが白色かどうかを確認する
    def is_valid(b):
        for i in range(H * W):
            if b >> i & 1 and C[i // W][i % W] == '#':
                return False
        return True
    if not is_valid(b):
        continue

    def bfs(s, b):
        q = deque()
        q.append(s)
        seen = [[-1] * (W) for _ in range(H)]
        while len(q) > 0:
            coord = q.popleft()
            seen[coord[1]][coord[0]] = 1

            for x, y in filter(in_range, map((lambda v: tuple(map(sum, zip(v, coord)))), vec)):
                if seen[y][x] < 0:
                    q.append((x, y))

                    # キングが隣り合ってないかチェック
                    is_king = bool(b >> to_num(coord) & 1)
                    next_is_king = bool(b >> to_num((x, y)) & 1)
                    if is_king and next_is_king:
                        return False
        return True
    
    if bfs((0, 0), b):
        answer += 1
        

print(answer)

