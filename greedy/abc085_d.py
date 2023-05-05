import math


# 投げ攻撃力の高いものから順番に投げていく
# 投げようとした刀が振り攻撃力が最も高い刀より弱い場合は、振り攻撃力が最も高い刀で降り続ける
# この際既に投げた刀でも振ることができると考える(振った後に投げたという解釈にもできるから)
def main(n, h, katana):
    swing = sorted([k[0] for k in katana], reverse=True) # 振り
    throw = sorted([k[1] for k in katana], reverse=True) # 投げ
    swing_power = swing[0]  # 振る場合は最も攻撃力の高い刀を振り続ければいい
    damage = 0
    for i in range(n):
        throw_power = throw[i]
        if swing_power < throw_power:
            damage += throw_power
            if h <= damage: # 複数投げて倒す
                return i + 1
            continue
        else:
            return i + math.ceil((h - damage) / swing_power) # 複数投げて、途中から振って倒す
    return n + math.ceil((h - damage) / swing_power) # 全て投げて、振って倒す


n, h = list(map(int, input().split(" ")))

katana = [list(map(int, input().split(" "))) for _ in range(n)]
print(main(n, h, katana))
