H, W = list(map(int, input().split(" ")))
S = [input() for _ in range(H)]

def to_num(b):
    return int(b, 2)

def to_bit(n):
    return "00000000" + bin(n)[2:]

def find_first_one(s):
    for i, c in enumerate(s):
        if c == "1":
            return i

def find_last_one(s):
    a = 0
    for i, c in enumerate(s):
        if c == "1":
            a = i
    return a
    


unit = 0
for line in S:
    bit = ""
    for cell in line:
        if cell == ".":
            bit += "0"
        else:
            bit += "1"
    unit = unit | to_num(bit)

l = find_first_one(to_bit(unit)[-W:])
r = find_last_one(to_bit(unit)[-W:])

unit = 0
for col_num in range(W):
    bit = ""
    for line_num in range(H):
        if S[line_num][col_num] == ".":
            bit += "0"
        else:
            bit += "1"
    unit = unit | to_num(bit)

u = find_first_one(to_bit(unit)[-H:])
d = find_last_one(to_bit(unit)[-H:])

for h in range(H):
    for w in range(W):
        if l <= w <= r and u <= h <= d:
            if S[h][w] == ".":
                print(str(h + 1) + " " + str(w + 1))
                exit()