#hight = int(input())
#wight = int(input())
#char = input()
def draw_param(x, y, wight, hight, char):
    map_= [[' ' for x in range(wight)]for y in range(hight)]
    for i in range(hight):
        if i == 0 or i == hight - 1:
            for j in range(wight):
                map_[i][j] = char
        else:
            map_[i][0] = char
            for j in range(1, wight - 1):
                #print(' ', end='')
                pass
            map_[i][0] = char
        return map_
        #print()
#sp = draw_param(1, 1, 5, 7, '*')
#for i in sp:
#    print(*i)\

b = int(input())
a = int(input())
simvol = input()
def pram_nezakr(a, b, s)
    sp = []
    sp.append(list(simvol) * a)
    for i in range(b - 2):
        sp1 = []
        sp1.append(simvol)
        for i in range(a - 2):
            sp1.append(' ')
        sp1.append(simvol)
        sp.append(sp1)
    sp.append(list(simvol) * a)
    return sp

for i in sp:
    print(i)