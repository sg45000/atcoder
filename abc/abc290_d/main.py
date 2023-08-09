"""
全探索するとT*NでLTE
https://twitter.com/kyopro_friends/status/1627303319994789888

一つのテストケースに対し、O(1)で解ける
1回目の手順を考えると手順ℹ︎でxは
0, D mod N, 2D mod N, 3D mod N となる
これはそれぞれDとNの最大公約数(gcd)の倍数となる。 (手順ℹ︎では、xはgcd(D, N)の倍数。ただしN以下)
Nをgcdで割った回数(cycle)でこのxは循環する。
循環した時に手順ⅱの条件に合致する。


"""


T = int(input())

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

for _ in range(T):
    N, D, K = list(map(int, input().split(" ")))
    cycle = N // gcd(D, N)  # 手順ⅱのマスxに印がついていると判定されるまでの回数
    i = (K % cycle or cycle) - 1  # 
    
    x = (i * D % N) + ((K - 1) // cycle)
    print(x)