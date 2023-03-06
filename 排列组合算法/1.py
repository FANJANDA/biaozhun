s = 'abc'
li = list(s)


def permutation(l, level):
    if level == len(l):
        print(l)
    for i in range(level, len(l)):
        l[level], l[i] = l[i], l[level]
        permutation(l, level + 1)
        l[level], l[i] = l[i], l[level]


permutation(li, 0)


def print_all_binary(n, prefix=""):
    if n == 0:
        print(prefix)
    else:
        print_all_binary(n - 1, prefix + "0")
        print_all_binary(n - 1, prefix + "1")
