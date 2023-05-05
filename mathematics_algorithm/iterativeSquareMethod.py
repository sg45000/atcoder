# a^bをmodで割った余　を求める. 1 <= a <= 100 , 1 <= b <= 10^9
a = int(input())
b = int(input())

m = 1000000007

ans = 1
p = a
for i in range(30):
    if b & 1 << i != 0:
        ans *= p
        ans %= m
    p *= p
    p %= m

print(ans)