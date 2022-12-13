# https://atcoder.jp/contests/abc175/tasks/abc175_c

import math


def main (x, k, d):
    """
    x 数直線上のスタート地点。
    k 移動回数
    d 1回の移動距離
    """
    x = abs(x)  # マイナスの可能性もあるので、絶対値で考える
    move_count_near_0 = math.floor(x / d)  # 0に最も近づいた場合の移動回数
    near_0_distance = x % d  # 0に最も近づいた場合の座標
    
    rest_move_count = k - move_count_near_0  # 0に最も近づいた場合の残りの移動回数
    if rest_move_count < 0:  # 0に最も近づく前に移動回数を使い切ってしまった場合
        return abs(x - (d * k))  # 移動回数を使い切った場合の座標の絶対値が答え

    # 0に最も近づいてから0周辺でrest_move_countの数だけ行ったり来たりする
    if rest_move_count % 2 == 0:  # パリティによって0を超える場合と超えない場合に分岐
        return abs(near_0_distance)
    else:
        return abs(near_0_distance - d)

x, k, d = list(map(int, input().split(' ')))

print(main(x, k, d))