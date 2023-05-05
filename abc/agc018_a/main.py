import math


def main(n, k, balls):
    gcd = gcd_all(balls)
    m = max(balls)
    if k % gcd == 0 and k <= m:
        return 'POSSIBLE'
    else:
        return 'IMPOSSIBLE'


def gcd_all(nums):
    gcd = nums[0]
    for num in nums:
        gcd = math.gcd(gcd, num)
    return gcd


n, k = list(map(int, input().split(' ')))
balls = list(map(int, input().split(' ')))
print(main(n, k, balls))