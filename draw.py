def ft_split(stroka, s):
    stroka += s
    arg = ''
    spisok = []
    for i in stroka:
        if i != s:
            arg += i
        else:
            if arg != '':
                spisok.append(arg)
                arg = ''
    return spisok

def field(x, y, char):
    field_sp = []
    for i in range(x):
        for j in range(y):
            field_sp[i][j] = char
    return field_sp


def crug(width, height, a, b, r, char, char_f):
    map_= [[char_f for x in range(width)]for y in range(height)]
    for y in range(height):
        for x in range(width):
            if (x - a) ** 2 + (y - b) ** 2 <= (r ** 2 - 2.2 ** 2):
                map_[y][x] = char
    return map_

def draw_circle(w_f, h_f, x, y, r, char, char_f): # Алгоритм Брезендхема
    map_= [[char_f for x in range(w_f)]for y in range(w_f)]
    disp_x = x
    disp_y = y
    x = 0
    y = r
    delta = (1 - 2 * r)
    error = 0
    while y >= 0:
        map_[disp_x + x][disp_y + y] = char
        map_[disp_x + x][disp_y - y] = char
        map_[disp_x - x][disp_y + y] = char
        map_[disp_x - x][disp_y - y] = char
        
        error = 2 * (delta + y) - 1
        if ((delta < 0) and (error <=0)):
            x+=1
            delta = delta + (2*x+1)
            continue
        error = 2 * (delta - x) - 1
        if ((delta > 0) and (error > 0)):
            y -= 1
            delta = delta + (1 - 2 * y)
            continue
        x += 1
        delta = delta + (2 * (x - y))
        y -= 1
    return map_


def draw_line(w_f, h_f, x1, y1, x2, y2, char, char_f): # Алгоритм Брезендхема
    map_= [[char_f for x in range(w_f)]for y in range(w_f)]
    dx = x2 - x1
    dy = y2 - y1
    sign_x = 1 if dx>0 else -1 if dx<0 else 0
    sign_y = 1 if dy>0 else -1 if dy<0 else 0
    if dx < 0:
        dx = -dx
    if dy < 0:
        dy = -dy
    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy
    x, y = x1, y1
    error, t = el/2, 0
    map_[x][y] = char
    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        map_[x][y] = char
    return map_

def draw_rec_nf(w_f, h_f, x, y, w, h, char, char_f):
    mas = [[char_f for x in range(w_f)]for y in range(h_f)]
    for y1 in range(h + y):
        for x1 in range(w + x):
            if (x1 >= x and y1 == y) or (x1 == x and y1 >= y) or (x1 == x + w - 1 and y1 >= y) or\
                    (x1 >= x and y1 == y + h - 1):
                mas[y1][x1] = char
    return mas

def draw_rec_f(w_f, h_f, x, y, w, h, char, char_f):
    mas = [[char_f for x in range(w_f)]for y in range(h_f)]
    for y1 in range(h + y):
        for x1 in range(w + x):
            if h + y >= y1 >= y and w + x >= x1 >= x:
                mas[y1][x1] = char
    return mas


#xx = square_full(10, 10,1, 3, 4, 5, '*', '&')
#for x in range(len(xx)):
#    print(*xx[x])
#DrawFillRec([10, 5, '*'], 5, 1, color='W')
#sp = draw_param(10, 7, 1, 1, 5, 5, '$', '*')
#for i in sp:
#    print(*i)
#sp1 = draw_line(5, 7, 8, 12, '#')
#for i in sp1:
#    print(*i)
#sp1 = draw_circle(20, 20, 7, 7, 5, '*', '#')
#for i in sp1:
#    print(*i)

#sp1 = crug(50, 50, 20, 20, 5, '%','j')
#for i in sp1:
#    print(*i)
#sp2 = pram_nezakr(10, 10, 2, 1, 5, 7, '#', '%')
#for i in sp2:
#    print(*i)
#hight = int(input())
#wight = int(input())
#char = input()
#for i in range(hight):
#    if i == 0 or i == hight - 1:
#        for j in range(wight):
#            print(char, end='')
#    else:
#        print(char, end='')
#        for j in range(1, wight - 1):
#            print(' ', end='')
#        print(char, end='')
#    print()