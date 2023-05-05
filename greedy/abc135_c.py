n = int(input())
monsters = list(map(int, input().split(" ")))
soldiers = list(map(int, input().split(" ")))
count = 0

for i in range(n):
    this_town_monster = monsters[i]
    next_town_monster = monsters[i + 1]
    soldier = soldiers[i]
    power1 = soldier - this_town_monster
    if power1 >= 0:
        count += this_town_monster
        power2 = power1 - next_town_monster
        if power2 >= 0:
            count += next_town_monster
            monsters[i + 1] = 0
        else:
            count += power1
            monsters[i + 1] = -1 * power2
    else:
        count += soldier

print(count)