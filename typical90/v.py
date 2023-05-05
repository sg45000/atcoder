def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

A, B, C = list(map(int, input().split(" ")))
g = gcd(gcd(A, B), C)
print(A // g + B // g + C // g - 3)