def fromDigits(base: int, x: int):
    xs = [int(digit) for digit in str(x)]
    s = 0
    for i in range(len(xs)):
        s += xs[- i - 1] * base ** i
    return s


def toDigits(base: int, x: int):
    if x == 0:
        return 0
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    digits.reverse()
    return int(''.join(digits))