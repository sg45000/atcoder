"""
2分かけた場合は、1分かけた場合よりa - b ポイントもらえる
つまり、bポイント

キモなのはAi/2 < Bi < Aiという点
a - b が b を超えることはないので、
a-bとbを全て一つにまとめて降順ソートして上から貪欲に取っていけばいい
(必ず、満点を取る場合は、部分点を取っていることになる)
"""

N, K = list(map(int, input().split()))

point = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    point.append(b)
    point.append(a - b)

point.sort(reverse=True)

print(sum(point[:K]))