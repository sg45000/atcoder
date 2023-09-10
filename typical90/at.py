N = int(input())
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
C = list(map(int, input().split(" ")))

p = 46

a_bucket = [0] * p
b_bucket = [0] * p
c_bucket = [0] * p

# 46で割った余り毎にその数をバケットに記録
# その種類数は46種になる
for a in A:
    a_bucket[a % p] += 1

for b in B:
    b_bucket[b % p] += 1

for c in C:
    c_bucket[c % p] += 1

# 46種類の要素が入ったバケットになるので、O(10 ^ 3)くらいで計算ができる
ans = 0
for i in range(p):
    for j in range(p):
        for k in range(p):
            if (i + j + k) % p == 0:
                ans += a_bucket[i] * b_bucket[j] * c_bucket[k]

print(ans)