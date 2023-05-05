# 文字列をbitで表す

# 各インデックスを捜査し、そのインデックスより左側の(の数が)の数以下であることが正しいかっこの条件
def check(bit):
    count = 0
    for i in range(len(bit)):
        count += 1 if bit[i] == '0' else -1
        if count < 0:
            return False
    return True

N = int(input())

# 偶数でないと正しい括弧は作れない
if N % 2 == 0:
    for b in range((2 ** N)):
        t = ('0' * N + bin(b)[2:])
        bit = t[len(t) - N:]

        # (と)の数は同じである必要がある
        if bit.count('1') != bit.count('0'):
            continue
        if check(bit):
            answer = bit.replace('0', '(')
            print(answer.replace('1', ')'))

