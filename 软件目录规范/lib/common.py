import time
from 软件目录规范.conf.settings import LOG_PATH


def logger(msg):
    with open(LOG_PATH, mode='at', encoding='UTF-8') as f:
        f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} {msg}\n')
