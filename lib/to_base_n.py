from typing import List

"""
10進数からbase進数に変換
2 <= base <= 10
0 <= n
"""
def from_base_10(n: int, base: int) -> str:
    if n == 0:
        return "0"

    to: List[int] = []
    while n > 0:
        r = n % base
        to.append(r)
        n = (n - r) // base
    return "".join(reversed(list(map(str, to))))

"""
base進数から10進数に変換
2 <= base <= 10
"""
def to_base_10(s: str, base: int) -> int:
    n = 0
    for i, c in enumerate(reversed(s)):
        n += int(c) * (base ** i)
    return n
