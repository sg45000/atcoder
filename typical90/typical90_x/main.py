def main(n, k, aList, bList):
    for i in range(n):
        move = abs(aList[i] - bList[i])
        if k < move:
            return 'No'
        else: 
            k -= move
    return 'Yes' if k % 2 == 0 else 'No'


n, k = list(map(int, input().split(' ')))
aList = list(map(int, input().split(' ')))
bList = list(map(int, input().split(' ')))

print(main(n, k, aList, bList))