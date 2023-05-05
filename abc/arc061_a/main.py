s = list(input())

s_length = len(s)

total = 0
for bit in range(2 ** (s_length - 1)):
    i = 0
    cp_s = [*s]
    for current_bit in range(s_length):
        if bit >> current_bit & 1:
            i += 1
            cp_s = cp_s[0:current_bit + i] + ['+'] + cp_s[current_bit + i:]
    total += eval("".join(cp_s))

print(total)