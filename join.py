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
