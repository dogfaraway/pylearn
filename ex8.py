#在Python程序中，分别使用未定义变量、访问列表不存在的索引、访问字典不存在的关键字观察系统提示的错误信息

# 使用未定义变量
# i+j

# 访问列表不存在的索引
# list_a = ['a',1,'c']
# print(list_a[4])

# 访问字典不存在的key
# dict_a = {'a':1,'b':2}
# print(dict_a['c'])


#通过Python程序产生IndexError，并用try捕获异常处理

try:
    list_b = ['a','b','c']
    print(list_b[3])
except Exception as a:
    print(' 发生错误：%s ' % a)