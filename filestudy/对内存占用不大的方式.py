import os

with open('data/k.txt', mode='rt', encoding='utf-8') as f,\
        open('data/.k.swap', mode='wt', encoding='utf-8') as f1:
    for line in f:
        new_res = line.replace('一天', '一年')
        f1.write(new_res)
os.remove('data/k.txt')
os.rename('data/.k.swap', 'data/k.txt')
