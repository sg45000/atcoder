"""
すぬけプライムに入らなかった場合、それぞれの日に払う合計金額を考える
それぞれの日の払う金額がCより高かった場合はCを選択する
それを貪欲に日数分行えば答えが出る

ただし、日数は最大10^9なので、全日数を網羅するとTLEする
なので、金額の増減があった日だけを記録していき、日毎の合計金額の計算は
増減があった日から次に増減があった日までは同じ金額なので、日数とかけることで日✖️合計金額を算出できる
"""

from collections import defaultdict
N, C = list(map(int, input().split(" ")))
abc = [list(map(int, input().split(" "))) for _ in range(N)]

AB = []
for a, b, c in abc:
    AB.append((a, c))
    AB.append((b + 1, -c))


def fst(x):
    return x[0]
    

AB.sort(key=fst)

pay_of_day = defaultdict(int)

for i, v in AB:
    pay_of_day[i] += v

pay_of_day = sorted(list(pay_of_day.items()), key=fst)

pre_day = pay_of_day[0][0]
value = pay_of_day[0][1]
ans = 0

for i in range(1, len(pay_of_day)):
    day, v = pay_of_day[i]
    days = day - pre_day
    if value < C:
        ans += days * value
    else:
        ans += days * C

    value += v
    pre_day = day

print(ans)
