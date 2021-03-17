import sys
import os
from draw import *


def ft_len(str_):
    a = 0
    for i in str_:
        a += 1
    return a


def is_digit(st):
    try:
        st1 = int(st)
        return True
    except:
        return False


def ft_join(lst, n=' '):
    a = ft_len(lst)
    i = 0
    x = ''
    for i in range(a):
        x += lst[i]
        if i != a - 1:
            x += n
        i += 1
    return x


def file_read(path):
    try:
        sp = []
        with open(path, 'r') as f:
            for i in f.readlines():
                if i[ft_len(i) - 1:] == '\n':
                    sp.append(i[:-1:])
                else:
                    sp.append(i)
        return sp
    except:
        return 'Error: Operation file corrupted'


def ft_split(stroka, s=' '):
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

def error_check(sp):
    if ft_len(sp) != 2:
        return 'Error: data file'
    sp1 = ft_split(sp[0])
    sp2 = ft_split(sp[1])
    if not (is_digit(sp1[0]) and int(sp1[0]) <= 300 and int(sp1[1]) <= 300 and int(sp1[0]) > 0 and int(sp1[1]) > 0 and is_digit(sp1[1]) and not is_digit(sp1[2])) and ft_len(sp1[2]) != 3:
        return 'Error: data file'
    if not (sp2[0] in ['r', 'R', 'c', 'C', 'L']):
        return 'Error: data file'
    for i in sp2[1:-1]:
        if not is_digit(i):
            return 'Error: data file'
    if is_digit(sp2[-1]):
        return 'Error: data file'
    if sp2[0] == 'L' and ft_len(sp2) != 6:
        return 'Error: data file'
    elif ft_len(sp2) == 6 and sp2[0] == 'R':
        return sp
    elif ft_len(sp2) == 6 and sp2[0] == 'r':
        return sp
    elif ft_len(sp2) != 5 and sp2[0] != 'L':
        #print(sp2)
        return 'Error: data file'
    return sp


def arg_pass(sp):
    if ft_len(sp) == 2:
        if sp[-1][-2:] != 'it':
            return 'Error: Operation file has not correct extension'
        elif ft_split(sp[-1], '/')[-1] != 'operation.it':
            return 'Error: name file'
        elif os.path.exists(sp[-1]):
            return sp[-1]
        elif not os.path.exists(sp[-1]):
            return 'Error: file not found'
    elif ft_len(sp) > 2:
        return "Error: a lot of arguments"


def main():
    Er = arg_pass(sys.argv)
    if Er == 'Error: Operation file has not correct extension':
        print('Error: Operation file has not correct extension')
    elif Er == 'Error: name file':
        print('Error: name file')
    elif Er == "Error: a lot of arguments":
        print('Error: a lot of arguments')
    elif Er == 'Error: file not found':
        print('Error: file not found')
    else:
        if file_read(Er) == 'Error: Operation file corrupted':
            print('Error: Operation file corrupted')
        else:
            sp = error_check(file_read(Er))
            if type(sp) == list:
                if sp[1][0] == 'C':
                    sp1 = []
                    for i in sp:
                        sp1.append(ft_split(i))
                    for i in crug(int(sp1[0][0]), int(sp1[0][1]), int(sp1[1][1]), int(sp1[1][2]), int(sp1[1][3]), sp1[1][4], sp1[0][2]):
                        print(*i)
                elif sp[1][0] == 'L':
                    sp1 = []
                    for i in sp:
                        sp1.append(ft_split(i))
                    m = draw_line(int(sp1[0][0]), int(sp1[0][1]), int(sp1[1][1]), int(sp1[1][2]), int(sp1[1][3]), int(sp1[1][4]), sp1[1][5], sp1[0][2])
                    for i in m:
                        print(*i)
                elif sp[1][0] == 'c':
                    sp1 = []
                    for i in sp:
                        sp1.append(ft_split(i))
                    m = draw_circle(int(sp1[0][0]), int(sp1[0][1]), int(sp1[1][1]), int(sp1[1][2]), int(sp1[1][3]), sp1[1][4], sp1[0][2])
                    for i in m:
                        print(*i)
                elif sp[1][0] == 'r':
                    sp1 = []
                    for i in sp:
                        sp1.append(ft_split(i))
                    m = draw_rec_nf(int(sp1[0][0]), int(sp1[0][1]), int(sp1[1][1]), int(sp1[1][2]), int(sp1[1][3]), int(sp1[1][4]), sp1[1][5], sp1[0][2])
                    for i in m:
                        print(*i)
                elif sp[1][0] == 'R':
                    sp1 = []
                    for i in sp:
                        sp1.append(ft_split(i))
                    print(sp1)
                    m = draw_rec_nf(int(sp1[0][0]), int(sp1[0][1]), int(sp1[1][1]), int(sp1[1][2]), int(sp1[1][3]), int(sp1[1][4]), sp1[1][5], sp1[0][2])
                    for i in m:
                        print(*i)
            else:
                print(sp)


def widht_height_background_char(w, h, char):
    for i in range(h):
        if i == 0 or i == h - 1:
            for j in range(w):
                print(char, end=' ')
        else:
            print(char, end=' ')
            for j in range(1, w - 1):
                print(' ', end=' ')
            print(char, end=' ')
        print()



if __name__ == '__main__':
    main()
    pass
# file_read('operation.it')
# widht_height_background_char(5, 9, '@')
