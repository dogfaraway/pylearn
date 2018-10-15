## 练习一 定义装饰器，用于打印函数执行的时间

# 统计函数开始执行和结束执行的时间
import time
import datetime


def timer(func):
    def wrapper():
        print('start time: %s' % datetime.datetime.now())
        func()
        print('stop time: %s' % datetime.datetime.now())

    return wrapper()


@timer
def test_func():
    print('this is a test')


test_func()

# 扩展练习：为装饰器传入超时时间，函数执行超过指定时间后退出


# 练习二 定义装饰器，实现不同颜色显示执行结果的功能
# 向装饰器传递参数，通过传递的参数获取到输出的颜色
# 被装饰函数的print( )输出根据装饰器得到的颜色进行输出
