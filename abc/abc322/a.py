N = int(input())

S = input()

for i in range(N - 2):
    if 'ABC' == S[i] + S[i+1] + S[i+2]:
        print(i + 1)
        exit()

print(-1)