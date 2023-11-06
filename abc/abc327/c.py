A = [list(map(int, input().split(" "))) for _ in range(9)]

box = [0] * 9

for i in range(9):
    record = 0
    column = 0
    for j in range(9):
        record |= 1 << (A[i][j] - 1)
        column |= 1 << (A[j][i] - 1)
        if i < 3 and j < 3:
            box[0] |= 1 << (A[j][i] - 1)
        elif i < 6 and j < 3:
            box[1] |= 1 << (A[j][i] - 1)
        elif i < 9 and j < 3:
            box[2] |= 1 << (A[j][i] - 1)
        elif i < 3 and j < 6:
            box[3] |= 1 << (A[j][i] - 1)
        elif i < 6 and j < 6:
            box[4] |= 1 << (A[j][i] - 1)
        elif i < 9 and j < 6:
            box[5] |= 1 << (A[j][i] - 1)
        elif i < 3 and j < 9:
            box[6] |= 1 << (A[j][i] - 1)
        elif i < 6 and j < 9:
            box[7] |= 1 << (A[j][i] - 1)
        else:
            box[8] |= 1 << (A[j][i] - 1)
    for k in range(9):
        if not (record & 1 << k):
            print("No")
            exit()
        if not (column & 1 << k):
            print("No")
            exit()
    
for i in range(9):
    for k in range(9):
        if not (box[i] & 1 << k):
            print("No")
            exit()

print("Yes")