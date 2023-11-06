import deque

A = [list(map(int, input().split(" "))) for _ in range(4)]
B = [list(map(int, input().split(" "))) for _ in range(4)]
C = [list(map(int, input().split(" "))) for _ in range(4)]
x = 0
y = 0
z = 0
for i, s in enumerate(A):
    for j, c in enumerate(s):
        if c == '#':
            x &= 1 << i << (j * 4)
for i, s in enumerate(B):
    for j, c in enumerate(s):
        if c == '#':
            y &= 1 << i << (j * 4)
for i, s in enumerate(C):
    for j, c in enumerate(s):
        if c == '#':
            z &= 1 << i << (j * 4)

def toMove(p):
    if p << 1: # ポリのミドを右に移動
    elif p >> 1: # ポリのミドを左に移動
    elif p >> 4: # 上に移動
    elif p << 4: # 下に移動

field = 0

d = deque()
d.append(x)

while d:
    p = d.popleft()
    e = deque()
    field = p
    while e:
        q = e.popleft()
        f = deque()
        if field & q > 0:
            continue
        field &= q
        while f:
            r = f.popleft()
            if field & r > 0:
                continue
            field &= r
            if field == 2 ** 16 - 1:
                print("Yes")
                exit()

print("No")
