p, q = list(input().split(" "))

d = dict()
d["A"] = 0
d["B"] = 3
d["C"] = 4
d["D"] = 8
d["E"] = 9
d["F"] = 14
d["G"] = 23

x = max(p, q)
y = min(p, q)

print(d[x] - d[y])