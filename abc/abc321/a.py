N = input()

ans = "Yes"
p = 10
for s in N:
    if p <= int(s):
        ans = "No"
        break
    p = int(s)

print(ans)