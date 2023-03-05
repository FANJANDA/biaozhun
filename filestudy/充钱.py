while True:
    with open('charge.log', mode='at', encoding='utf-8') as f:
        money = input('请问你要充多少钱')
        str_123 = f'张大仙充值了{money}w元\n'
        f.write(str_123)
