import sys
from iterDemo import iterTest
import pickle
import builtins
import os
import shutil
import glob

print('命令行参数如下')
for i in sys.argv:
    print(i)

print('Python路径为：')
for x in sys.path:
    print(x)

test = iterTest()
l1 = iter(test)
for x in l1:
    print(x)
print(iterTest.__name__)


print(dir(iterTest))
print(dir(sys))
print(dir())

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list+=selfref_list
print(selfref_list)
output = open('data.pkl', 'wb')

pickle.dump(data1, output)
pickle.dump(selfref_list, output, -1)
pickle.dump(selfref_list, output, -1)

output.close()

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
print(data1)
data2 = pickle.load(pkl_file)
print(data2)
data3 = pickle.load(pkl_file)
print(data3)

pkl_file.close()

while True:
    try:
        # x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")

def runoob():
    pass

try:
    runoob()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论异常是否发生都会执行。')

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

print(dir(builtins))
print(os.getcwd())
print(dir(os))
print(dir(shutil))

print(glob.glob('*.py'))
print(glob.glob('*.pkl'))

for i in [1,0]:
    print(i+1)