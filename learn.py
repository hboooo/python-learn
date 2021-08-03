import keyword

# 关键字
print('关键字:')
print(keyword.kwlist)

# 注释
# 单行注释
print("单行注释以#开头")
'''
print('Visual Studio Code')
print('Visual Studio Code for python')
'''
print("多行注释''',\"\"\"")

# print输出
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""
x="a"
y="b"
# 换行输出
print(x)
print(y)
# 不换行输出
print(x, end=" ")
print(y, end="")
print()

# 字符串
# 使用',"","""指定一个字符串
word = 'One world, one dream'
sentence = "Where there is a will, there is a way"
paragraph = """  这是一个段落
我家院子外面有两颗枣树，一个是枣树，另一颗也是枣树"""
print(word)
print(sentence)
print(paragraph)
# 转义符\ ，r反斜杠不发生转义
path1 = "C:\\Users\\habo\\Pictures\\111.jpg"
path2 = r"C:\Users\habo\Pictures\111.jpg"
print(path1)
print(path2)
# 字符串可以用+运算符连接，用*运算符重复
# 字符串的索引方式，从左往右以0开始，从右往左以-1开始
# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
strtest = 'environment'
print(strtest)                 # 输出字符串
print(strtest[0:-1])           # 输出第一个到倒数第二个的所有字符
print(strtest[0])              # 输出字符串第一个字符
print(strtest[2:5])            # 输出从第三个开始到第五个的字符
print(strtest[2:])             # 输出从第三个开始后的所有字符
print(strtest[1:10:2])         # 输出从第二个开始到第十个且每隔一个的字符（步长为2）
print(strtest[-5:-1])          # 输出从倒数第五个开始到倒数第二个
print(strtest[-8])             # 输出倒数第8个字符
print(strtest * 2)             # 输出字符串两次
print(strtest + ' hello')      # 连接字符串
print('hello\npython')     # 使用反斜杠(\)+n转义特殊字符
print(r'hello\npython')    # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# 等待用户输入
# key = input('请输入任意键继续')
# print("您输入了:"+key)

# 同一行使用多条语句
print("One world"); print("One dream")

# 多个语句构成代码组
# 像if、while、def和class这样的复合语句，
# 首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
print("""例如：
if i==0: 
   y='a'
elif i==1: 
   y='b' 
else: 
   y='c'""")
i = 1
if i==0:
    print("输出y='a'")
elif i==1:
    print("输出y='b'")
else:
    print("输出y='c'")

# 基本数据类型
# 变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
counter = 100                     # 整型变量
miles   = 1000.0                  # 浮点型变量
name    = "runoob"                # 字符串
print (counter)
print (miles)
print (name)
a = b = c = "1"                   # 同时为多个变量赋值
print(a+b+c)
a,b,c = "1","3","python"          # 为多个变量分别赋值
print(a+b+c)

# 标准数据类型
# Python3 中有六个标准的数据类型：
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Set（集合）
# Dictionary（字典）
# Python3 的六个标准数据类型中：
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）
# Number（数字）支持 int、float、bool、complex（复数）
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))   # 用户type()获取类型
print(isinstance(a, int))                   # 用isinstance来判断类型
# 删除对象引用
var1,var2,var3=1,10,"abc"
del var1
del var2,var3

