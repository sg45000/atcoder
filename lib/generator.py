def number_generator():
    num = 0
    while True:
        yield num
        num += 1

# ジェネレータを作成
gen = number_generator()

# 値を生成
for i in gen:
    print(i)