import math
R, X, Y =list(map(int, input().split(" ")))

print(math.sqrt(X ** 2 + Y ** 2) // R + 1)