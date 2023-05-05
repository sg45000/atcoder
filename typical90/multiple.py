def multiple(l, r):
    l_len = len(l)
    res = [[0] * l_len for _ in range(l_len)]

    r = list(zip(*r))
    for i in range(l_len):
        for j in range(l_len):
            res[i][j] = l[i][0] * r[j][0] + l[i][1] * r[j][1] + l[i][2] * r[j][2] 
    return res

print(multiple([[1,2,3], [3,4,5], [5,4,3]], [[0,3,2], [2,4,2], [1,0,0]]))