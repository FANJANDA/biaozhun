from 软件目录规范.lib.common import logger


def login():
    print('执行登录功能'.center(30, '*'))
    logger('大仙登录了')


def register():
    print('执行注册功能'.center(30, '*'))
    logger('大仙注册了')


def recharge():
    print('执行充值功能'.center(30, '*'))
    logger('大仙充值了')


def transfer():
    print('执行转账功能'.center(30, '*'))
    logger('大仙转账了')


func_dic = {
    '0': ('退出', exit),
    '1': ('登录', login),
    '2': ('注册', register),
    '3': ('转账', transfer),

}


def main():
    while True:
        for key in func_dic:
            print(key, func_dic[key][0])
        opt = input('请输入功能编号>>>').strip()
        if opt not in func_dic:
            print('\033[33m输入有误!请重新输入!\033[0m')
            continue
        func_dic[opt][1]()  # 拿到函数名可以执行
