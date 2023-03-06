from functools import wraps


def auth(source):
    def outer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            name = input("请输入您的用户名").strip()
            pwd = input("请输入您的密码").strip()
            if source == 'file':
                print('使用file解锁')
                if name == 'jack' and pwd == '123456':
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('密码错误')
            elif source == 'mysql':
                print('使用mysql')
            elif source == 'ldap':
                print('使用的是ldap')
        return wrapper
    return outer
# 有参装饰器 装饰器叠加使用
@auth('mysql')
def home():
    """我是home函数的函数介绍"""
    print("welcome home")

home()