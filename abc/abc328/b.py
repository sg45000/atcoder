N = int(input())
D = list(map(int, input().split(" ")))

ans = 0
for i in range(1, N + 1):
    d = D[i - 1]
    for j in range(1, d + 1):
        s = str(j)
        flag = True
        char = str(i)[0]
        for next_char in str(i):
            if char != next_char:
                flag = False
        for c in s:
            if char != c:
                flag = False
        if flag:
            ans += 1

print(ans)
                

