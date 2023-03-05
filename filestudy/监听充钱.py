import time

with open('charge.log', mode='rt', encoding='utf-8') as f:
    f.seek(0, 2)
    while True:
        res = f.readline()
        if res:
            print(res)
        time.sleep(0.2)
