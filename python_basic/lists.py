


def task_Z():
    N = 10
    K = 4

    l = [x for x in range(N)]


    # Моё решение
    def cycle_shift(l, k):
        if k == 0:
            return l

        l_copy = list(l)
        r = k if k > 0 else -k
        if k > 0:
            insert_index = 0
        insert_index = len(l_copy) - 1

        for _ in range(r):
            if k > 0:
                l_copy.insert(insert_index, l_copy.pop())
            l_copy.insert(insert_index, l_copy.pop(0))
        return l_copy

    # Решение с доп. массивом
    def cycle_shift_standart(lst, k):
        # Проверка, если вдруг K больше размера листа
        k = k % len(lst)
        k = -k
        ret = [0]*len(lst)
        len_lst = len(lst)
        for i in range(len_lst):
            if i+k < len_lst and i+k >= 0:  # Если сдвиг положительный
                ret[i] = lst[i+k]
            if i+k >= len_lst:  # Если сдвиг отрицательный
                ret[i] = lst[i+k-len_lst]
            if i+k < 0:  # Добавляем в начало с конца K элементов
                ret[i] = lst[i+k+len_lst]

        return(ret)

    # Решение для ленивых
    def smart_shift(l, n):
        return l[-n:] + l[:-n]


    print('list', l)
    print('smart_shift', smart_shift(l, 3))
    print('cycle_shift', cycle_shift(l, 3))
    #print(cycle_shift_standart(l, K))
    print('list', l)


def task_Y():
    def solve():
        n = 8
        x = []
        y = []
        for i in range(n):
            new_x, new_y = [int(s) for s in input().split()]
            x.append(new_x)
            y.append(new_y)
        
        for i in range(n):
            for j in range(i + 1, n):
                if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                    return "NO"

        return "YES"

    print(solve())


def task_X():
    def solve():
        n, k = [int(s) for s in input().split()]
        keg = ['I'] * n
        for _ in range(k):
            left, right = [int(s) for s in input().split()]
            for j in range(left - 1, right):
                keg[j] = '.'
        return ''.join(keg)
    
    print(solve())


#task_X()
#task_Y()
#task_Z()
