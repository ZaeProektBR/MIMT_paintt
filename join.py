def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


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


print(ft_split('C:/Users/zuiko/OneDrive/Desktop/mini_paint/MIMT_paintt/2_5355301061030579284.pdf'))