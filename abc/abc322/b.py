N, M = list(map(int, input().split(" ")))
S = input()
T = input()


head = T[:N] == S
tail = T[M - N:] == S
if head and tail:
    print(0)
elif head:
    print(1)
elif tail:
    print(2)
else:
    print(3)
