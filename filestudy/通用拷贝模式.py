with open('data/wallhaven-1pk58v.jpg', mode='rb') as f, open('data/new.jpg', mode='wb') as f1:
    while True:
        res = f.read(1024)
        if not res:
            break
        f1.write(res)
