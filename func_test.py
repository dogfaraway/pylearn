# print('abc',end='\n\n')
# print('abc',end='\n')

# def func(a,b,c):
#     print('a=%s' %a )
#     print('b=%s' %b)
#     print('c=%s' %c)
#
# func(1,2,'a')

# 取得参数的个数
# def howlong(first, *other):
#     print(1+len(other))
#
# howlong(12,456)

# var1 = 123
#
# def func():
#     global var1
#     var1 = 456
#     print(var1)
#
# func()
# print(var1)

# list1 = [1,2,3]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# def frange(start,stop,step):
#     x = start
#     while x < stop:
#         yield(x)
#         x += step
#
# for i in frange(10, 20, 0.5):
#     print(i)

from decimal import Decimal
a = Decimal('1')
b = Decimal('0.2')
print(a+b+b+b)