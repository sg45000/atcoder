"""
メモ化再帰でフィボナッチ数列を解く
"""

n = 11
count = 0

memo = [-1] * (n + 1)

def fibo(i):
    global count
    count += 1 
    if memo[i] >= 0:
        return memo[i]
    if i == 0:
        return 0
    if i == 1:
        return 1

    v = fibo(i - 1) + fibo(i - 2)
    memo[i] = v
    return v

print(fibo(n))
print(count)