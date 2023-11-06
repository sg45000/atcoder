## 1点
# def solve(n):
#     maximum = -1
#     for i in range(n):
#         print("?", i + 1)
#         out = int(input())
#         if maximum < out:
#             maximum = out
#         else:
#             return maximum
#     return maximum


# T = int(input())

# for _ in range(T):
#     N = int(input())
#     print("!", solve(N))


## 3点
### 三分探索

def query(i):
    print("?", i + 1)
    return int(input())

def solve(l, r):
    while l + 2 < r:
        c1 = (2 * l + r) // 3
        c2 = (l + 2 * r) // 3
        o1 = query(c1)
        o2 = query(c2)
        maximum = max(o1, o2)
        if o1 < o2:
            l = c1
        else:
            r = c2
    c1 = (2 * l + r) // 3
    c2 = (l + 2 * r) // 3
    return max(query(c1), query(c2), maximum) 


T = int(input())

for _ in range(T):
    N = int(input())
    print("!", solve(0, N))