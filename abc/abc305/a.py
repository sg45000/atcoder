N = input()

a = int(N[0])
if len(N) == 2:
    b = int(N[1])
    if b <= 2:
        b = 0
    elif 8 <= b:
        a += 1
        b = 0
    else:
        b = 5
    print(str(a) + str(b))
elif len(N) == 3:
    print(N)
else:
    if a <= 2:
        a = 0
    elif 8 <= a:
        a += 1
    else:
        a = 5
    print(a)