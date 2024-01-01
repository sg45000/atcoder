S = input()

L = ""

for i in range(len(S)):
    if len(L) >= 2:
        if L[-2] + L[-1] + S[i] == "ABC":
            L = L[:-2]
        else:
            L = L + S[i]
    else:
        L = L + S[i]

print(L)
