
import sys

sys.setrecursionlimit(1000 * 1000)


def solve(buttonNo, buttons, count):
    nextButtonNo = buttons[buttonNo - 1]
    buttons[buttonNo - 1] = None
    if nextButtonNo == 2:
        return count + 1
    elif nextButtonNo is None:
        return -1
    else:
        return solve(nextButtonNo, buttons, count + 1)


def main():
    N = int(input())
    As = [int(input()) for _ in range(N)]
    return solve(1, As, 0)


print(main())
