with open(r'C:\Users\f1316\Desktop\All Python Project\biaozhun\biaozhun\log\log.txt', mode='rt', encoding='utf-8') as f:
    length = 0
    for line in f:
        length += len(line)
    f.seek(0, 0)
    res = sum(len(line) for line in f)
    print(res)
    print(length)
