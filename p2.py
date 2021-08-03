import random

# 生成随机数
print(random.random())
print(random.randint(0,100))
print(random.randbytes(3))
print(random.randrange(0,100))

# 交换变量
x = 2
y = 3
x,y = y,x
print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))

# 判断字符串是否为数字
def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        pass
    
    try:
        import unicodedata
        unicodedata.numeric(x)
        return True
    except (TypeError,ValueError):
        pass

    return False

print(is_number('a'))
print(is_number(1))
print(is_number('ab'))
print(is_number('四'))
print(is_number('个'))

# 判断是否为闰年
def year(y):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

for x in range(1900,2001):
    if year(x):
        print('{}是闰年'.format(x))


# 最大值
print(max(1, 2))
print(max('a', 'b'))
print(max([1,2]))
print(max((1,2)))
print("80, 100, 1000 最大值为: ", max(80, 100, 1000))
print("-20, 100, 400最大值为: ", max(-20, 100, 400))
print("-80, -20, -10最大值为: ", max(-80, -20, -10))
print("0, 100, -400最大值为:", max(0, 100, -400))

# 九九乘法表
print('==============================================================')
for x in range(1,10):
    for y in range(1,x+1):
        print("{}*{}={}".format(y,x,str(x*y).zfill(2)),end=' ')
    print()
print('==============================================================')