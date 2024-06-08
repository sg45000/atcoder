#############################
# input
#############################

get_ints = lambda: list(map(int, input().split()))
get_ints_n_lines = lambda n: [list(map(int, input().split())) for _ in range(n)]

get_chars = lambda: list(input())
get_chars_n_lines = lambda n: [input() for _ in range(n)]
get_chars_with_trim = lambda s: list(input().split(s))

#############################
# main
#############################


N = int(input())
AB = get_ints_n_lines(N)


imosu = [0] * 100_010
for i in range(N):
    a, b = AB[i]
    imosu[a] += 1
    imosu[b + 1] -= 1

a = 0
c = 0
ans = 0
for i in range(len(imosu)):
    a += imosu[i]
    if a > 0:
        c += 1
    if a == 0:
        ans = max(c, ans)
        c = 0
print(ans)
