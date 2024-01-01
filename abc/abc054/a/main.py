A, B = list(map(int, input().split()))

A = A * 20 if A == 1 else A
B = B * 20 if B == 1 else B

if A > B:
    print("Alice")
elif B > A:
    print("Bob")
else:
    print("Draw")