# 数值运算
print(5+3)                # 加法
print(5-3)                # 减法
print(5*3)                # 乘法
print(5/3)                # 除法，得到一个浮点数
print(5//3)               # 除法，得到一个整数
print(5%3)                # 取余
print(5**3)               # 乘方

# 列表 (List)
# 列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
# 变量[头下标:尾下标]
list1 = [ 'abcd', 786 , 2.23, 'python', 70.2 ]
tinylist = [123, 'python']
print(list1)            # 输出完整列表
print(list1[0])         # 输出列表第一个元素
print(list1[1:3])       # 从第二个开始输出到第三个元素
print(list1[2:])        # 输出从第三个元素开始的所有元素
print(tinylist * 2)    # 输出两次列表
print(list1 + tinylist) # 连接列表
# 修改list元素
list1[0]=999
print("第一次修改后:",list1)
list1[2:4]=["aaa",8980]
print("第二次修改后:",list1)
list1[2:4]=[]  # 将对应的元素值设置为 []
print("第三次修改后:",list1)

# 元组 (Tuple)
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
tuple1 = ( 'abcd', 786 , 2.23, 'python', 70.2  )
tinytuple = (123, 'python')
print (tuple1)             # 输出完整元组
print (tuple1[0])          # 输出元组的第一个元素
print (tuple1[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple1[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple1 + tinytuple) # 连接元组
tup1 = ()                 # 空元组
tup2 = (20,)              # 一个元素，需要在元素后添加逗号

# 集合(Set)
# 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，
# 因为 { } 是用来创建一个空字典。
# 创建格式：parame = {value01,value02,...} 或者 set(value)
sites = {'Google', 'Taobao', 'Python', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)   # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Python' in sites:
    print('Python 在集合中')
else:
    print('Python 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素

# 字典(Dictionary)
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
# 键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。
dict1 = {}
dict1['one'] = "1 - Python"
dict1[2]     = "2 - test"
tinydict = {'name': 'Python','code':1, 'site': 'https://www.python.org'}

print (dict1['one'])       # 输出键为 'one' 的值
print (dict1[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

# 数据类型转换
# int()将一个字符串或数字转换为整型 语法：class int(x, base=10)
a = int()
b = int(3)
c = int(3.6)
d = int('12', 16)     # 如果是带参数base的话，12要以字符串的形式进行输入，12为16进制
e = int('0xa', 16)
f = int('10', 8)
print(a,b,c,d,e,f)
# float()将整数和字符串转换成浮点数 语法：class float([x])
a = float(1)
b = float(112)
c = float(-123.6)
d = float('123')
print(a,b,c,d)
# str()将对象转化为适于人阅读的形式 语法：class str(object='')
s = 'Python'
dict1 = {'python': 'python.com', 'google': 'google.com'}
print(str(s))
print(str(dict1))
# repr()将对象转化为供解释器读取的形式 语法：repr(object)
print(repr(s))
print(repr(dict1))
# eval()执行一个字符串表达式，并返回表达式的值 语法：eval(expression[, globals[, locals]])
x=7
print(eval('3*x'))
print(eval('pow(2,3)'))
print(eval('2+x'))
print(eval("6+6"))
# tuple()将可迭代系列（如列表）转换为元组 语法：tuple(iterable)
list1= ['Google', 'Taobao', 'Python', 'Baidu']
print(tuple(list1))
# list() 将元组或字符串转换为列表 语法：list(seq)   seq -- 要转换为列表的元组或字符串。
tuple1 = (123, 'Google', 'Python', 'Taobao')
tuple2 = 12,23,4,345,'asd'
print(tuple1)
print(tuple2)
# set() 创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等 语法：class set([iterable])
print(set('Python'))
print(set('huawei'))
print(set('google'))  # 重复的被删除
set1 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(set1)
if 'asldkjasd' in set1:
    print('asldkjasd 在set1中')
else:
    print('asldkjasd 不在set1中')

# dict() 创建一个字典 语法：class dict(**kwarg);class dict(mapping, **kwarg);class dict(iterable, **kwarg)
print(dict())                                          # 创建空字典
print(dict(a='a',b='b',c='c'))                         # 传入关键字
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))   # 映射函数方式来构造字典
print(dict([('one', 1), ('two', 2), ('three', 3)]))    # 可迭代对象方式来构造字典
dict1 = {'sape': 4139, 'guido': 4127, 'jack': 4098}
print(dict1.keys())
print(dict1.values())
for k,v in dict1.items():
    print("字典的key:{},value:{}".format(k,v))
dict2 = {x:x**2 for x in (1,2,4,8)}
print(dict2)
# frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素 语法：class frozenset([iterable])
a = frozenset(range(10))     # 生成一个新的不可变集合
b = frozenset('runoob')
print(a,b)
# chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
print(chr(0x30), chr(0x31), chr(0x61))   # 十六进制
print(chr(48), chr(49), chr(97))         # 十进制
# ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
# 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
# 如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
print(ord('a'),ord('b'),ord('c'))
print(ord('1'),ord('*'),ord('/'))
# hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
print(hex(255),hex(-42),hex(0x1a),hex(12))
print(type(hex(12)))       # 字符串
# oct() 函数将一个整数转换成8进制字符串
print(oct(10),oct(20),oct(30))
print(type(oct(12)))       # 字符串