group_list = []


def print_all_binary(n, prefix=""):
    if n == 0:
        print(f'{prefix}')
    else:
        print_all_binary(n - 1, prefix + "0")
        print_all_binary(n - 1, prefix + "1")


print_all_binary(6)
