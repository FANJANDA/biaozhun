import random
import time

li = [i for i in range(10)]
random.shuffle(li)


def outer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return res

    return wrapper

@outer
def find_2(l: list, num: int):
    l.sort()
    mid_value = l[len(l) // 2]
    if num < mid_value:
        new_l = l[:(len(l) // 2)]
        find_2(new_l, num)
    elif num > mid_value:
        new_l = l[(len(l) // 2) + 1:]
        find_2(new_l, num)
    elif num == mid_value:
        print('找到了')
        print(len(l) // 2)
        print(l)
    elif len(l) == 0:
        print('没找到')
        return 


find_2(li, 8)
