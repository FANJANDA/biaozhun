import time
import decorter


@decorter.outer
def recharge(num):
    for i in range(num, 101):
        print(f'\r当前手机电量{"❁" * i} {i}%', end='')
        time.sleep(0.05)
    print('\n充电完成')
    return 100


def outer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return res

    return wrapper


recharge(1)
