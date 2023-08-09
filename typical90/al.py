"""
lcm(A, B) * gcd(A, B) = A * B
"""
A, B = list(map(int, input().split(" ")))

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

lcm = A * B // gcd(A, B)
if 10 ** 18 < lcm:
    print("Large")
else:
    print(lcm)