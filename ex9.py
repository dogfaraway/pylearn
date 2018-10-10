# 1. 创建一个函数，用于接收用户输入的数字，并计算用户输入数字的和
# def recv(First=0):
#     num_input = list(input('please input number'))
#     num1, *_, num2 = num_input
#
#     print(type(num_input))
#     print(int(num1) + int(num2))
#
#
# recv()

# 2. 创建一个函数，传入n个整数，返回其中最大的数和最小的数
# def func3(*nums):
#     print(max(list(nums)))
#     print(min(list(nums)))
#     print(sum(nums))
#
#
# func3(1, 2, 3)

# 3. 创建一个函数，传入一个参数n，返回n的阶乘
import time


def timeer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('运行了 %s 秒' % (stop_time - start_time))

    return wrapper


x = int(input('please input integer'))


@timeer
def func_p():
    p = 1
    for i in range(1, x + 1):
        p *= i
    print(p)

func_p()


@timeer
def fact(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fact(x - 1)

# 使用高阶函数
from functools import reduce
num4 = 10
print(reduce(lambda x, y: x * y, range(1, num4 + 1)))

print(fact(x))
