"""
貪欲法で
2文探索かな
"""
N = int(input())
R = int(input())
X = list(map(int, input().split()))

X.sort()

s = 0

if X[s:]