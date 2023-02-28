# 随机生成一个16位的密码 必须包含大写字母 小写字母 和符号
import random

pwd = ''
print(chr(89))
print(ord('Y'))
char_list = [[97, 122], [65, 90], [48, 57], [33, 47]]

for _ in range(2):
    random_list = random.choice(char_list)
    print(random_list)
    random_char = chr(random.randint(*random_list))  # 用作实参是打散
    # print(random.randint(*random_list))

    print(random_char)
