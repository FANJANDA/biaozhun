def g_outer(x):
    def outer(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res

        return wrapper

    return outer
