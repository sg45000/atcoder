"""
移動の全探索 + 回復アイテム探索の二分探索
"""


from collections import defaultdict


def binary_search(li, t):
    left = 0
    right = len(li) - 1
    while left <= right:
        m = (left + right) // 2
        if li[m] == t:
            return t
        elif li[m] < t:
            left = m + 1
        else:
            right = m - 1
    return None

def move(command, coord):
    x, y = coord
    if command == "R":
        return (x + 1, y)
    elif command == "L":
        return (x - 1, y)
    elif command == "U":
        return (x, y + 1)
    elif command == "D":
        return (x, y - 1)
    raise Exception("無効なコマンド")

N, M, H, K = list(map(int, input().split(" ")))
commands = list(input())
items = [tuple(map(int, input().split(" "))) for _ in range(M)]

D = set()

for i in items:
    D.add(i)

answer = "Yes"
coord = (0, 0)
for command in commands:
    H -= 1
    if H < 0:
        answer = "No"
        break
    
    coord = move(command, coord)
    if coord in D and H < K:
        H = K
        D.remove(coord)


print(answer)