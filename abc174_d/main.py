"""
    R より前にWがあってはいけないので、
    必ず RRRRWWWW というふうに Rが連続で並んだ後、Wが連続で並ぶ形になる
"""
def main(n, stones):  
    r_cnt = stones.count('R')
    return stones[:r_cnt].count('W')


n = int(input())
stones = list(input())
print(main(n, stones))