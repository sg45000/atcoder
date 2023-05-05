def main(A,B):
    # bin(x ^ y)
    num_count = B - A
    a = 1 if num_count % 2 == 0 else 0
    return int(bin(B ^ a), 2)

# A, B = map(int, input().split())

print(main(123, 456))
# print(main(A, B))