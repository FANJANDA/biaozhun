import random

print(random.random())  # 0-1的随机小数
print(random.uniform(1, 10))  # >1 <10的小数
print(random.randint(-100, 100))  # 闭区间
print(random.randrange(1, 3))  # 左闭右开
print(random.choice([1, 2, 4, ('张大仙', '烫头')]))
print(random.sample([1, 2, 4, ('张大仙', '烫头')], 2))
li = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(li)
print(li)  # 列表是可变的对象
