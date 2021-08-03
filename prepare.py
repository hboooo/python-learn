import sys
import iterDemo

# 赋值 循环
a, b = 0, 1
while b < 10000:
    print(b, end=',')
    a, b = b, a+b
print()

# while 循环使用else
count = 0
while(count < 5):
    print(count, "小于5")
    count += 1
else:
    print(count, "大于或等于5，退出循环")

# for 循环与使用else
# 循环语句可以有 else 子句，
# 它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，
# 但循环被 break 终止时不执行。
for i in range(0, 9):
    print(i, "小于9")
else:
    print("退出循环")

for n in range(1, 50):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, "*", n//x)
            break
    else:
        print(n, "是质数")

# pass 语句是空语句，是为了保持程序结构的完整性
i = 1
if i == 1:
    pass
else:
    print("It is a test")

# 迭代器 自定义迭代器
it1 = iter('Why is Python')
print(next(it1))
print(next(it1))
print(next(it1))
for x in it1:
    print(x,end=" ")
print('')
it2 = iter("Why not is Python")
for x in it2:
    print(x,end=" ")
print()

itDemo = iterDemo.iterTest()
it3 = iter(itDemo)
print(next(it3))
print(next(it3))
print(next(it3))

for x in it3:
    print(x)

# 生成器
def fibonacci(n):
    a,b,counter = 0,1,0
    while True:
        if counter>n:
            return 
        yield b
        a,b = b,a+b
        counter +=1
f=fibonacci(10)
for x in f:
    print(x,end=' ')     
print()

# 函数
def pow(x):
    return '{}的平方是{}'.format(x, x**2)
print(pow(5))
#默认参数/关键字参数
def pow2(x,y=1):
    return '{}的{}次方是{}'.format(x,y,x**y)
print(pow2(x=2))
print(pow2(x=2,y=8))
# 不可变参数/可变参数
def change(a, l1):
    print(id(a))
    print(id(l1))
    print(a)
    print(l1)
    a = 10
    l1[0]='test'
    print(id(a))
    print(id(l1))
    print(a)
    print(l1)
b = 1
l2 = [1,2,3]
print(id(b))
change(b,l2)    
print(b)
print(l2)
# 不定长参数
def appendlist(*l1):
    for i in l1:
        yield i
f1 = appendlist(1,2,3,4)
for x in f1:
    print(x)
f2 = appendlist()
for x in f2:
    print(x)
def appendlist2(a1,**l1):
    print(a1)
    print(l1)
appendlist2('中',a=2,b=3,c=4)
# 匿名函数
sum = lambda a1,a2: a1+a2
print(sum(10,10))
print(sum(10,20))
# * /
# *后的参数必须用关键字传入
# /前的参数必须用指定位置参数
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

# 列表推导式
vec = [2,4,6]
t1 = [3*x for x in vec]
print(t1)
t2 = tuple(t1)
print(t2)
t3 = [[x,3*x] for x in vec]
print(t3)
print(['{}乘以3是{}'.format(x,x*3) for x in vec])
t4 = ['  banana', '  loganberry ', 'passion fruit  ']
t5 = [x.strip() for x in t4]
print(t5)
t6 = [3*x for x in vec if x >3]
print(t6)
t7 = [3*x for x in vec if x <=2]
print(t7)
# 嵌套列表解析
vec1=[2,4,6]
vec2=[4,3,-9]
t8 = [x*y for x in vec1 for y in vec2]
print(t8)
t9 = [x+y for x in vec1 for y in vec2]
print(t9)
t10 = [vec1[i]*vec2[i] for i in range(len(vec2))]
print(t10)
t11 ={'a':'A','b':'B'}
print(['{}--'.format(k) for k in t11.keys()])
print([str(round(355/113,i)) for i in range(1,7)])
# 矩阵转换
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],]
print([row for row in matrix])
print([[row[i] for row in matrix] for i in range(4)])
trans = []
for i in range(4):
    trans_row = []
    for row in matrix:
        trans_row.append(row[i])
    trans.append(trans_row)
print(trans)
# 遍历索引和元素
l1 = [ 'abcd', 786 , 2.23, 'python', 70.2 ]
for i,v in enumerate(l1):
    print(i,v)
# 多个列表遍历
l2 = ['name', 'quest', 'favorite color']
l3 = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(l2,l3):
    print('What is your {}? It is {}'.format(q,a))
# 反向遍历
for x in reversed(range(1,10,2)):
    print(x,end=' ')
print()
# 顺序遍历 排序
for x in sorted(set(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])):
    print(x)
