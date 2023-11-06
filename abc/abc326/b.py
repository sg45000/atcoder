N = int(input())

for i in range(N, 100000):
    s = str(i)
    if int(s[0]) * int(s[1]) == int(s[2]):
        print(i)
        exit()