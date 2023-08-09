def binary_search(l, t):
    left = 0
    right = len(l) - 1
    while left <= right:
        m = (left + right) // 2
        if l[m] == t:
            return m
        elif l[m] < t:
            left = m + 1
        else:
            right = m - 1
    return None
print(binary_search(sorted([1,2,4,56,3,26,654, 6, 3]), 6))