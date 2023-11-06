N = int(input())

if N == 0:
    print(0)
    exit()

ans = ""
while N:
    i = N % 2
    if i:
        ans += "1"
    else:
        ans += "0"
    N -= i
    N //= -2

print(str.join("", reversed(ans)))