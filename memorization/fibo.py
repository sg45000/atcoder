count = 0

def fibo(n):
    global count
    count = count + 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

print(fibo(11))
print(count)
