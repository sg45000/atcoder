import math
from functools import reduce

# 余弦定理
def angle(a, b, c):
    cosA = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    if -1 > cosA or 1 < cosA:
        cosA = round(cosA)
    return math.degrees(math.acos(cosA))

#2点間の距離を求める
def distance(a, b):
    ax, ay = a
    bx, by = b
    return math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)

# listを受け取って最大値を返す
def maximum(*int_list):
    return reduce(lambda a, b: max(a, b), int_list)

def binary_search_closest(lst, x, low=0, high=None):
    if high is None:
        high = len(lst) - 1

    if low > high:  # lowとhighが交差した場合
        if abs(lst[low] - x) < abs(lst[high] - x):
            return lst[low]
        else:
            return lst[high]
        
    if x < lst[low]:  # xがlstの最小値より小さい場合
        return lst[low]
    if x > lst[high]:  # xがlstの最大値より大きい場合
        return lst[high]

    mid = (low + high) // 2
    if lst[mid] == x:
        return lst[mid]
    elif lst[mid] < x:
        return binary_search_closest(lst, x, mid+1, high)
    else:
        return binary_search_closest(lst, x, low, mid-1)
        


N = int(input())
P = [list(map(int, input().split(" "))) for _ in range(N)]

answer = 0
for i in range(N):
    declinations = []
    for j in range(N):
        if i == j:
            continue
        x, y = map(lambda p: p[1] - p[0], zip(P[i], P[j]))
        d = math.degrees(math.atan2(y, x))
        if d < 0:
            d += 360
        declinations.append(d)
    for d1 in declinations:
        target = d1 - 180 if d1 > 180 else d1 + 180
        d2 = binary_search_closest(sorted(declinations), target)
        d3 = abs(d1 - d2)
        answer = max(answer, d3 if d3 <= 180 else 360 - d3)
print(answer)