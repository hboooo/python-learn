# 导入 cmath(复杂数学运算) 模块
import cmath

# 计算二次方根
a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))
 
# 计算
d = (b**2) - (4*a*c)
 
# 两种求解方式
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
 
print('结果为 {0} 和 {1}'.format(sol1,sol2))


# 计算三角形的面积
a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))
 
# 计算半周长
s = (a + b + c) / 2
 
# 计算面积
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('三角形面积为{}'.format(area))


# 计算圆面积
def findArea(r):
    PI = 3.142
    return PI*(r*r)
print("圆的面积为{}".format(findArea(10)))