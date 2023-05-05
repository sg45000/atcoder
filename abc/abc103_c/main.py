"""
    mの最大値はa1..aNの最大値*2-1
    m mod aN の最大値はaNの最大値-1
    a1..aN全ての数に対して、m mod aN が aN - 1 となるmが存在する
    従って、a1..aNそれぞれから1をひいた数の合計が最大値となる
"""
n = int(input())
aList = list(map(int, input().split(' ')))

answer = sum(aList) - len(aList)
print(answer)