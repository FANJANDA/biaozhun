# 装饰器 一个用来给其他函数增加功能的函数
# 面向对象的核心 开放封闭原则 开放 在源代码不变的情况下为其添加功能 封闭
import time

def inside(group, s, z):
    print('欢迎来到王者荣耀')
    print(f'您的出生地在{group}阵容')
    print(f'敌军还有{s}秒到达战场')
    time.sleep(3)
    print(f'{z}出击!')


# inside('蓝色', 3, '全军')


def outer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(end - start)

    return wrapper


inside = outer(inside)
inside('蓝色', 3, '全军')
