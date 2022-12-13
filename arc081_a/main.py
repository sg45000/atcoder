# 計算量On


from collections import defaultdict


def main(n, sides):
    side_count_dict = defaultdict(int)
    for side in sides:
        side_count_dict[side] += 1  # 辺の長さごとに何本あるか数えてdictに入れておく

    side_ranking = sorted(side_count_dict.keys(), reverse=True)  # 辺の長さのランキングを作る

    height = 0
    width = 0
    for side in side_ranking:  # 長い辺から探索
        if side_count_dict[side] >= 2:  # 2本以上あるものを長方形の辺として使う
            if side_count_dict[side] >= 4 and height == 0:  # 4本以上あってそれ以上長い辺がない場合は正方形としてその辺を使う
                height = width = side
                break
            if height == 0:
                height = side
            elif width == 0:
                width = side
            else:
                break
    return height * width  # 長方形の面積を計算する




n = int(input())
sides = list(map(int, input().split(' ')))
print(main(n, sides))