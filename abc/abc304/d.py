import bisect
W, H = list(map(int, input().split(" ")))
N = int(input())
PQ = [list(map(int, input().split(" "))) for _ in range(N)]
A = int(input())
AA = list(map(int, input().split(" ")))
B = int(input())
BB = list(map(int, input().split(" ")))

num_strawberry_in_pieces = [0] * (((A + 1) * (B + 1)))


for i in range(N):
    p, q = PQ[i]
    a = bisect.bisect(AA, p)
    b = bisect.bisect(BB, q)
    num_strawberry_in_pieces[b * (A + 1) + a] += 1

num_strawberry_in_pieces.sort()
print(str(num_strawberry_in_pieces[0]) + " " + str(num_strawberry_in_pieces[-1]))
