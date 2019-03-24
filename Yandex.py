

def input_value():
    N = int(input())
    return(N)


def divisor_search(arg):
    n = []
    a = []
    f = 0  # счетчик цикла for
    w = 0  # счетчик цикла while

    import time
    start_time = time.time()  # счетчик времени

    for i in range(2, arg):
        f += 1
        n.append(arg)

        while arg % i == 0:
            w += 1
            arg = int(arg / i)
            a.append(i)

    print('Список делимых-частных: ', n)
    print('Список простых делителей: ', a)
    print('Количество итераций for:', f)
    print('Количество итераций while:', w)
    print('--- %s seconds ---' % (time.time() - start_time))


# ----------------------------------------------


divisor_search(input_value())