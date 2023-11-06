K = int(input())

dp = [[] for _ in range(11)]

for i in range(10):
    dp[0].append(i)

if 1 <= K <= 9:
    print(K)
    exit()

i = 10

def judge(digit, head):
    global i
    for d in dp[digit - 1]:
        if head <= int(str(d)[0]):
            break
        else:
            dp[digit].append(int(str(head) + str(d)))
        if i == K:
            print(dp[digit][-1])
            exit()
        i += 1

for digit in range(1, 11):
    for head in range(1, 10):
        judge(digit, head)

            
