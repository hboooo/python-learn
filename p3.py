import calendar
import datetime
import time

# 各个进制之间转换
dec = 10
print("十进制数为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))

c = 'c'
a = 116
print("{}的ASCII码为{}".format(c.rjust(3,' '),ord(c)))
print("{}对应的字符为{}".format(str(a).rjust(3,' '),chr(a)))

# 日历
print(calendar.month(2021,7))
print(calendar.monthrange(2021,7))

# 获取昨天日期
def getYesterday1():
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday  
    return yesterday

def getYesterday2():
    return datetime.date.today() + datetime.timedelta(-1)

print(datetime.timedelta(1))
print(datetime.timedelta(-1))
print(getYesterday1())
print(getYesterday2())

  
print('按下回车开始计时，按下 Ctrl + C 停止计时。')
while True:
    
    input("") # 如果是 python 2.x 版本请使用 raw_input() 
    starttime = time.time()
    print('开始')
    try:
        while True:
            print('计时: ', round(time.time() - starttime, 2), '秒', end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print('结束')
        endtime = time.time()
        print('总共的时间为:', round(endtime - starttime, 2),'secs')
        break
