with open('./data/1.txt', 'rt', encoding='utf-8') as f:
    res = f.read()
    print(res)
    l = list(res)
    l.insert(3, '不')
    print(l)
    print(''.join(l))
    new_res = res.replace('我喜欢你','我不喜欢你')
    print(new_res)

with open('./data/1.txt', 'wt', encoding='utf-8') as f:
    f.write(new_res)
