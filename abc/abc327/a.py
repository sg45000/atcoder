N = int(input())
S = input()

a = False
b = False

for c in S:
    if c == 'a':
        if b:
            print("Yes")
            exit()
        a = True
        b = False
    elif c == 'b':
        if a:
            print("Yes")
            exit()
        a = False
        b = True
    else:
        a = False
        b = False

print("No")